from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Database settings
DATABASE_URL = "postgresql://default:reF43CaPdbGV@ep-dawn-snow-a1702yle.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    def __init__(self, user_data):
        """
        Initializes a User object from a dictionary containing user data.

        Args:
            user_data (dict): A dictionary with keys matching the User class attributes.
        """

        for key, value in user_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise ValueError(f"Invalid key '{key}' in user data")
            
def insert(orm_model, **param):
    try:
        db = SessionLocal()
        data = orm_model(param)
        db.add(data)
        db.commit()
        db.refresh(data)
        return 200, ''
    except Exception as e:
        return 404, f'Failed: {e}'
    
def search(orm_model, **param):
    db = SessionLocal()
    result = db.query(orm_model).filter_by(email = param['email']).first()
    return result

# Create database tables
Base.metadata.create_all(bind=engine)
