from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from models.models import User, Diagnosis, DiagnosisResult
from passlib.context import CryptContext

load_dotenv()

SQLALCHEMY_DATABASE_URL = (
    f"mysql+mysqlconnector://"
    f"{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@"
    f"{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/"
    f"{os.getenv('MYSQL_DATABASE')}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def add_sample_data():
    db = SessionLocal()
    try:
        # Add sample users
        user1 = User(
            email="doctor@example.com",
            full_name="Dr. John Smith",
            hashed_password=pwd_context.hash("password123")
        )
        db.add(user1)
        db.commit()
        db.refresh(user1)

        # Add sample diagnoses
        diagnosis1 = Diagnosis(
            image_path="uploads/sample1.jpg",
            symptoms="Patient presents with joint hypermobility and skin elasticity",
            user_id=user1.id,
            status="completed"
        )
        db.add(diagnosis1)
        db.commit()
        db.refresh(diagnosis1)

        # Add sample diagnosis results
        result1 = DiagnosisResult(
            diagnosis_id=diagnosis1.id,
            disease_name="Ehlers-Danlos Syndrome",
            confidence=0.85,
            description="A group of inherited disorders affecting connective tissues"
        )
        db.add(result1)
        db.commit()

        print("Sample data added successfully!")

    except Exception as e:
        print(f"Error adding sample data: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_sample_data() 