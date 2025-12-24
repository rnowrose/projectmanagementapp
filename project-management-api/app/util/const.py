from enum import Enum

class PaymentType(Enum):
    HOURLY = 'Hourly'
    MILESTONE = 'MileStone'
    PURCHASE = 'Purchase'
    SUBSCRIPTION = 'Subscription'
    FIXED_AMOUNT = 'Fixed Amount'
    

class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    QA = "qa"
    DONE = "done"
    CANCELLED = "cancelled"
    
class WorkType(Enum):
    FREELANCE = 'Freelance'
    PROFILE_PROJECT = 'Profile Project'
    INDIE_APP = 'Indie App'
    
class CategoryType(Enum):
    EXPENSE = 'Expense'
    REVENUE = 'Revenue'
    
class PriorityLevel(Enum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    URGENT = 'Urgent'
    
class PaymentStatus(Enum):
    NONE = 'None'
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    FAILED = 'Failed'
    REFUNDED = 'Refunded'
    CANCELLED = 'Cancelled'

class IntegrationType(Enum):
    GITHUB = 'GitHub'
    
class TaskType(Enum):
    FEATURE = 'Feature'
    BUG = 'Bug'
    IMPROVEMENT = 'Improvement'
    RESEARCH = 'Research'

class ProficiencyLevel(Enum):
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'
    EXPERT = 'Expert'

class AccomplishmentType(Enum):
    AWARD = 'Award'
    CERTIFICATION = 'Certification'
    PROJECT = 'Project'