from peewee import *

from app.models.payments import Payments
from app.models.revenue import Revenue
from app.models.expenses import Expenses
from app.util.exceptions import PaymentException, RevenueException
from app.dto.payments import PaymentDTO

def create_payment(payment: PaymentDTO) -> Payments:
    payment = Payments.create(
        amount=payment.amount,
        payment_type=payment.payment_type,
        comment=payment.comment,
        app=payment.app
    )
    if not payment:
        raise PaymentException("Failed to create payment")
    return payment

def create_expenses(expense: Expenses) -> Expenses:
    expense = Expenses.create(
        name=expense.name,
        description=expense.description,
        date=expense.date,
        amount=expense.amount,
        categories=expense.categories,
        payments=expense.payments,
        app=expense.app
    )
    if not expense:
        raise PaymentException("Failed to create expense")
    return expense

def create_revenue(revenue: Revenue) -> Revenue:
    revenue = Revenue.create(
        name=revenue.name,
        description=revenue.description,
        date=revenue.date,
        amount=revenue.amount,
        categories=revenue.categories,
        payments=revenue.payments,
        app=revenue.app
    )
    if not revenue:
        raise RevenueException("Failed to create revenue")
    return revenue

def create(payment: Payments, revenue: Revenue, app_id: int) -> None:
    if app_id:
        create_payment(payment)
        create_revenue(revenue)
    else:
        raise PaymentException("App ID is required to create payment and revenue")
        
def get_revenue(app_id: int):
    revenues = Revenue.select(Revenue, Payments).join(Payments).where(Revenue.app_id == app_id)
    if not revenues:
        raise RevenueException("No revenues found for this app")
    return revenues

def get_expenses(app_id: int):
    expenses = Expenses.select(Expenses, Payments).join(Payments).where(Expenses.app_id == app_id)
    if not expenses:
        raise PaymentException("No expenses found for this app")
    return expenses

def update_payment(payment_id: int, updated_payment: Payments) -> Payments:
    payment = Payments.get_or_none(Payments.id == payment_id)
    if not payment:
        raise PaymentException("Payment not found")
    payment.amount = updated_payment.amount
    payment.payment_type = updated_payment.payment_type
    payment.comment = updated_payment.comment
    payment.app = updated_payment.app
    payment.save()
    return payment

def update_revenue(revenue_id: int, updated_revenue: Revenue) -> Revenue:
    revenue = Revenue.get_or_none(Revenue.id == revenue_id)
    if not revenue:
        raise RevenueException("Revenue not found")
    revenue.name = updated_revenue.name
    revenue.description = updated_revenue.description
    revenue.date = updated_revenue.date
    revenue.amount = updated_revenue.amount
    revenue.categories = updated_revenue.categories
    revenue.payments = updated_revenue.payments
    revenue.app = updated_revenue.app
    revenue.save()
    return revenue


