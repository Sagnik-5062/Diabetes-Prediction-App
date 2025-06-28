# 🩺 Diabetes Prediction App
# App Link: https://diabetes-prediction-app-modzstu7apbqj4ytancq3m.streamlit.app/
👨‍💻 Developed by
Sagnik Das<br>
Jhinuk Guha<br><hr>
A simple machine learning web application built with Python and Streamlit to predict whether a person is likely to have diabetes based on medical input parameters.  
It uses the Pima Indians Diabetes Dataset and models like Logistic Regression or SVM.

---

## 📌 Features

- Predicts diabetes based on user input (like Glucose level, BMI, Age, etc.)
- Clean and interactive UI with Streamlit
- Trained using supervised learning models (e.g., Logistic Regression / SVM)
- Accurate and fast predictions
- Lightweight and easy to deploy

---

## 📊 Dataset

- **Name:** Pima Indians Diabetes Dataset
- **Source:** UCI Machine Learning Repository / Kaggle
- **Attributes:**  
  - Pregnancies  
  - Glucose  
  - Blood Pressure  
  - Skin Thickness  
  - Insulin  
  - BMI  
  - Diabetes Pedigree Function  
  - Age  
  - Outcome (0 = Non-diabetic, 1 = Diabetic)

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Sagnik-5062/Diabetes-Prediction-App.git
cd Diabetes-Prediction-App

2. Install Dependencies
bash
Copy code
pip install -r requirements.txt

3. Run the App
bash
Copy code
streamlit run app.py

🧠 Model Info
You can modify or retrain the model using model.py or directly load a pre-trained model using joblib.

📁 Project Structure
text
Copy code
Diabetes-Prediction-App/
├── app.py                 # Streamlit frontend
├── model.py               # Model training script
├── diabetes.csv           # Dataset file
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
