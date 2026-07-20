import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="AI Suggestions",
    page_icon="💡",
    layout="wide"
)

st.title("💡 AI Performance Advisor")

st.write("Get personalized suggestions based on your academic profile.")

st.divider()

# ==========================
# Input
# ==========================

col1, col2 = st.columns(2)

with col1:

    predicted_grade = st.number_input(
        "Predicted Grade",
        0.0,
        100.0,
        72.0
    )

    study_hours = st.slider(
        "Study Hours",
        0.0,
        12.0,
        4.0
    )

    attendance = st.slider(
        "Attendance (%)",
        0,
        100,
        80
    )

    practice_tests = st.slider(
        "Practice Tests Taken",
        0,
        10,
        3
    )

with col2:

    notes_quality = st.slider(
        "Notes Quality",
        1,
        10,
        5
    )

    screen_time = st.slider(
        "Screen Time (Hours)",
        0.0,
        12.0,
        6.0
    )

    sleep_hours = st.slider(
        "Sleep Hours",
        3.0,
        10.0,
        6.0
    )

st.divider()

# ==========================
# Result
# ==========================

if st.button("💡 Generate Suggestions"):

    st.subheader("🎯 Predicted Grade")

    st.metric(
        "Final Grade",
        round(predicted_grade,2)
    )

    st.divider()

    st.subheader("📋 Personalized Suggestions")

    suggestions=[]

    if study_hours<5:
        suggestions.append("📚 Increase study hours to 5–6 hours/day.")

    if attendance<90:
        suggestions.append("🏫 Maintain attendance above 90%.")

    if practice_tests<5:
        suggestions.append("📝 Practice more mock tests.")

    if notes_quality<7:
        suggestions.append("📖 Improve notes quality.")

    if screen_time>5:
        suggestions.append("📱 Reduce screen time.")

    if sleep_hours<7:
        suggestions.append("😴 Maintain a healthy sleep schedule.")

    if len(suggestions)==0:
        suggestions.append("🎉 Excellent! Keep following the same routine.")

    for s in suggestions:
        st.write("✅",s)

    st.divider()

    # ==========================
    # Risk Level
    # ==========================

    risk=0

    if attendance<75:
        risk+=1

    if study_hours<4:
        risk+=1

    if practice_tests<3:
        risk+=1

    if screen_time>6:
        risk+=1

    if sleep_hours<6:
        risk+=1

    if predicted_grade<60:
        risk+=2

    st.subheader("⚠️ Academic Risk Level")

    if risk<=1:

        st.success("🟢 LOW RISK")

    elif risk<=3:

        st.warning("🟡 MEDIUM RISK")

    else:

        st.error("🔴 HIGH RISK")

    st.divider()

    st.subheader("📌 Overall Recommendation")

    if predicted_grade>=90:

        st.success("""
Excellent performance.

Continue maintaining consistency.
Keep solving advanced practice papers.
Maintain healthy habits.
""")

    elif predicted_grade>=75:

        st.info("""
Good performance.

Increase practice tests.
Improve attendance.
Focus on revision.
""")

    elif predicted_grade>=60:

        st.warning("""
Average performance.

Increase study hours.
Improve notes.
Revise daily.
Reduce distractions.
""")

    else:

        st.error("""
Needs Improvement.

Increase study hours.
Take more practice tests.
Improve attendance.
Reduce social media.
Sleep properly.
Seek guidance from teachers.
""")