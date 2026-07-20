import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Visualizations",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Exploratory Data Analysis (EDA)")

st.markdown("""
This page provides graphical analysis of the student performance dataset.
The visualizations help understand the relationship between academic and
lifestyle factors affecting final grades.
""")

# Load Dataset

df = pd.read_csv("dataset/student_performance_prediction_dataset.csv")

# Final Grade Distribution

st.subheader("📈 Final Grade Distribution")

fig, ax = plt.subplots(figsize=(8,4))

sns.histplot(df["final_grade"], bins=30, kde=True, ax=ax)

ax.set_xlabel("Final Grade")
ax.set_ylabel("Frequency")

st.pyplot(fig)

st.divider()
# Attendance Distribution
st.subheader("📉 Attendance Distribution")

fig, ax = plt.subplots(figsize=(8,4))

sns.histplot(df["attendance"], bins=30, kde=True, color="green", ax=ax)

st.pyplot(fig)

st.divider()

# Study Hours Distribution

st.subheader("📚 Study Hours Distribution")

fig, ax = plt.subplots(figsize=(8,4))

sns.histplot(df["study_hours"], bins=20, kde=True, color="orange", ax=ax)

st.pyplot(fig)

st.divider()

# Gender Distribution
st.subheader("👨‍🎓 Gender Distribution")

fig, ax = plt.subplots(figsize=(6,4))

sns.countplot(x="gender", data=df, palette="Set2", ax=ax)

st.pyplot(fig)

st.divider()

# Scatter Plot
st.subheader("📌 Study Hours vs Final Grade")

fig, ax = plt.subplots(figsize=(8,5))

sns.scatterplot(
    x="study_hours",
    y="final_grade",
    data=df,
    ax=ax
)

st.pyplot(fig)

st.divider()

# Attendance vs Final Grade
st.subheader("📌 Attendance vs Final Grade")

fig, ax = plt.subplots(figsize=(8,5))

sns.scatterplot(
    x="attendance",
    y="final_grade",
    data=df,
    ax=ax
)

st.pyplot(fig)

st.divider()
# Heatmap
st.subheader("🔥 Correlation Heatmap")

fig, ax = plt.subplots(figsize=(14,8))

sns.heatmap(
    df.corr(numeric_only=True),
    cmap="coolwarm",
    annot=False,
    ax=ax
)

st.pyplot(fig)

st.divider()
# Correlation Table
st.subheader("📊 Correlation with Final Grade")

corr = df.corr(numeric_only=True)

correlation = corr["final_grade"].sort_values(ascending=False)

st.dataframe(correlation)

st.divider()
# Box Plot

st.subheader("📦 Study Hours Box Plot")

fig, ax = plt.subplots(figsize=(8,4))

sns.boxplot(x=df["study_hours"], ax=ax)

st.pyplot(fig)

st.divider()

# Key Insights

st.subheader("💡 Key Insights")

st.success("""
✅ Students with higher attendance generally perform better.

✅ Previous academic performance has a strong impact on final grades.

✅ Regular study hours are associated with improved performance.

✅ Assignments and practice tests contribute positively to academic results.

✅ Time management and motivation also influence student performance.
""")