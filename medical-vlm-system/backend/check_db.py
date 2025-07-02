from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from models.models import User, Diagnosis, DiagnosisResult

load_dotenv()

SQLALCHEMY_DATABASE_URL = (
    f"mysql+mysqlconnector://"
    f"{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@"
    f"{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/"
    f"{os.getenv('MYSQL_DATABASE')}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def check_database():
    db = SessionLocal()
    try:
        # Check users table
        users = db.query(User).all()
        print("\nUsers in database:")
        for user in users:
            print(f"ID: {user.id}, Email: {user.email}, Name: {user.full_name}")

        # Check diagnoses table
        diagnoses = db.query(Diagnosis).all()
        print("\nDiagnoses in database:")
        for diagnosis in diagnoses:
            print(f"ID: {diagnosis.id}, User ID: {diagnosis.user_id}, Status: {diagnosis.status}")

        # Check diagnosis_results table
        results = db.query(DiagnosisResult).all()
        print("\nDiagnosis Results in database:")
        for result in results:
            print(f"ID: {result.id}, Diagnosis ID: {result.diagnosis_id}, Disease: {result.disease_name}")

    finally:
        db.close()

if __name__ == "__main__":
    check_database() 