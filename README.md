<div align="center">

# 🎓 Student Exam Pass Predictor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/ML-ScikitLearn-F7931E?logo=scikitlearn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

### 🧠 Predict if a student will pass or fail based on study habits and performance metrics

[Demo](#-screenshots) • [Features](#-features) • [Installation](#-installation--setup) • [Usage](#-usage)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Dataset](#-dataset)
- [Model Performance](#-model-performance)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Overview

The **Student Exam Pass Predictor** is an intelligent web-based machine learning application built with **Streamlit**. It leverages a **Logistic Regression model** to estimate the probability of a student **passing or failing** an exam based on key academic indicators.

### 🎯 Prediction Factors

- ⏰ **Study Hours (0-24)** - Daily study time investment
- 📅 **Attendance (0-100%)** - Class attendance percentage
- 📊 **Previous Score (0-100)** - Historical academic performance

The model analyzes these three key metrics and provides an instant prediction with a confidence score to help identify at-risk students early.

---

## ✨ Features

✅ **Real-time Predictions** - Instant pass/fail likelihood assessment  
✅ **Interactive UI** - User-friendly Streamlit interface with emojis  
✅ **Probability Score** - Confidence percentage for predictions  
✅ **Visual Feedback** - Color-coded results (Green for Pass, Red for Fail)  
✅ **Input Validation** - Range checking and numeric validation  
✅ **Model Persistence** - Pre-trained model for quick predictions  
✅ **Easy Deployment** - Simple setup and execution  
✅ **Lightweight Dataset** - 61 student records for training

---

## 📸 Screenshots

### 🏠 Home Interface
![Home Interface](screenshots/home_interface.png)
*Main prediction interface with input fields for study hours, attendance, and previous score*

### ✅ Pass Prediction
![Pass Prediction](screenshots/pass_prediction.png)
*Example of a successful pass prediction with high confidence score*

### ❌ Fail Prediction
![Fail Prediction](screenshots/fail_prediction.png)
*Example of a fail prediction with confidence percentage*

### 📊 Model Training Output
![Model Training](screenshots/model_training.png)
*Training completion message showing model saved successfully*

> **Note:** Create a `screenshots/` folder in your project root and add your application screenshots with the names shown above.

---

## 🗂️ Project Structure

```bash
ML_Project_RollNo_43_44_45_/
│
├── 📄 app.py                   # Streamlit web application
├── 🔧 train_model.py           # Model training and saving script
├── 📦 model/
│   └── model.pkl               # Trained Logistic Regression model
├── 📊 data/
│   └── student_data.csv        # Training dataset (61 records)
├── 🖼️ screenshots/              # Application screenshots (optional)
│   ├── home_interface.png
│   ├── pass_prediction.png
│   ├── fail_prediction.png
│   └── model_training.png
├── 📋 requirements.txt         # Python dependencies
└── 📖 README.md                # Project documentation
```

---

## 🔍 How It Works

### 🔹 Training Phase (`train_model.py`)

1. **Data Loading** 
   - Reads `student_data.csv` containing 61 student records
   - Features: `study_hours`, `attendance`, `previous_score`
   - Target: `pass_exam` (0 = Fail, 1 = Pass)

2. **Data Preprocessing**
   - Removes any null/missing values using `dropna()`
   - Splits data into features (X) and target (y)

3. **Train-Test Split**
   - 80% training data, 20% testing data
   - Random state = 42 for reproducibility

4. **Model Training**
   - Trains a Logistic Regression classifier
   - Fits the model on training data

5. **Model Saving**
   - Serializes model using pickle
   - Saves to `model/model.pkl` for deployment

### 🔹 Prediction Phase (`app.py`)

1. **Model Loading**
   - Loads pre-trained model from `model/model.pkl`

2. **User Input Collection**
   - Study Hours: Text input (0-24 hours)
   - Attendance: Text input (0-100%)
   - Previous Score: Text input (0-100)

3. **Input Validation**
   - Checks if values are numeric
   - Validates ranges for each input
   - Displays warnings for invalid inputs

4. **Prediction Generation**
   - Creates input array from user data
   - Uses `model.predict()` for classification
   - Uses `model.predict_proba()` for confidence score

5. **Result Display**
   - ✅ Green success box for "Likely to Pass"
   - ❌ Red error box for "Likely to Fail"
   - Shows confidence percentage

---

## 🧠 Tech Stack

| Technology | Purpose | Usage |
|------------|---------|-------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | Core Programming | Main language |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) | Web Framework | UI development |
| ![scikit-learn](https://img.shields.io/badge/ScikitLearn-F7931E?logo=scikitlearn&logoColor=white) | ML Library | Logistic Regression |
| ![pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white) | Data Processing | CSV handling |
| ![Pickle](https://img.shields.io/badge/Pickle-3776AB?logo=python&logoColor=white) | Serialization | Model persistence |

---

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for cloning the repository)

### Step-by-Step Installation

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/bhusareMayur/ML_Project_RollNo_43_44_45_.git
cd ML_Project_RollNo_43_44_45_
```

#### 2️⃣ Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**Or install manually:**
```bash
pip install streamlit pandas scikit-learn
```

#### 4️⃣ Create Required Directories

```bash
# Create model directory if it doesn't exist
mkdir model
```

#### 5️⃣ Train the Model

```bash
python train_model.py
```

**Expected Output:**
```
Model saved as model/model.pkl
```

#### 6️⃣ Run the Web Application

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

## 💻 Usage

### Running Predictions

1. **Launch the Application**
   ```bash
   streamlit run app.py
   ```

2. **Enter Student Information**
   - **Study Hours**: Enter value between 0-24 hours
   - **Attendance**: Enter percentage between 0-100%
   - **Previous Score**: Enter score between 0-100

3. **Get Prediction**
   - Click the **"🎯 Predict"** button
   - View the pass/fail prediction
   - Check the confidence score

### Example Test Cases

#### ✅ Pass Scenarios

| Study Hours | Attendance (%) | Previous Score | Prediction | Confidence |
|:-----------:|:--------------:|:--------------:|:----------:|:----------:|
| 8 | 85 | 75 | ✅ **Likely to Pass** | ~85-90% |
| 10 | 95 | 90 | ✅ **Likely to Pass** | ~95%+ |
| 6 | 75 | 65 | ✅ **Likely to Pass** | ~70-80% |
| 5 | 70 | 60 | ✅ **Likely to Pass** | ~65-75% |

#### ❌ Fail Scenarios

| Study Hours | Attendance (%) | Previous Score | Prediction | Confidence |
|:-----------:|:--------------:|:--------------:|:----------:|:----------:|
| 1 | 50 | 30 | ❌ **Likely to Fail** | ~80-90% |
| 2 | 55 | 40 | ❌ **Likely to Fail** | ~75-85% |
| 3 | 60 | 50 | ❌ **Likely to Fail** | ~60-70% |
| 0 | 0 | 0 | ❌ **Likely to Fail** | ~95%+ |

#### ⚠️ Edge Cases

| Study Hours | Attendance (%) | Previous Score | Prediction | Notes |
|:-----------:|:--------------:|:--------------:|:----------:|:------|
| 0 | 95 | 80 | ✅ **Pass** | High attendance compensates |
| 10 | 10 | 10 | ❌ **Fail** | Low attendance hurts |
| 5 | 50 | 50 | 🟡 **Borderline** | Close to decision boundary |

---

## 📊 Dataset

### Dataset Overview

- **File**: `data/student_data.csv`
- **Records**: 61 students
- **Features**: 3 (study_hours, attendance, previous_score)
- **Target**: 1 (pass_exam: 0 or 1)

### Data Structure

```csv
study_hours,attendance,previous_score,pass_exam
1,50,30,0
2,55,40,0
5,70,60,1
8,85,75,1
10,95,90,1
```

### Column Descriptions

| Column | Type | Description | Range | Target |
|--------|------|-------------|-------|--------|
| `study_hours` | Integer | Daily study hours | 0-24 | Feature |
| `attendance` | Integer | Class attendance percentage | 0-100 | Feature |
| `previous_score` | Integer | Previous exam score | 0-100 | Feature |
| `pass_exam` | Binary | Pass (1) or Fail (0) | 0, 1 | Label |

### Dataset Characteristics

- **Balanced Classes**: Mix of pass (1) and fail (0) cases
- **Real-world Scenarios**: Includes edge cases like:
  - High study hours with low attendance
  - Low study hours with high attendance
  - Various score combinations
- **Clean Data**: No missing values after `dropna()`

---

## 📈 Model Performance

### Algorithm Details

- **Model**: Logistic Regression
- **Library**: scikit-learn
- **Training Split**: 80-20 (train-test)
- **Random State**: 42

### Key Features

✅ **Fast Training** - Trains in seconds  
✅ **Interpretable** - Clear decision boundaries  
✅ **Probabilistic** - Provides confidence scores  
✅ **Binary Classification** - Pass/Fail prediction  
✅ **Low Overfitting Risk** - Simple linear model  

### Model Capabilities

- Handles 3 input features simultaneously
- Provides probability estimates (0-100%)
- Works well with small datasets
- No hyperparameter tuning required for basic use

### Prediction Logic

The model learns patterns like:
- **High study hours + High attendance + High scores → Pass**
- **Low study hours + Low attendance + Low scores → Fail**
- Weighs each feature's importance automatically

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** your changes
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push** to the branch
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open** a Pull Request

### Ideas for Enhancement

- 🎨 **UI Improvements**: Add charts, graphs, or animations
- 📊 **Data Visualization**: Display feature importance
- 🤖 **Advanced Models**: Try Random Forest, SVM, or Neural Networks
- 📈 **Model Metrics**: Add accuracy, precision, recall display
- 💾 **Database Integration**: Store predictions history
- 📱 **Responsive Design**: Mobile-friendly interface
- 🌐 **Deployment**: Deploy on Streamlit Cloud or Heroku
- 📝 **Logging**: Add prediction history tracking
- 🔔 **Alerts**: Email notifications for at-risk students
- 📚 **Documentation**: API documentation, video tutorials

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👥 Team Members

**Roll Numbers:** 43, 44, 45

### Project Lead
- [@bhusareMayur](https://github.com/bhusareMayur) - GitHub Repository Owner

### Development Team
- **Roll No. 43** - Model Development & Training
- **Roll No. 44** - Web Application & UI Design
- **Roll No. 45** - Data Collection & Documentation

---

## 🎯 Project Goals

- ✅ Build a functional ML prediction system
- ✅ Create an intuitive web interface
- ✅ Apply machine learning concepts in education
- ✅ Help identify at-risk students early
- ✅ Demonstrate practical ML application

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) - Amazing web framework
- Powered by [scikit-learn](https://scikit-learn.org/) - ML library
- Inspired by educational data science projects
- Thanks to our instructors for guidance

---

## 📞 Contact

For questions, suggestions, or collaboration:

- **GitHub Issues**: [Report bugs or request features](https://github.com/bhusareMayur/ML_Project_RollNo_43_44_45_/issues)
- **GitHub**: [@bhusareMayur](https://github.com/bhusareMayur)

---

## 📝 Requirements File

Create a `requirements.txt` file with:

```txt
streamlit>=1.28.0
pandas>=2.0.0
scikit-learn>=1.3.0
```

---

<div align="center">

### ⭐ If you found this project helpful, please give it a star!

### 🎓 Built for Educational Purposes

Made with ❤️ by ML Project Team (Roll No. 43, 44, 45)

[⬆ Back to Top](#-student-exam-pass-predictor)

</div>
