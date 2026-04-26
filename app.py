import streamlit as st
from streamlit_folium import st_folium

from backend.data_loader import prepare_outbreak_summary
from backend.llm_engine import get_ai_recommendation
from backend.map_generator import create_outbreak_map
from backend.hospital_dashboard import get_hospital_data


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="EpiSense Dashboard",
    page_icon="🩺",
    layout="wide"
)


# ---------------------------------------------------
# CUSTOM CSS (UI POLISH)
# ---------------------------------------------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0B1220;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #1F2937;
}

/* Main Title */
.main-title {
    font-size: 42px;
    font-weight: 700;
    color: white;
    margin-bottom: 10px;
}

/* Subtitle */
.sub-title {
    font-size: 20px;
    color: #CBD5E1;
    margin-bottom: 30px;
}

/* Section Titles */
.section-title {
    font-size: 26px;
    font-weight: 600;
    margin-top: 30px;
    margin-bottom: 15px;
    color: #F8FAFC;
}

/* Buttons */
.stButton > button {
    width: 100%;
    background-color: #2563EB;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 12px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #1D4ED8;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown("""
<div class="main-title">
🩺 EpiSense — AI Disease Prevention Dashboard
</div>

<div class="sub-title">
Predict Early → Prevent Faster → Act Smarter
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.markdown("## Public Health Control Center")

location = st.sidebar.selectbox(
    "Select Locality",
    [
        "KR Puram",
        "Whitefield"
    ]
)

disease = st.sidebar.selectbox(
    "Select Disease",
    [
        "Dengue",
        "Viral Fever",
        "Respiratory Infection"
    ]
)

analyze_button = st.sidebar.button("Analyze Outbreak")


# ---------------------------------------------------
# MAIN LOGIC
# ---------------------------------------------------

if analyze_button:

    with st.spinner("Analyzing outbreak using Local AI (Ollama)..."):

        outbreak_data = prepare_outbreak_summary(location, disease)
        ai_result = get_ai_recommendation(outbreak_data)

    # -----------------------------------------------
    # TOP METRICS
    # -----------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📍 Location", outbreak_data["location"])

    with col2:
        st.metric("🦠 Disease", outbreak_data["disease"])

    with col3:
        st.metric("📈 New Cases", outbreak_data["new_cases"])

    st.markdown("---")

    # -----------------------------------------------
    # OUTBREAK DATA SUMMARY
    # -----------------------------------------------

    st.markdown("""
    <div class="section-title">
    📊 Outbreak Data Summary
    </div>
    """, unsafe_allow_html=True)

    st.json(outbreak_data)

    st.markdown("---")

    # -----------------------------------------------
    # AI RECOMMENDATIONS
    # -----------------------------------------------

    st.markdown("""
    <div class="section-title">
    🤖 AI Government Recommendations
    </div>
    """, unsafe_allow_html=True)

    st.write(ai_result)

    st.markdown("---")

    # -----------------------------------------------
    # LIVE OUTBREAK MAP
    # -----------------------------------------------

    st.markdown("""
    <div class="section-title">
    🗺 Live Outbreak Risk Map
    </div>
    """, unsafe_allow_html=True)

    outbreak_map = create_outbreak_map()

    st_folium(
        outbreak_map,
        width=1200,
        height=500
    )

    st.markdown("---")

    # -----------------------------------------------
    # HOSPITAL READINESS
    # -----------------------------------------------

    st.markdown("""
    <div class="section-title">
    🏥 Clinical Monitoring & Hospital Readiness
    </div>
    """, unsafe_allow_html=True)

    hospital_data = get_hospital_data(location)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Hospital Availability")
        st.metric(
            "Total Hospitals in Locality",
            outbreak_data["total_hospitals"]
        )

    with col2:
        st.markdown("### Hospital Types")
        st.dataframe(
            hospital_data[
                ["hospital_name", "hospital_type"]
            ],
            use_container_width=True
        )

else:
    st.info(
        "Select locality and disease, then click Analyze Outbreak"
    )