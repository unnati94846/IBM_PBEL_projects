import streamlit as st

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

# ==========================
# HERO SECTION
# ==========================

st.title("🎓 AI-Driven Student Performance Prediction System")

st.markdown("""
### Predict Student Academic Performance using Machine Learning & Artificial Intelligence

This project predicts a student's final academic performance based on
their academic records, attendance, study habits, lifestyle, and other
important factors using Machine Learning algorithms.

The system also provides performance analysis and personalized
recommendations for improving academic results.
""")

st.markdown("---")

# ==========================
# BANNER
# ==========================

st.image(
    "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=1400",
    use_container_width=True
)

st.markdown("---")

# ==========================
# BUTTONS
# ==========================

col1, col2 = st.columns(2)

with col1:
    st.page_link(
        "pages/Prediction.py",
        label="🚀 Start Prediction",
        icon="🚀"
    )

with col2:
    st.page_link(
        "pages/Dataset.py",
        label="📊 View Dataset",
        icon="📊"
    )

st.markdown("---")

# ==========================
# INFORMATION CARDS
# ==========================

col1, col2 = st.columns(2)

with col1:

    st.info("""
### 📁 Dataset Size

- 👨‍🎓 Records : **1,000,000**
- 📊 Features : **25**
- 🎯 Target : **Final Grade**
""")

with col2:

    st.success("""
### 🤖 ML Models Used

✅ Linear Regression

✅ Decision Tree

✅ Random Forest
""")

col3, col4 = st.columns(2)

with col3:

    st.warning("""
### 📈 Model Accuracy

**R² Score**

🏆 Linear Regression

**83%**
""")

with col4:

    st.error("""
### 🎯 Target Variable

**Final Grade**

The model predicts the student's final academic score.
""")

st.markdown("---")

# ==========================
# PROJECT FEATURES
# ==========================

st.subheader("✨ Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
✅ Predict Student Score

✅ Fast Prediction

✅ Accurate Results
""")

with col2:
    st.info("""
📊 Interactive Dashboard

📈 Data Visualization

📉 Performance Analysis
""")

with col3:
    st.warning("""
💡 AI Suggestions

🎯 Performance Category

📚 Personalized Recommendations
""")

st.markdown("---")

# ==========================
# WORKFLOW
# ==========================

st.subheader("⚙️ Project Workflow")

st.markdown("""
1️⃣ Student enters academic details.

⬇️

2️⃣ Data is preprocessed.

⬇️

3️⃣ Machine Learning model predicts the score.

⬇️

4️⃣ Performance category is generated.

⬇️

5️⃣ Personalized study recommendations are displayed.
""")

st.markdown("---")

# ==========================
# TECHNOLOGIES
# ==========================

st.subheader("🛠 Technologies Used")

tech1, tech2, tech3, tech4, tech5 = st.columns(5)

with tech1:
    st.metric("🐍 Python", "✓")

with tech2:
    st.metric("🐼 Pandas", "✓")

with tech3:
    st.metric("🤖 Scikit-Learn", "✓")

with tech4:
    st.metric("📊 Plotly", "✓")

with tech5:
    st.metric("🎈 Streamlit", "✓")

st.markdown("---")

# ==========================
# FOOTER
# ==========================

st.caption(
    "Developed as an IBM PBEL Machine Learning Project | Student Performance Prediction using AI"
)