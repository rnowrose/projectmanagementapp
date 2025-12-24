import os
import colorlog
import logging
import secrets
from peewee import PostgresqlDatabase, SqliteDatabase

formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
log = logging.getLogger(__name__)
log.addHandler(handler)
log.setLevel(logging.DEBUG)

formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)

SECRET_KEY = os.getenv("JWT_SECRET", secrets.token_urlsafe(64))
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "5000"))


TESTING = os.getenv("TESTING", "False")

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD") 
host = os.getenv("DB_HOST", "localhost")
port = int(os.getenv("DB_PORT", "5433"))
name = os.getenv("DB_NAME", "rownok-admin-dev")

if TESTING == "True":
    db = SqliteDatabase(":memory:")
    log.info("Using SQLite in-memory database for testing")
else:
    db = PostgresqlDatabase(user=user,
                       password=password,
                       host=host,
                       port=port,
                       database=name)
    log.info(f"Using PostgreSQL database: {name} at {host}:{port}")


def schema_exists(schema_name: str) -> bool:
    """Check if a PostgreSQL schema exists"""
    query = """
        SELECT EXISTS(
            SELECT 1 
            FROM information_schema.schemata 
            WHERE schema_name = %s
        )
    """
    cursor = db.execute_sql(query, (schema_name,))
    result = cursor.fetchone()
    return result[0] if result else False


def create_schema(schema_name: str = "public"):
    """Create PostgreSQL schema if it doesn't exist"""
    if schema_name == "public":
        log.info("Using default 'public' schema")
        return
    
    if schema_exists(schema_name):
        log.info(f"Schema '{schema_name}' already exists")
    else:
        with db:
            db.execute_sql(f'CREATE SCHEMA {schema_name}')
            log.info(f"Schema '{schema_name}' created successfully")
    
    # Set search path
    db.execute_sql(f'SET search_path TO {schema_name}, public')
    log.info(f"Search path set to '{schema_name}'")