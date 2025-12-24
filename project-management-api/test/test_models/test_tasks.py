import pytest
from app.models import Users, Apps, Projects, Tasks
from datetime import datetime
from app.util.const import WorkType, TaskStatus, TaskPriority


class TestTasks:
    @pytest.fixture(autouse=True)
    def setUp(self):
        """Set up test database and test data"""
        # Create test user
        user = Users.create_user(
            username="taskuser",
            password="task123",
            first_name="Task",
            last_name="User"
        )
        self.user = user
        
        # Create test app
        app = Apps.create(
            name="Task App",
            timestamp=datetime(2023, 1, 1),
            description="A task app",
            work_type=WorkType.PERSONAL_PROJECT,  # Store enum value as string
            host="localhost",
            user=user  # Link to user
        )
        self.app = app
        
        # Create test project
        project = Projects.create(
            name="Task Project",
            start_date=datetime(2023, 1, 1),
            end_date=datetime(2023, 12, 31),
            timestamp=datetime(2023, 1, 1),
            description="A task project",
            release="v1.0",
            app=app  # Link to app using foreign key
        )
        self.project = project
        
        # Create test task
        task = Tasks.create(
            name="Test Task",
            description="A test task",
            status=TaskStatus.TODO,  # Store enum value as string
            priority=TaskPriority.MEDIUM,  # Store enum value as string
            due_date=datetime(2023, 6, 30),
            project=project  # Link to project using foreign key
        )
        self.task = task

    def test_create_task(self):
        """Test task creation"""
        assert self.task.id is not None
        assert self.task.name == "Test Task"
        assert self.task.project.id == self.project.id
    
    def test_get_tasks(self):
        """Test retrieving tasks"""
        tasks = list(Tasks.select())  # Get all tasks
        assert len(tasks) == 1
        assert tasks[0].name == "Test Task"
        
    def test_task_relationships(self):
        """Test foreign key relationships"""
        # Test task -> project relationship
        assert self.task.project.name == "Task Project"
        
        # Test project -> tasks relationship (via backref)
        project_tasks = list(self.project.tasks)
        assert len(project_tasks) == 1
        assert project_tasks