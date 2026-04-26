import pandas as pd


def get_hospital_data(location):
    hospital_df = pd.read_csv("data/raw/hospital_master.csv")

    hospital_filtered = hospital_df[
        hospital_df["locality"] == location
    ]

    return hospital_filtered