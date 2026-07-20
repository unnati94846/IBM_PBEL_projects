import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About the Project")

st.markdown("""
This project uses **Machine Learning** to predict a student's final academic performance
based on academic records, study habits, attendance, and lifestyle factors.
""")

st.divider()

# ==========================================================
# Project
# ==========================================================

st.header("🎓 Project")

st.info("""
**AI-Driven Student Performance Prediction System using Machine Learning**

The system predicts a student's final academic grade using Machine Learning
algorithms and provides personalized recommendations to improve performance.
""")

st.divider()

# ==========================================================
# Problem Statement
# ==========================================================

st.header("📌 Problem Statement")

st.write("""
Educational institutions often identify weak-performing students only after
their final examinations. This project aims to predict student performance
at an early stage so that timely guidance and academic support can be provided.
""")

st.divider()

# ==========================================================
# Objectives
# ==========================================================

st.header("🎯 Objectives")

st.markdown("""
- Predict students' final academic performance.
- Analyze the impact of attendance and study habits.
- Compare different Machine Learning algorithms.
- Build an interactive web application.
- Provide personalized suggestions to improve performance.
""")

st.divider()

# ==========================================================
# Algorithms
# ==========================================================

st.header("🤖 Algorithms Used")

st.markdown("""
✅ Linear Regression *(Final Model)*

✅ Decision Tree Regression

✅ Random Forest Regression
""")

st.divider()

# ==========================================================
# Dataset
# ==========================================================

st.header("📂 Dataset")

st.write("""
The dataset contains academic, personal and lifestyle attributes of students.

Main Features:

• Age

• Gender

• Attendance

• Study Hours

• Previous Grade

• Assignments Completed

• Practice Tests

• Motivation Level

• Mental Health Score

• Screen Time

• Parent Education

• Internet Access

Target Variable:

🎯 Final Grade
""")

st.divider()

# ==========================================================
# Technologies
# ==========================================================

st.header("🛠 Technologies Used")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
🐍 Python

🐼 Pandas

🔢 NumPy
""")

with col2:
    st.success("""
📈 Matplotlib

🎨 Seaborn

🤖 Scikit-Learn
""")

with col3:
    st.success("""
🎈 Streamlit

💾 Joblib

💻 VS Code
""")

st.divider()

# ==========================================================
# Future Scope
# ==========================================================

st.header("🚀 Future Scope")

st.markdown("""
- Integration with college ERP systems.
- Real-time student performance monitoring.
- AI chatbot for academic guidance.
- Mobile application support.
- Deep Learning based prediction models.
- Personalized learning recommendations.
""")

st.divider()

# ==========================================================
# Team
# ==========================================================

st.header("👩‍💻 Team Members")

st.write("""
**Unnati Yadav**

B.Tech (Information Technology)

IBM PBEL Machine Learning Project
""")

st.divider()

# ==========================================================
# Guide
# ==========================================================

st.header("👨‍🏫 Project Guide")

guide_name = st.text_input(
    "Guide Name",
    placeholder="Enter Guide Name"
)

if guide_name:
    st.success(f"Project Guide : {guide_name}")

st.divider()

# ==========================================================
# Results
# ==========================================================

st.header("📈 Project Outcome")

st.success("""
✔ Student Performance Prediction

✔ Performance Analysis

✔ AI-Based Suggestions

✔ Risk Level Detection

✔ Interactive Dashboard

✔ Professional Streamlit Application
""")

st.divider()

# ==========================================================
# Footer
# ==========================================================

st.markdown(
    """
---
### ❤️ Thank You

**AI-Driven Student Performance Prediction System**

Developed using Python, Machine Learning and Streamlit.
"""
)