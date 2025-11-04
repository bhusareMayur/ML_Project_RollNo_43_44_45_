<div align="center">

# 🎓 Student Exam Pass Predictor  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![scikit-learn](https://img.shields.io/badge/ML-ScikitLearn-orange?logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green)

### 🧠 Predict if a student will pass or fail based on study habits and performance metrics.

</div>

---

## 🚀 Overview  

The **Student Exam Pass Predictor** is a web-based machine learning app built with **Streamlit**.  
It uses a **Logistic Regression model** to estimate the probability of a student **passing or failing** an exam.  

The prediction is based on:
- ⏰ **Study Hours**
- 📅 **Attendance (%)**
- 📊 **Previous Scores**

---

## 🧩 Project Structure  

student-exam-pass-prediction/
│
├── app.py # Streamlit web application
├── train_model.py # Script for model training and saving
├── model/
│ └── model.pkl # Trained logistic regression model
├── data/
│ └── student_data.csv # Dataset for model training
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚙️ How It Works  

### 🔹 `train_model.py`
- Loads and preprocesses the dataset from `data/student_data.csv`
- Trains a **Logistic Regression** model using scikit-learn
- Saves the model as `model/model.pkl`

### 🔹 `app.py`
- Loads the saved model
- Takes user inputs:
  - Study Hours  
  - Attendance %  
  - Previous Score  
- Outputs **Pass/Fail** prediction with confidence score

---

## 🧠 Tech Stack  

| Tool            | Purpose                 |
|-----------------|-------------------------|
| **Python**      | Programming language    |
| **Streamlit**   | Interactive web app     |
| **scikit-learn**| Machine Learning model  |
| **pandas**      | Data manipulation       |
| **pickle**      | Model serialization     |

---

## 🛠️ Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/bhusareMayur/ML_Project_RollNo_43_44_45_.git
cd ML_Project_RollNo_43_44_45_
```
###2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
###3️⃣ Train the Model (Optional)
```bash
python train_model.py
```
###4️⃣ Run the Web App
```bash
streamlit run app.py
```
Then open the local URL shown (e.g., http://localhost:8501) in your browser.

##💡 Example Input
<pre> | Study Hours | Attendance (%) | Previous Score | Prediction | | ------------ | -------------- | -------------- | ---------------- | | 6 | 85 | 70 | ✅ Likely to Pass | | 2 | 45 | 40 | ❌ Likely to Fail | </pre>

