from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from starlette.middleware.base import BaseHTTPMiddleware
from app.db.database import db, create_schema
from app.models import *
from app.router import apps
from app.router import user
from fastapi.middleware.cors import CORSMiddleware

class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Application"] = "Project Management API"
        return response

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    if db.is_closed():
        db.connect() 
        create_schema('users')
        create_schema('project_management')
        create_schema('finance')
    db.create_tables([
        Users, 
        Clients,
        Apps,
        Projects,
        Tasks,
        Experiences,
        Education,
        Expenses,
        Payments,
        Categories,
        Revenue,
        UserIntegrations,
        Release,
        Skills,
        Accomplishment,
    ], safe=True)
    yield  # app runs here

    # Shutdown
    if not db.is_closed():
        db.close()

app = FastAPI(title="Project Management API", version="1.0.0", lifespan=lifespan, root_path="/api")
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(apps.router)
app.include_router(user.router)
app.add_middleware(CustomHeaderMiddleware)




@app.get("/")
async def root():
    return {"message": "Project Management API"}


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "database": "connected"}
