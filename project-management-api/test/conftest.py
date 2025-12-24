
import os
os.environ["TESTING"] = "True"


import pytest
from app.db.database import db
from app.models import Users, Experiences, Apps, Projects, Expenses, Payments, Tasks, Revenue, Clients

@pytest.fixture(autouse=True)
def setup_and_teardown_db():
    db.bind([Users, Experiences, Revenue, Expenses, Apps, Projects, Payments, Tasks, Clients])
    db.connect()
    db.create_tables([Users, Experiences, Revenue, Expenses, Apps, Projects, Payments, Tasks, Clients], safe=True)
    yield
    db.drop_tables([Users, Experiences, Revenue, Expenses, Apps, Projects, Payments, Tasks, Clients])
    db.close()