import pandas as pd


def load_all_data():
    hospital_df = pd.read_csv("data/raw/hospital_master.csv")
    clinical_df = pd.read_csv("data/raw/clinical_reports.csv")
    weather_df = pd.read_csv("data/raw/weather_data.csv")
    aqi_df = pd.read_csv("data/raw/aqi_data.csv")

    return hospital_df, clinical_df, weather_df, aqi_df


def prepare_outbreak_summary(location, disease):
    hospital_df, clinical_df, weather_df, aqi_df = load_all_data()

    clinical_filtered = clinical_df[
        (clinical_df["locality"] == location) &
        (clinical_df["disease_type"] == disease)
    ]

    weather_filtered = weather_df[
        weather_df["locality"] == location
    ]

    aqi_filtered = aqi_df[
        aqi_df["locality"] == location
    ]

    hospital_filtered = hospital_df[
        hospital_df["locality"] == location
    ]

    outbreak_summary = {
        "location": location,
        "disease": disease,
        "new_cases": int(clinical_filtered["new_cases_today"].sum()),
        "severe_cases": int(clinical_filtered["severe_cases"].sum()),
        "admissions": int(clinical_filtered["admissions"].sum()),
        "humidity": weather_filtered.iloc[0]["humidity"],
        "rainfall": weather_filtered.iloc[0]["rainfall"],
        "weather_condition": weather_filtered.iloc[0]["weather_condition"],
        "AQI": int(aqi_filtered.iloc[0]["AQI"]),
        "total_hospitals": len(hospital_filtered),
        "hospital_status": "Hospitals reporting unusual surge"
    }

    return outbreak_summary