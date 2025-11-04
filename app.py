import streamlit as st
import pandas as pd
import pickle

# Load the saved model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="Student Exam Predictor", layout="centered")
st.title("🎓 Student Exam Pass Prediction")
st.write("Enter the student's data below to predict if they will **pass** or **fail** the exam.")

study_hours = st.text_input("📚 Study Hours (0–24)")
attendance = st.text_input("📅 Attendance (%) (0–100)")
prev_score = st.text_input("📊 Previous Score (0–100)")

if st.button("🎯 Predict"):
    try:
        hours = float(study_hours)
        attend = float(attendance)
        score = float(prev_score)

        if not (0 <= hours <= 24 and 0 <= attend <= 100 and 0 <= score <= 100):
            st.warning("⚠️ Please enter values within valid range.")
        else:
            input_data = [[hours, attend, score]]
            prediction = model.predict(input_data)
            prob = model.predict_proba(input_data)[0][1] * 100

            if prediction[0] == 1:
                st.success(f"✅ Likely to Pass (Confidence: {prob:.2f}%)")
            else:
                st.error(f"❌ Likely to Fail (Confidence: {100 - prob:.2f}%)")

    except ValueError:
        st.warning("⚠️ Please enter **numeric values only**.")
