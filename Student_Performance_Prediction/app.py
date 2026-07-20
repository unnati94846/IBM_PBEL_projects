import streamlit as st

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI-Driven Student Performance Prediction")

st.success("Welcome to the Student Performance Prediction System.")

st.write("### Navigate through the project")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.page_link(
        "pages/Home.py",
        label="Home",
        icon="🏠"
    )

    st.page_link(
        "pages/Dataset.py",
        label="Dataset",
        icon="📂"
    )

    st.page_link(
        "pages/Visualizations.py",
        label="Visualizations",
        icon="📊"
    )

with col2:

    st.page_link(
        "pages/Prediction.py",
        label="Prediction",
        icon="🤖"
    )

    st.page_link(
        "pages/Model_Evaluation.py",
        label=" Model Evaluation",
        icon="📈"
    )

    st.page_link(
        "pages/AI_Suggestions.py",
        label=" AI Suggestions",
        icon="💡"
    )

st.page_link(
    "pages/About.py",
    label="ℹAbout",
    icon="ℹ️"
)

st.markdown("---")

st.info("""
Click any button above or use the sidebar to navigate between pages.
""")