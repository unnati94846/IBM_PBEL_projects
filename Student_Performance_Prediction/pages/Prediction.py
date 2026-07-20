import streamlit as st
# PAGE CONFIG (Always first Streamlit command)

st.set_page_config(
    page_title="AI Student Performance Advisor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)
# IMPORT LIBRARIES

import pandas as pd
import numpy as np
import joblib

import plotly.graph_objects as go
# LOAD MODEL

model = joblib.load("models/student_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# LOAD LABEL ENCODERS

le_gender = joblib.load("models/le_gender.pkl")
le_parent = joblib.load("models/le_parent.pkl")
le_income = joblib.load("models/le_income.pkl")
le_device = joblib.load("models/le_device.pkl")
le_school = joblib.load("models/le_school.pkl")
le_extra = joblib.load("models/le_extra.pkl")

# CSS

st.markdown("""
<style>

/* ===============================
BACKGROUND
=============================== */

.stApp{

background:
linear-gradient(
135deg,
#0F172A,
#111827,
#020617
);

color:white;

}

/* ===============================
SIDEBAR
=============================== */

section[data-testid="stSidebar"]{

background:#0B1120;

border-right:1px solid #1E293B;

}

/* ===============================
HEADINGS
=============================== */

h1{

font-size:48px;

font-weight:800;

color:white;

}

h2{

font-weight:700;

color:white;

}

h3{

color:white;

}

/* ===============================
GLASS CARD
=============================== */

.glass{

background:rgba(255,255,255,.08);

padding:25px;

border-radius:20px;

backdrop-filter:blur(18px);

border:1px solid rgba(255,255,255,.15);

box-shadow:0px 8px 32px rgba(0,0,0,.35);

margin-bottom:20px;

}

/* ===============================
METRIC CARD
=============================== */

.metric-card{

background:

linear-gradient(
135deg,
#2563EB,
#06B6D4
);

padding:20px;

border-radius:18px;

text-align:center;

font-size:22px;

font-weight:bold;

color:white;

box-shadow:0px 8px 25px rgba(0,0,0,.35);

transition:.3s;

}

/* Hover */

.metric-card:hover{

transform:translateY(-8px);

}

/* ===============================
BUTTON
=============================== */

.stButton>button{

width:100%;

height:60px;

border:none;

border-radius:18px;

background:

linear-gradient(
90deg,
#2563EB,
#06B6D4
);

font-size:22px;

font-weight:bold;

color:white;

transition:.3s;

}

.stButton>button:hover{

transform:scale(1.03);

box-shadow:0px 10px 25px cyan;

}

/* ===============================
INPUTS
=============================== */

.stSelectbox label{

font-size:18px;

font-weight:600;

color:white;

}

.stNumberInput label{

font-size:18px;

font-weight:600;

color:white;

}

.stSlider label{

font-size:18px;

font-weight:600;

color:white;

}

/* ===============================
SUCCESS BOX
=============================== */

div[data-baseweb="notification"]{

border-radius:15px;

}

</style>
""", unsafe_allow_html=True)
#  HERO SECTION

st.markdown("""
<div class="glass" style="padding:40px;">

<h1 style="
text-align:center;
font-size:52px;
margin-bottom:5px;
">
🎓 AI Student Performance Advisor
</h1>

<h3 style="
text-align:center;
color:#9CA3AF;
margin-top:0;
">
Predict • Analyze • Improve
</h3>

<p style="
text-align:center;
font-size:18px;
color:#CBD5E1;
max-width:900px;
margin:auto;
line-height:1.8;
">
Experience an AI-powered dashboard that predicts student academic
performance using Machine Learning and provides smart insights,
interactive analytics and personalized recommendations for every student.
</p>

</div>
""", unsafe_allow_html=True)
# DASHBOARD STATS

st.markdown("<br>", unsafe_allow_html=True)

card1, card2, card3, card4 = st.columns(4)

with card1:
    st.markdown("""
    <div class="metric-card">
    📊
    <br><br>
    <span style="font-size:34px;">21</span><br>
    Features
    </div>
    """, unsafe_allow_html=True)

with card2:
    st.markdown("""
    <div class="metric-card">
    🤖
    <br><br>
    <span style="font-size:34px;">AI</span><br>
    Linear Regression
    </div>
    """, unsafe_allow_html=True)

with card3:
    st.markdown("""
    <div class="metric-card">
    🎯
    <br><br>
    <span style="font-size:34px;">100%</span><br>
    Smart Prediction
    </div>
    """, unsafe_allow_html=True)

with card4:
    st.markdown("""
    <div class="metric-card">
    ⚡
    <br><br>
    <span style="font-size:34px;">24×7</span><br>
    AI Advisor
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# FEATURE STRIP

f1, f2, f3 = st.columns(3)

with f1:
    st.info("📈 **Real-Time Prediction**")

with f2:
    st.success("🤖 **AI Powered Dashboard**")

with f3:
    st.warning("🎯 **Personalized Suggestions**")

st.divider()

# INPUT PANEL

left, right = st.columns([1.2,1])

with left:

    st.markdown("""
    <div class="glass">
    <h2>📝 Student Academic Profile</h2>
    <p style="color:#94A3B8;">
    Enter the student's academic and personal details.
    </p>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- Personal Information ----------------

    st.markdown("### 👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Age",
            min_value=15,
            max_value=30,
            value=20
        )

    with col2:
        gender = st.selectbox(
            "Gender",
            ["Male","Female"]
        )

    st.markdown("---")

    # ---------------- Academic Performance ----------------

    st.markdown("### 📚 Academic Performance")

    col1, col2 = st.columns(2)

    with col1:

        study_hours = st.slider(
            "Study Hours / Day",
            0.0,10.0,5.0
        )

        attendance = st.slider(
            "Attendance %",
            0.0,100.0,80.0
        )

        previous_grade = st.slider(
            "Previous Grade",
            0.0,100.0,75.0
        )

        assignments_completed = st.slider(
            "Assignments Completed",
            0,10,7
        )

        practice_tests_taken = st.slider(
            "Practice Tests",
            0,10,5
        )

    with col2:

        sleep_hours = st.slider(
            "Sleep Hours",
            3.0,10.0,7.0
        )

        group_study_hours = st.slider(
            "Group Study Hours",
            0.0,10.0,2.0
        )

        notes_quality_score = st.slider(
            "Notes Quality",
            1.0,10.0,7.0
        )

        time_management_score = st.slider(
            "Time Management",
            1.0,10.0,7.0
        )

        motivation_level = st.slider(
            "Motivation",
            1.0,10.0,7.0
        )

    st.markdown("---")

    # ---------------- Lifestyle ----------------

    st.markdown("### ❤️ Lifestyle")

    col1, col2 = st.columns(2)

    with col1:

        mental_health_score = st.slider(
            "Mental Health",
            1.0,10.0,7.0
        )

        screen_time = st.slider(
            "Screen Time",
            0.0,12.0,4.0
        )

    with col2:

        social_media_hours = st.slider(
            "Social Media Hours",
            0.0,10.0,2.0
        )

        internet_access = st.selectbox(
            "Internet Access",
            ["Yes","No"]
        )

    st.markdown("---")

    # ---------------- Family ----------------

    st.markdown("### 🏠 Family Details")

    col1, col2 = st.columns(2)

    with col1:

        family_income = st.selectbox(
            "Family Income",
            ["Low","Medium","High"]
        )

        parent_education = st.selectbox(
            "Parent Education",
            [
                "High School",
                "Bachelor",
                "Master",
                "PhD"
            ]
        )

    with col2:

        device_type = st.selectbox(
            "Device Type",
            [
                "Mobile",
                "Laptop",
                "Tablet"
            ]
        )

        school_type = st.selectbox(
            "School Type",
            [
                "Private",
                "Public"
            ]
        )

    extracurriculars = st.selectbox(
        "Extracurricular Activities",
        [
            "Coding Club",
            "Music",
            "Debate",
            "Sports",
            "Dance",
            "Art",
            "None"
        ]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    predict = st.button(
        "🚀 Predict Performance",
        use_container_width=True
    )
    prediction = None
    category = ""
    badge = ""
    
# PREDICTION
if predict:

    # Encode Categorical Features

    gender = 1 if gender == "Male" else 0

    parent_map = {
    "High School":0,
    "Bachelor":1,
    "Master":2,
    "PhD":3
}
    parent_education = parent_map[parent_education]

    income_map = {
    "Low":0,
    "Medium":1,
    "High":2
}
    family_income = income_map[family_income]

    device_map = {
    "Mobile":0,
    "Laptop":1,
    "Tablet":2
}
    device_type = device_map[device_type]

    school_map = {
    "Private":0,
    "Public":1
}
    school_type = school_map[school_type]

    extra_map = {
    "Coding Club":0,
    "Music":1,
    "Debate":2,
    "Sports":3,
    "Dance":4,
    "Art":5,
    "None":6
}
    extracurriculars = extra_map[extracurriculars]

    internet_access = 1 if internet_access == "Yes" else 0

    # Create DataFrame

    input_df = pd.DataFrame({

        "age":[age],

        "gender":[gender],

        "study_hours":[study_hours],

        "attendance":[attendance],

        "sleep_hours":[sleep_hours],

        "previous_grade":[previous_grade],

        "assignments_completed":[assignments_completed],

        "practice_tests_taken":[practice_tests_taken],

        "group_study_hours":[group_study_hours],

        "notes_quality_score":[notes_quality_score],

        "time_management_score":[time_management_score],

        "motivation_level":[motivation_level],

        "mental_health_score":[mental_health_score],

        "screen_time":[screen_time],

        "social_media_hours":[social_media_hours],

        "family_income":[family_income],

        "parent_education":[parent_education],

        "internet_access":[internet_access],

        "device_type":[device_type],

        "school_type":[school_type],

        "extracurriculars":[extracurriculars]

    })
# Scaling

    scaled_data = scaler.transform(input_df)

    # Prediction

    prediction = model.predict(scaled_data)[0]

    prediction = round(float(prediction),2)

    # Performance Category

    if prediction >= 90:

        category = "🏆 Excellent"

        badge = "🟢"

    elif prediction >= 80:

        category = "⭐ Very Good"

        badge = "🟢"

    elif prediction >= 70:

        category = "👍 Good"

        badge = "🟡"

    elif prediction >= 60:

        category = "🙂 Average"

        badge = "🟠"

    else:

        category = "⚠ Needs Improvement"

        badge = "🔴"

# RIGHT PANEL

if prediction is not None:

    with right:

        # AI DASHBOARD

        st.markdown("""
        <div class="glass">
            <h2 style="text-align:center;">🤖 AI Prediction Dashboard</h2>
            <p style="text-align:center;color:#94A3B8;">
                Machine Learning Prediction Result
            </p>
        </div>
        """, unsafe_allow_html=True)

    # BIG GAUGE

    fig = go.Figure(
        go.Indicator(

            mode="gauge+number+delta",

            value=prediction,

            delta={
                "reference":75
            },

            number={
                "suffix":"%",
                "font":{
                    "size":58
                }
            },

            title={
                "text":"Academic Score",
                "font":{
                    "size":24
                }
            },

            gauge={

                "shape":"angular",

                "axis":{
                    "range":[0,100],
                    "tickwidth":2
                },

                "bar":{
                    "color":"#22D3EE",
                    "thickness":0.35
                },

                "bgcolor":"rgba(255,255,255,.08)",

                "bordercolor":"#334155",

                "borderwidth":3,

                "steps":[

                    {
                        "range":[0,60],
                        "color":"#EF4444"
                    },

                    {
                        "range":[60,75],
                        "color":"#F59E0B"
                    },

                    {
                        "range":[75,90],
                        "color":"#3B82F6"
                    },

                    {
                        "range":[90,100],
                        "color":"#22C55E"
                    }

                ]

            }

        )
    )

    fig.update_layout(

        height=420,

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=10
        ),

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font_color="white"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # PERFORMANCE CARD

    st.markdown(f"""

    <div style="

    background:linear-gradient(
    135deg,
    rgba(37,99,235,.85),
    rgba(6,182,212,.85)
    );

    border-radius:25px;

    padding:28px;

    margin-top:20px;

    box-shadow:0 15px 35px rgba(0,0,0,.35);

    ">

    <h1 style="
    text-align:center;
    color:white;
    margin-bottom:10px;
    ">
    {prediction}%
    </h1>

    <h3 style="
    text-align:center;
    color:white;
    ">
    {badge} {category}
    </h3>

    </div>

    """, unsafe_allow_html=True)

    # MINI STATUS

    s1,s2,s3 = st.columns(3)

    with s1:
        st.metric(
            "🎯 Grade",
            f"{prediction}%"
        )

    with s2:
        st.metric(
            "📈 Attendance",
            f"{attendance}%"
        )

    with s3:
        st.metric(
            "📚 Study",
            f"{study_hours} hrs"
        )
   
 # KPI DASHBOARD
    academic_health=min(
        100,
        round(
            (
                attendance+
                study_hours*10+
                sleep_hours*8
            )/3,
            1
        )
    )

    confidence=max(
        82,
        min(
            99,
            round(prediction+10)
        )
    )

    focus_score=round(
        (
            motivation_level*10+
            notes_quality_score*10+
            time_management_score*10
        )/3,
        1
    )

    if prediction>=85:
        risk="🟢 LOW"

    elif prediction>=70:
        risk="🟡 MEDIUM"

    else:
        risk="🔴 HIGH"

    st.markdown("<br>",unsafe_allow_html=True)

    k1,k2=st.columns(2)

    with k1:

        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#2563EB,#06B6D4);
        padding:22px;
        border-radius:22px;
        color:white;
        box-shadow:0 15px 30px rgba(0,0,0,.35);
        ">
        <h4>❤️ Academic Health</h4>
        <h1>{academic_health}%</h1>
        </div>
        """,unsafe_allow_html=True)

    with k2:

        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#9333EA,#6366F1);
        padding:22px;
        border-radius:22px;
        color:white;
        box-shadow:0 15px 30px rgba(0,0,0,.35);
        ">
        <h4>🤖 AI Confidence</h4>
        <h1>{confidence}%</h1>
        </div>
        """,unsafe_allow_html=True)

    st.markdown("<br>",unsafe_allow_html=True)

    k3,k4=st.columns(2)

    with k3:

        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#0EA5E9,#06B6D4);
        padding:22px;
        border-radius:22px;
        color:white;
        box-shadow:0 15px 30px rgba(0,0,0,.35);
        ">
        <h4>🎯 Focus Score</h4>
        <h1>{focus_score}%</h1>
        </div>
        """,unsafe_allow_html=True)

    with k4:

        st.markdown(f"""
        <div style="
        background:linear-gradient(135deg,#10B981,#22C55E);
        padding:22px;
        border-radius:22px;
        color:white;
        box-shadow:0 15px 30px rgba(0,0,0,.35);
        ">
        <h4>⚠ Risk Level</h4>
        <h1>{risk}</h1>
        </div>
        """,unsafe_allow_html=True)

    st.markdown("<br>",unsafe_allow_html=True)

    st.subheader("📈 Overall Performance")

    st.progress(prediction/100)

    st.caption(f"Current Performance : {prediction}%")

    st.divider()

# STUDENT SUMMARY

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style='text-align:center;color:white;'>
👨‍🎓 Student Overview
</h2>
<p style='text-align:center;color:#94A3B8;'>
AI Generated Student Academic Profile
</p>
""", unsafe_allow_html=True)

left, right = st.columns(2)

# ===============================
# LEFT CARD
# ===============================

with left:

    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#1E3A8A,#0F172A);
    border-radius:28px;
    padding:28px;
    box-shadow:0 15px 35px rgba(0,0,0,.40);
    color:white;
    ">

    <h2>📚 Academic Profile</h2>

    <hr>

    <h4>🎯 Previous Grade</h4>
    <h2 style="color:#22D3EE;">{previous_grade}%</h2>

    <br>

    <h4>📖 Study Hours</h4>
    <h3>{study_hours} hrs/day</h3>

    <br>

    <h4>🏫 Attendance</h4>
    <h3>{attendance}%</h3>

    <br>

    <h4>😴 Sleep</h4>
    <h3>{sleep_hours} hrs/day</h3>

    <br>

    <h4>👥 Group Study</h4>
    <h3>{group_study_hours} hrs/day</h3>

    </div>
    """, unsafe_allow_html=True)

# ===============================
# RIGHT CARD
# ===============================

with right:

    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#312E81,#111827);
    border-radius:28px;
    padding:28px;
    box-shadow:0 15px 35px rgba(0,0,0,.40);
    color:white;
    ">

    <h2>⚡ Learning Insights</h2>

    <hr>

    <h4>📝 Assignments</h4>
    <h3>{assignments_completed}</h3>

    <br>

    <h4>📄 Practice Tests</h4>
    <h3>{practice_tests_taken}</h3>

    <br>

    <h4>🎯 Motivation</h4>
    <h3>{motivation_level}/10</h3>

    <br>

    <h4>🧠 Mental Health</h4>
    <h3>{mental_health_score}/10</h3>

    <br>

    <h4>📱 Screen Time</h4>
    <h3>{screen_time} hrs/day</h3>

    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# QUICK METRICS
# ==========================================================

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("📚 Study", f"{study_hours} hrs")

with m2:
    st.metric("🏫 Attendance", f"{attendance}%")

with m3:
    st.metric("🎯 Motivation", f"{motivation_level}/10")

with m4:
    st.metric("😴 Sleep", f"{sleep_hours} hrs")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# AI STATUS BAR
# ==========================================================

status = min(
    100,
    round(
        (
            attendance +
            previous_grade +
            motivation_level*10 +
            (10-screen_time)*5
        )/4,
        1
    )
)

st.markdown("### 🚀 Overall Academic Readiness")

st.progress(status/100)

if status >= 90:

    st.success("🏆 Excellent Academic Profile")

elif status >= 80:

    st.success("🚀 Very Good Academic Profile")

elif status >= 70:

    st.info("📚 Good Academic Profile")

elif status >= 60:

    st.warning("⚠ Needs Improvement")

else:

    st.error("🚨 High Academic Risk")

st.divider()
# st.subheader("👨‍🎓 Student Overview")

# st.markdown("<br>", unsafe_allow_html=True)

# c1, c2 = st.columns(2)

# with c1:

#     st.markdown(f"""
#     <div style="

#     background:rgba(255,255,255,.08);

#     border-radius:22px;

#     padding:22px;

#     border:1px solid rgba(255,255,255,.10);

#     backdrop-filter:blur(20px);

#     box-shadow:0 12px 30px rgba(0,0,0,.30);

#     ">

#     <h3>📚 Academic Profile</h3>

#     <hr>

#     <p>🎯 <b>Previous Grade</b> : {previous_grade}</p>

#     <p>📖 <b>Study Hours</b> : {study_hours} hrs/day</p>

#     <p>🏫 <b>Attendance</b> : {attendance}%</p>

#     <p>😴 <b>Sleep</b> : {sleep_hours} hrs</p>

#     <p>👥 <b>Group Study</b> : {group_study_hours} hrs</p>

#     </div>

#     """, unsafe_allow_html=True)


# with c2:

#     st.markdown(f"""
#     <div style="

#     background:rgba(255,255,255,.08);

#     border-radius:22px;

#     padding:22px;

#     border:1px solid rgba(255,255,255,.10);

#     backdrop-filter:blur(20px);

#     box-shadow:0 12px 30px rgba(0,0,0,.30);

#     ">

#     <h3>⚡ Learning Insights</h3>

#     <hr>

#     <p>📝 <b>Assignments</b> : {assignments_completed}</p>

#     <p>📄 <b>Practice Tests</b> : {practice_tests_taken}</p>

#     <p>🎯 <b>Motivation</b> : {motivation_level}/10</p>

#     <p>🧠 <b>Mental Health</b> : {mental_health_score}/10</p>

#     <p>📱 <b>Screen Time</b> : {screen_time} hrs</p>

#     </div>

#     """, unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)

# # QUICK INSIGHTS

# q1, q2, q3 = st.columns(3)

# with q1:
#     st.metric(
#         "📚 Study Index",
#         f"{round(study_hours*10)}%"
#     )

# with q2:
#     st.metric(
#         "🏫 Attendance",
#         f"{attendance}%"
#     )

# with q3:
#     st.metric(
#         "🎯 Motivation",
#         f"{motivation_level*10}%"
#     )

# st.divider()
 
# PERFORMANCE DONUT


st.subheader("🎯 Performance Analytics")

donut_left, donut_right = st.columns([1.1,1])

with donut_left:

    # Safe value
    score = prediction if prediction is not None else 0

    fig = go.Figure()

    fig.add_trace(

        go.Pie(

            labels=["Achieved","Remaining"],

            values=[score,100-score],

            hole=0.72,

            marker=dict(

                colors=[

                    "#06B6D4",

                    "#1E293B"

                ]

            ),

            textinfo="none",

            hovertemplate="%{label}<br>%{value}%<extra></extra>"

        )

    )

    fig.update_layout(

        height=360,

        margin=dict(
            l=10,
            r=10,
            t=10,
            b=10
        ),

        showlegend=True,

        legend=dict(
            orientation="h",
            y=-0.10
        ),

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="white",
            size=14
        ),

        annotations=[

            dict(

                text=f"<b>{prediction}%</b><br>Score",

                showarrow=False,

                font=dict(
                    size=24,
                    color="white"
                )

            )

        ]

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================================
# RIGHT : PERFORMANCE STATUS
# ==========================================================

with donut_right:

    if prediction is None:
        prediction = 0

    st.markdown(
        f"""
<div style="
background:rgba(255,255,255,.08);
padding:25px;
border-radius:25px;
border:1px solid rgba(255,255,255,.12);
backdrop-filter:blur(18px);
box-shadow:0 12px 35px rgba(0,0,0,.35);
">

<h2>📊 Performance Status</h2>

<hr>

<h3>Current Grade</h3>

<h1 style="color:#22D3EE;font-size:52px;">
{prediction:.1f}%
</h1>

<p style="color:#CBD5E1;">
Your academic performance has been analysed using Machine Learning.
</p>

<hr>

<h3>{badge} {category}</h3>

</div>
""",
        unsafe_allow_html=True
    )

    st.metric(
        "📚 Study Hours",
        f"{study_hours:.1f} hrs/day"
    )

    st.metric(
        "🏫 Attendance",
        f"{attendance:.0f}%"
    )

    st.metric(
        "🎯 Motivation",
        f"{motivation_level}/10"
    )

st.divider()

#  AI RADAR ANALYTICS

st.subheader("🧠 AI Learning Analytics")

left_radar, right_radar = st.columns([1.3,1])

# RADAR CHART

with left_radar:

    categories = [
        "Study",
        "Attendance",
        "Notes",
        "Motivation",
        "Mental Health",
        "Practice"
    ]

    values = [
        study_hours*10,
        attendance,
        notes_quality_score*10,
        motivation_level*10,
        mental_health_score*10,
        practice_tests_taken*10
    ]

    radar = go.Figure()

    radar.add_trace(

        go.Scatterpolar(

            r=values,

            theta=categories,

            fill="toself",

            fillcolor="rgba(34,211,238,0.35)",

            line=dict(
                color="#22D3EE",
                width=4
            ),

            marker=dict(
                size=9,
                color="#38BDF8"
            ),

            name="Student"

        )

    )

    radar.update_layout(

        height=470,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="white",
            size=14
        ),

        polar=dict(

            bgcolor="rgba(255,255,255,.02)",

            radialaxis=dict(

                visible=True,

                range=[0,100],

                tickfont=dict(
                    color="white"
                ),

                gridcolor="rgba(255,255,255,.15)"

            ),

            angularaxis=dict(

                gridcolor="rgba(255,255,255,.15)"

            )

        ),

        showlegend=False

    )

    st.plotly_chart(
        radar,
        use_container_width=True
    )

# AI INSIGHTS

with right_radar:

    st.markdown(f"""
    <div style="
    background:rgba(255,255,255,.08);
    padding:25px;
    border-radius:25px;
    border:1px solid rgba(255,255,255,.12);
    backdrop-filter:blur(18px);
    box-shadow:0 12px 30px rgba(0,0,0,.35);
    ">

    <h2>🤖 AI Insights</h2>

    <hr>

    <h4>Overall Prediction</h4>

    <h1 style="color:#22D3EE;">
    {prediction}%
    </h1>

    <p>
    Machine Learning indicates that the student's
    overall academic performance is
    <b>{category}</b>.
    </p>

    </div>

    """, unsafe_allow_html=True)

    st.metric(
        "📚 Learning Efficiency",
        f"{round((study_hours*10 + notes_quality_score*10)/2)}%"
    )

    st.metric(
        "⚡ Focus Index",
        f"{round((motivation_level*10 + time_management_score*10)/2)}%"
    )

    st.metric(
        "❤️ Wellness Index",
        f"{round((mental_health_score*10 + sleep_hours*10)/2)}%"
    )

    st.metric(
        "🎯 Practice Readiness",
        f"{practice_tests_taken*10}%"
    )

st.divider()
# ==========================================================
# 🤖 AI MENTOR
# ==========================================================

if prediction is not None:

    st.subheader("🤖 AI Academic Mentor")

    if prediction >= 90:

        mentor_title = "🌟 Outstanding Performance"

        mentor_msg = """
✔ You are performing exceptionally well.

✔ Maintain your current study routine.

✔ Keep solving advanced practice papers.

✔ Continue balancing academics and health.

✔ Keep helping other students.
"""

        mentor_color = "#22C55E"

    elif prediction >= 80:

        mentor_title = "🚀 Great Progress"

        mentor_msg = """
✔ Very impressive performance.

✔ Revise regularly.

✔ Increase mock test practice.

✔ Maintain attendance above 90%.

✔ Improve time management.
"""

        mentor_color = "#3B82F6"

    elif prediction >= 70:

        mentor_title = "📚 Good Performance"

        mentor_msg = """
✔ You're doing well.

✔ Increase study hours.

✔ Improve note preparation.

✔ Practice previous year papers.

✔ Focus on weak subjects.
"""

        mentor_color = "#F59E0B"

    elif prediction >= 60:

        mentor_title = "⚠ Average Performance"

        mentor_msg = """
✔ Your performance is average.

✔ Study consistently.

✔ Revise every day.

✔ Reduce distractions.

✔ Complete assignments on time.
"""

        mentor_color = "#FB923C"

    else:

        mentor_title = "🚨 High Academic Risk"

        mentor_msg = """
✔ Immediate improvement is required.

✔ Follow a daily study schedule.

✔ Seek guidance from teachers.

✔ Reduce social media usage.

✔ Improve attendance.
"""

        mentor_color = "#EF4444"

    st.markdown(
        f"""
<div style="
background:linear-gradient(135deg,#111827,#1E293B);
padding:30px;
border-radius:25px;
border-left:8px solid {mentor_color};
box-shadow:0 12px 30px rgba(0,0,0,.35);
">

<h2 style="color:white;margin-bottom:15px;">
{mentor_title}
</h2>

<div style="
color:#E5E7EB;
font-size:18px;
line-height:2;
white-space:pre-line;
">
{mentor_msg}
</div>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.info(
        "💡 AI Mentor Tip: Small improvements every day produce excellent long-term results."
    )

    tip1, tip2 = st.columns(2)
# AI Quick Tips

tip1, tip2 = st.columns(2)

with tip1:

    st.success("📖 Revise for at least 30 minutes daily.")

    st.success("😴 Sleep 7–8 hours regularly.")

    st.success("📝 Make concise revision notes.")

with tip2:

    st.info("🏫 Maintain attendance above 90%.")

    st.info("📱 Reduce unnecessary screen time.")

    st.info("🎯 Attempt weekly mock tests.")

st.divider()

# 💪 STRENGTHS & IMPROVEMENT ANALYSIS

st.subheader("💪 Strength & Improvement Analysis")

left_strength, right_strength = st.columns(2)

# STRENGTHS

with left_strength:

    st.markdown("""
    <div style="
    background:rgba(34,197,94,.12);
    border-left:6px solid #22C55E;
    border-radius:20px;
    padding:25px;
    ">
    <h3>✅ Student Strengths</h3>
    </div>
    """, unsafe_allow_html=True)

    if attendance >= 90:
        st.success("🏫 Excellent Attendance")

    if study_hours >= 6:
        st.success("📚 Strong Study Habit")

    if notes_quality_score >= 8:
        st.success("📝 High Quality Notes")

    if motivation_level >= 8:
        st.success("🎯 Highly Motivated")

    if mental_health_score >= 8:
        st.success("❤️ Good Mental Health")

    if practice_tests_taken >= 7:
        st.success("📄 Regular Mock Test Practice")

# IMPROVEMENT

with right_strength:

    st.markdown("""
    <div style="
    background:rgba(239,68,68,.12);
    border-left:6px solid #EF4444;
    border-radius:20px;
    padding:25px;
    ">
    <h3>📈 Areas for Improvement</h3>
    </div>
    """, unsafe_allow_html=True)

    if attendance < 85:
        st.warning("🏫 Improve Attendance")

    if study_hours < 5:
        st.warning("📚 Increase Study Hours")

    if notes_quality_score < 6:
        st.warning("📝 Improve Notes")

    if motivation_level < 6:
        st.warning("🎯 Stay Motivated")

    if screen_time > 5:
        st.warning("📱 Reduce Screen Time")

    if social_media_hours > 3:
        st.warning("📵 Limit Social Media Usage")

    if sleep_hours < 7:
        st.warning("😴 Improve Sleep Schedule")

st.divider()

# 📊 PERFORMANCE INDICATORS

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style='color:white;text-align:center;'>
📊 AI Performance Indicators
</h2>
""", unsafe_allow_html=True)

# -------------------------------
# Calculations
# -------------------------------

study_index = max(0, min(100, round(study_hours * 10)))

focus_index = max(
    0,
    min(
        100,
        round(
            (
                motivation_level*10 +
                time_management_score*10 +
                notes_quality_score*10
            )/3
        )
    )
)

wellness_index = max(
    0,
    min(
        100,
        round(
            (
                mental_health_score*10 +
                sleep_hours*10
            )/2
        )
    )
)

academic_health = max(
    0,
    min(
        100,
        round(
            (
                attendance +
                study_index +
                focus_index +
                wellness_index
            )/4
        )
    )
)

# Safety check

if prediction is None:
    prediction = 0

prediction = float(prediction)

confidence = max(
    70,
    min(
        99,
        round(prediction + 5)
    )
)

recommendation_score = round(
    (
        study_index +
        focus_index +
        wellness_index
    )/3,
    1
)

# -------------------------------
# KPI CARDS
# -------------------------------

k1,k2,k3,k4 = st.columns(4)

with k1:

    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#2563EB,#06B6D4);
    padding:22px;
    border-radius:22px;
    color:white;
    text-align:center;
    box-shadow:0 10px 25px rgba(0,0,0,.35);
    ">
    <h3>📚 Study Index</h3>
    <h1>{study_index}%</h1>
    </div>
    """, unsafe_allow_html=True)

    st.progress(study_index/100)

with k2:

    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#8B5CF6,#EC4899);
    padding:22px;
    border-radius:22px;
    color:white;
    text-align:center;
    box-shadow:0 10px 25px rgba(0,0,0,.35);
    ">
    <h3>🎯 Focus</h3>
    <h1>{focus_index}%</h1>
    </div>
    """, unsafe_allow_html=True)

    st.progress(focus_index/100)

with k3:

    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#10B981,#22D3EE);
    padding:22px;
    border-radius:22px;
    color:white;
    text-align:center;
    box-shadow:0 10px 25px rgba(0,0,0,.35);
    ">
    <h3>❤️ Wellness</h3>
    <h1>{wellness_index}%</h1>
    </div>
    """, unsafe_allow_html=True)

    st.progress(wellness_index/100)

with k4:

    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#F59E0B,#F97316);
    padding:22px;
    border-radius:22px;
    color:white;
    text-align:center;
    box-shadow:0 10px 25px rgba(0,0,0,.35);
    ">
    <h3>🤖 AI Confidence</h3>
    <h1>{confidence}%</h1>
    </div>
    """, unsafe_allow_html=True)

    st.progress(confidence/100)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------
