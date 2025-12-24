import pytest
from datetime import datetime
from app.models import Payments, Apps, Users
from app.util.const import PaymentType

class TestPayments:
    @pytest.fixture(autouse=True)
    def setUp(self):
        """Set up test database and test data"""
        # Create test user
        user = Users.create_user(
            username="paymentuser",
            password="pay123",
            first_name="Payment",
            last_name="User"
        )
        self.user = user
        
        # Create test app
        app = Apps.create(
            name="Payment App",
            timestamp=datetime(2023, 1, 1),
            description="A payment app",
            work_type="PERSONAL_PROJECT",  # Store enum value as string
            host="localhost",
            user=user  # Link to user
        )
        self.app = app
        
        # Create test payment
        payment_without_comment = Payments.create(
            amount=100.0,
            payment_type=PaymentType.HOURLY,  # Store enum value as string
            timestamp=datetime(2023, 1, 1),
            description="A test payment",
            app=app  # Link to app using foreign key
        )
        
        payment_with_comment = Payments.create(
            amount=100.0,
            payment_type=PaymentType.HOURLY,  # Store enum value as string
            timestamp=datetime(2023, 1, 1),
            description="A test payment",
            app=app,  # Link to app using foreign key
            comment="Test payment with comment"
        )
        self.payment_with_comment = payment_with_comment
        self.payment_without_comment = payment_without_comment

    def test_create_payment_without_comment(self):
        """Test payment creation without comment"""
        assert self.payment_without_comment.id is not None
        assert self.payment_without_comment.amount == 100.0
        assert self.payment_without_comment.payment_type == PaymentType.HOURLY
        assert self.payment_without_comment.app.id == self.app.id
    
    def test_create_payment_with_comment(self):
        """Test payment creation with comment"""
        assert self.payment_with_comment.id is not None
        assert self.payment_with_comment.amount == 100.0
        assert self.payment_with_comment.payment_type == PaymentType.HOURLY
        assert self.payment_with_comment.comment == "Test payment with comment"
        assert self.payment_with_comment.app.id == self.app.id

    def test_get_payments(self):
        """Test retrieving payments"""
        payments = list(Payments.select())  # Get all payments
        print(payments)
        assert len(payments) == 2
        assert payments[0].amount == 100.0
        
    def test_payment_relationships(self):
        """Test foreign key relationships"""
        # Test payment -> app relationship
        assert self.payment_without_comment.app.name == "Payment App"
        # Test payment -> user relationship
        assert self.payment_without_comment.app.user.id == self.user.id