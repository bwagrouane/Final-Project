from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import conf

# IF YOU WANT TO SEE IT ON YOUR LOCAL MYSQL UNCOMMENT BELOW VVVVV
# SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{conf.user}:{quote_plus(conf.password)}@{conf.host}:{conf.port}/{conf.database}?charset=utf8mb4"

# CURRENTLY ON A SHARED SQLITE FILE, COMMENT BELOW TO SWITCH TO LOCAL VVVVV
SQLALCHEMY_DATABASE_URL = "sqlite:///./warehouse_api.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
print(SQLALCHEMY_DATABASE_URL)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