# OVERALL HEALTH CARD
# -------------------------------

st.markdown(f"""
<div style="
background:linear-gradient(135deg,#0F172A,#1E293B);
padding:30px;
border-radius:25px;
border:1px solid rgba(255,255,255,.12);
box-shadow:0 15px 35px rgba(0,0,0,.45);
">

<h2 style="color:white;">
🧠 Overall Academic Health
</h2>

<h1 style="
font-size:65px;
color:#22D3EE;
margin-bottom:0px;
">
{academic_health}%
</h1>

<p style="
font-size:18px;
color:#CBD5E1;
">

AI Readiness Score :
<b>{recommendation_score}%</b>

</p>

</div>
""", unsafe_allow_html=True)

st.progress(academic_health/100)

# -------------------------------
# STATUS
# -------------------------------

if recommendation_score >= 90:

    st.success("🏆 Excellent! You are fully prepared.")

elif recommendation_score >= 80:

    st.success("🚀 Great! Keep maintaining consistency.")

elif recommendation_score >= 70:

    st.info("📚 Good performance. Small improvements can boost your score.")

elif recommendation_score >= 60:

    st.warning("⚠ You're improving, but consistency is needed.")

else:

    st.error("🚨 High Academic Risk. Follow the AI recommendations carefully.")

st.divider()

# FINAL STATUS

st.markdown("<br>", unsafe_allow_html=True)

if prediction >= 90:

    st.success("🏆 Outstanding Performance!")

    st.balloons()

elif prediction >= 80:

    st.success("🌟 Excellent Progress!")

elif prediction >= 70:

    st.info("👍 Good Performance! Keep Improving.")

else:

    st.warning("📚 More Practice Recommended.")

# FOOTER

st.markdown("""

---

<center>

<h3>🎓 AI Student Performance Prediction System</h3>

<p>

Developed using

<b>Python • Streamlit • Plotly • Scikit-Learn</b>

</p>

<p>

IBM PBEL Machine Learning Project

</p>

</center>

""", unsafe_allow_html=True)