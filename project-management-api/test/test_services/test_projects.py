from app.service.projects import *
import pytest
from peewee import *
from datetime import datetime
from app.models import Users, Apps, Projects
from app.util.const import WorkType

class TestProjectService:
    @pytest.fixture(autouse=True)
    def setUp(self):
        """Set up test database and test data"""
        # Create test user
        user = Users.create_user(
            username="serviceuser",
            password="serv123",
            first_name="Service",
            last_name="User"
        )
        self.user = user
        
        # Create test app
        app = Apps.create(
            name="Service App",
            timestamp=datetime(2023, 1, 1),
            description="A service app",
            work_type=WorkType.PERSONAL_PROJECT,  # Store enum value as string
            host="localhost",
            user=user  # Link to user
        )
        self.app = app
        
        # Create test project
        project = Projects.create(
            name="Service Project",
            start_date=datetime(2023, 1, 1),
            end_date=datetime(2023, 12, 31),
            timestamp=datetime(2023, 1, 1),
            description="A service project",
            release="v1.0",
            app=app  # Link to app using foreign key
        )
        self.project = project

    def test_get_projects_by_app_id(self):
        """Test retrieving projects by app ID"""
        projects = get_projects_by_app_id(self.app.id)
        assert len(projects) == 1
        assert projects[0].name == "Service Project"
        
    def test_get_app_by_id(self):
        """Test retrieving app by ID"""
        app = get_app_by_id(self.app.id)
        assert app is not None
        assert app.name == "Service App"
        
    def test_get_apps(self):
        """Test retrieving apps for a user"""
        apps = get_apps(self.user)
        assert len(apps) == 1
        assert apps[0].name == "Service App"

