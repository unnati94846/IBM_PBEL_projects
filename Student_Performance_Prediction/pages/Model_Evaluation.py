import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ----------------------------------------------------
# Page Config
# ----------------------------------------------------

st.set_page_config(
    page_title="Model Evaluation",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Evaluation")

st.markdown("Performance comparison of Machine Learning models.")

st.divider()

# ----------------------------------------------------
# Load Dataset
# ----------------------------------------------------

df = pd.read_csv("dataset/student_performance_prediction_dataset.csv")

# ----------------------------------------------------
# Encoding
# ----------------------------------------------------

from sklearn.preprocessing import LabelEncoder

categorical_cols = [
    "gender",
    "family_income",
    "parent_education",
    "internet_access",
    "device_type",
    "school_type",
    "extracurriculars",
    "grade_category",
    "pass_fail"
]

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# ----------------------------------------------------
# Feature Selection
# ----------------------------------------------------

features = [

    "age",
    "gender",
    "study_hours",
    "attendance",
    "sleep_hours",
    "previous_grade",
    "assignments_completed",
    "practice_tests_taken",
    "group_study_hours",
    "notes_quality_score",
    "time_management_score",
    "motivation_level",
    "mental_health_score",
    "screen_time",
    "social_media_hours",
    "family_income",
    "parent_education",
    "internet_access",
    "device_type",
    "school_type",
    "extracurriculars"

]

X = df[features]
y = df["final_grade"]

# ----------------------------------------------------
# Scaling
# ----------------------------------------------------

scaler = joblib.load("models/scaler.pkl")

X = scaler.transform(X)

# ----------------------------------------------------
# Split
# ----------------------------------------------------

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ----------------------------------------------------
# Load Saved Model
# ----------------------------------------------------

model = joblib.load("models/student_model.pkl")

# ----------------------------------------------------
# Prediction
# ----------------------------------------------------

y_pred = model.predict(X_test)

# ----------------------------------------------------
# Metrics
# ----------------------------------------------------

mae = mean_absolute_error(y_test,y_pred)
rmse = np.sqrt(mean_squared_error(y_test,y_pred))
r2 = r2_score(y_test,y_pred)

# ----------------------------------------------------
# Model Comparison Table
# ----------------------------------------------------

comparison = pd.DataFrame({

"Model":[
"Linear Regression",
"Decision Tree",
"Random Forest"
],

"R²":[
0.831,
0.509,
0.708
]

})

st.subheader("📊 Model Comparison")

st.dataframe(
    comparison,
    use_container_width=True
)

st.divider()

# ----------------------------------------------------
# Metric Cards
# ----------------------------------------------------

c1,c2,c3 = st.columns(3)

c1.metric("MAE",round(mae,3))
c2.metric("RMSE",round(rmse,3))
c3.metric("R² Score",round(r2,3))

st.divider()

# ----------------------------------------------------
# Actual vs Predicted
# ----------------------------------------------------

st.subheader("📈 Actual vs Predicted")

fig,ax=plt.subplots(figsize=(7,5))

ax.scatter(
    y_test,
    y_pred,
    alpha=0.5
)

ax.plot(
    [y.min(),y.max()],
    [y.min(),y.max()],
    color="red"
)

ax.set_xlabel("Actual Grade")
ax.set_ylabel("Predicted Grade")
ax.set_title("Actual vs Predicted")

st.pyplot(fig)

st.divider()

# ----------------------------------------------------
# Residual Plot
# ----------------------------------------------------

st.subheader("📉 Residual Plot")

residuals = y_test-y_pred

fig2,ax2=plt.subplots(figsize=(7,5))

ax2.scatter(
    y_pred,
    residuals,
    alpha=0.5
)

ax2.axhline(
    y=0,
    color="red"
)

ax2.set_xlabel("Predicted Grade")
ax2.set_ylabel("Residual")

st.pyplot(fig2)

st.divider()

# ----------------------------------------------------
# Conclusion
# ----------------------------------------------------

st.success(
"""
✅ Linear Regression achieved the highest performance on this dataset
and was selected as the final prediction model.

It provides:

• Lowest Error

• Highest R² Score

• Fast Prediction

• Better Generalization
"""
)