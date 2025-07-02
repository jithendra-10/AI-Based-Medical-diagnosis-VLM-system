from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from models.models import Disease

load_dotenv()

SQLALCHEMY_DATABASE_URL = (
    f"mysql+mysqlconnector://"
    f"{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@"
    f"{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/"
    f"{os.getenv('MYSQL_DATABASE')}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def add_disease_data():
    db = SessionLocal()
    try:
        # Sample diseases data
        diseases = [
            {
                "name": "Melanoma",
                "description": "A type of skin cancer that develops from melanocytes, the cells that produce melanin.",
                "symptoms": "Asymmetrical moles, irregular borders, multiple colors, diameter larger than 6mm, evolving appearance",
                "visual_characteristics": "Irregular shaped lesions, dark pigmentation, uneven color distribution, raised surface",
                "treatment_options": "Surgical excision, immunotherapy, targeted therapy, radiation therapy",
                "related_conditions": "Skin cancer, dysplastic nevus syndrome, xeroderma pigmentosum",
                "dietary_recommendations": "Foods rich in antioxidants (berries, leafy greens), omega-3 fatty acids (fish, flaxseeds), vitamin D (fortified dairy, eggs), and beta-carotene (carrots, sweet potatoes). Avoid processed foods and excessive alcohol.",
                "precautions": "Regular skin checks, use sunscreen (SPF 30+), wear protective clothing, avoid peak sun hours (10am-4pm), stay hydrated, monitor moles for changes, avoid tanning beds",
                "is_curable": True
            },
            {
                "name": "Diabetic Retinopathy",
                "description": "A diabetes complication that affects eyes, caused by damage to the blood vessels of the light-sensitive tissue at the back of the eye (retina).",
                "symptoms": "Blurred vision, fluctuating vision, dark areas in vision, poor night vision, color vision impairment",
                "visual_characteristics": "Microaneurysms, hemorrhages, cotton wool spots, hard exudates, macular edema",
                "treatment_options": "Laser treatment, anti-VEGF injections, vitrectomy, blood sugar control",
                "related_conditions": "Diabetes mellitus, hypertension, hyperlipidemia",
                "dietary_recommendations": "Low glycemic index foods (whole grains, legumes), leafy greens, fatty fish, nuts, and seeds. Control portion sizes and maintain regular meal timing. Limit processed sugars and refined carbohydrates.",
                "precautions": "Regular eye exams, maintain blood sugar levels, control blood pressure, quit smoking, regular exercise, monitor vision changes, wear protective eyewear",
                "is_curable": False
            },
            {
                "name": "Pneumonia",
                "description": "An infection that inflames the air sacs in one or both lungs, which may fill with fluid.",
                "symptoms": "Cough with phlegm, fever, chills, difficulty breathing, chest pain",
                "visual_characteristics": "Consolidation on chest X-ray, pleural effusion, air bronchograms",
                "treatment_options": "Antibiotics, oxygen therapy, fluids, rest, fever reducers",
                "related_conditions": "Influenza, chronic obstructive pulmonary disease, asthma",
                "dietary_recommendations": "Hydrating fluids (water, herbal teas), vitamin C-rich foods (citrus fruits, bell peppers), protein-rich foods (lean meats, beans), warm soups, and easily digestible foods. Avoid dairy if producing excess mucus.",
                "precautions": "Get vaccinated (flu and pneumonia vaccines), practice good hygiene, avoid smoking, maintain indoor air quality, rest adequately, stay hydrated, avoid close contact with sick individuals",
                "is_curable": True
            }
        ]

        # Add diseases to database
        for disease_data in diseases:
            disease = Disease(**disease_data)
            db.add(disease)
        
        db.commit()
        print("Disease data added successfully!")

    except Exception as e:
        print(f"Error adding disease data: {str(e)}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    add_disease_data() 