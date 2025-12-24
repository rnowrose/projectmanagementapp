import pytest
from datetime import datetime
from app.models.projects import Projects
from app.models.apps import Apps
from app.models.users import Users
from app.util.const import WorkType


class TestProjects:
    @pytest.fixture(autouse=True)
    def setUp(self):
        """Set up test database and test data"""
        # Create test user
        user = Users.create_user(
            username="testuser",
            password="test123",
            first_name="Test",
            last_name="User"
        )
        self.user = user
        
        # Create test app
        app = Apps.create(
            name="Test App",
            timestamp=datetime(2023, 1, 1),
            description="A test app",
            work_type=WorkType.PERSONAL_PROJECT,  # Store enum value as string
            host="localhost",
            user=user  # Link to user
        )
        self.app = app
        
        # Create test project
        project = Projects.create(
            name="Test Project",
            start_date=datetime(2023, 1, 1),
            end_date=datetime(2023, 12, 31),
            timestamp=datetime(2023, 1, 1),
            description="A test project",
            release="v1.0",
            app=app  # Link to app using foreign key
        )
        self.project = project

    def test_create_project(self):
        """Test project creation"""
        assert self.project.id is not None
        assert self.project.name == "Test Project"
        assert self.project.app.id == self.app.id
    
    def test_get_projects(self):
        """Test retrieving projects"""
        projects = list(Projects.select())  # Get all projects
        assert len(projects) == 1
        assert projects[0].name == "Test Project"
        
    def test_project_relationships(self):
        """Test foreign key relationships"""
        # Test project -> app relationship
        assert self.project.app.name == "Test App"
        
        # Test app -> projects relationship (via backref)
        app_projects = list(self.app.projects)
        assert len(app_projects) == 1
        assert app_projects[0].name == "Test Project"
        
    def test_project_queries(self):
        """Test various project queries"""
        # Query by name
        project = Projects.get(Projects.name == "Test Project")
        assert project.id == self.project.id
        
        # Query by app
        projects_for_app = Projects.select().where(Projects.app == self.app)
        assert len(list(projects_for_app)) == 1
        
        # Query with join
        projects_with_app = (Projects
                           .select()
                           .join(Apps)
                           .where(Apps.name == "Test App"))
        assert len(list(projects_with_app)) == 1
