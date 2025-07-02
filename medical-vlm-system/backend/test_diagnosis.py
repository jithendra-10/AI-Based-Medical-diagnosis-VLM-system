import os
import requests
from services.online_medical_service import OnlineMedicalService
from fastapi import FastAPI, UploadFile, File
from fastapi.testclient import TestClient
import json

app = FastAPI()
client = TestClient(app)
online_service = OnlineMedicalService()

def test_diagnosis_system():
    # Example 1: Test with a skin image (melanoma)
    print("\nTesting with skin image (melanoma)...")
    image_path = "test_images/melanoma.jpg"  # You'll need to add this image
    symptoms = "irregular mole, growing in size, dark pigmentation"
    
    result = online_service.get_comprehensive_diagnosis(
        image_path=image_path,
        symptoms=symptoms
    )
    
    print("\nDiagnosis Results:")
    print(json.dumps(result, indent=2))
    
    # Example 2: Test with chest X-ray (pneumonia)
    print("\nTesting with chest X-ray (pneumonia)...")
    image_path = "test_images/pneumonia_xray.jpg"  # You'll need to add this image
    symptoms = "cough, fever, difficulty breathing"
    
    result = online_service.get_comprehensive_diagnosis(
        image_path=image_path,
        symptoms=symptoms
    )
    
    print("\nDiagnosis Results:")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    # Create test images directory if it doesn't exist
    os.makedirs("test_images", exist_ok=True)
    
    # Run the test
    test_diagnosis_system() 