import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dataset",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Student Dataset")

st.markdown("### Dataset Overview")
# Load Dataset

df = pd.read_csv("dataset/student_performance_prediction_dataset.csv")

# Dataset Information
rows = df.shape[0]
cols = df.shape[1]
missing = df.isnull().sum().sum()
duplicate = df.duplicated().sum()

target = "final_grade"
# Top Cards

col1, col2 = st.columns(2)

with col1:

    st.info(f"""
### 📊 Dataset Shape

**Rows :** {rows:,}

**Columns :** {cols}
""")

with col2:

    st.success(f"""
### 📌 Dataset Information

**Missing Values :** {missing}

**Duplicate Values :** {duplicate}

**Target Variable :** {target}
""")

st.markdown("---")
# Dataset Preview
st.subheader("📄 Top 20 Records")

st.dataframe(
    df.head(20),
    use_container_width=True,
    height=500
)

st.markdown("---")
# Column Names
st.subheader("📑 Column Names")

st.write(list(df.columns))

st.markdown("---")

# Data Types
st.subheader("📋 Data Types")

st.dataframe(
    pd.DataFrame(df.dtypes, columns=["Data Type"]),
    use_container_width=True
)

st.markdown("---")

# Summary Statistics
st.subheader("📈 Summary Statistics")
st.dataframe(
    df.describe(),
    use_container_width=True
)
st.markdown("---")

# Footer
st.caption("IBM PBEL Project | Student Performance Prediction")