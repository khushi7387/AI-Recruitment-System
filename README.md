# AI Recruitment System

## 1. Project Overview
The **AI Recruitment System** is a machine learning-based application designed to automate candidate screening using resumes. The system evaluates candidates’ skills, education, and experience to provide **quantitative insights** for HR teams, helping them make faster and more objective hiring decisions.  

This project demonstrates:  
- Loading and preprocessing resume datasets  
- Cleaning and extracting meaningful features from resumes  
- Training a machine learning model for candidate suitability prediction  
- Performing real-time analysis of new candidate data  

---

## 2. Project Motivation
Manual resume screening is time-consuming and prone to human bias. This system helps by:  
- Reducing manual effort for HR teams  
- Providing standardized candidate evaluation  
- Ensuring faster and fairer recruitment decisions  

---

## 3. Dataset Used
The project uses the **Resume Dataset from Kaggle**, which contains structured and unstructured data extracted from real candidate resumes.  

- Source: [Kaggle Resume Dataset](https://www.kaggle.com/datasets)  
- Dataset includes candidate information such as skills, education, experience, applied roles, and job requirements.  
- This dataset serves as input for training the machine learning model to predict candidate suitability.  

---

## 4. Model Used
The project uses a **Passive Aggressive Classifier** from `scikit-learn` to predict candidate suitability.  

### Workflow:
1. Preprocess resumes by cleaning and tokenizing the text  
2. Convert textual data into numerical features using `TfidfVectorizer`  
3. Train the Passive Aggressive Classifier on the cleaned dataset  
4. Save the trained model for real-time predictions  

---

## 5. Project Structure
AI-Recruitment-System/
│
├── app.py # Main application script
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore # Git ignored files
├── model/ # Trained ML model (.pkl)
├── data/ # Original Kaggle Resume Dataset
├── cleaned_data/ # Preprocessed resumes for ML
└── outputs/ # Predicted outputs for new candidates
## 6. How the Project Works

### Local Execution:
1. Load the original Kaggle Resume Dataset  
2. Preprocess resumes into cleaned text suitable for ML  
3. Train the Passive Aggressive Classifier on the cleaned data  
4. Save the trained model for later use  
5. Input new candidate data via the application  
6. Predict candidate suitability and display results  

---

## 7. How to Run Locally

### A. Clone the Repository
```bash
git clone https://github.com/khushi7387/AI-Recruitment-System.git
cd AI-Recruitment-System

B. Setup Virtual Environment
python -m venv venv
# Activate virtual environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

C. Install Dependencies
pip install -r requirements.txt

D. Run the Application
python app.py

Open the browser at the provided URL (e.g., http://127.0.0.1:5000)
Input candidate data to perform real-time analysis

8. Real-Time Candidate Analysis
To perform real-time analysis for a new candidate:
Input candidate resume or structured data into the application
The system preprocesses the text and converts it to model-compatible features
The trained model predicts candidate suitability
The app displays results including candidate information and suitability insights

9. Future Improvements
Use larger and more diverse datasets for improved model accuracy
Compare multiple machine learning models to enhance predictions
Integrate a web-based user interface for easier resume uploads
Provide skill recommendations to help candidates improve suitability

10. References
Kaggle Resume Dataset: https://www.kaggle.com/datasets
Python scikit-learn documentation
GitHub tutorials for version control