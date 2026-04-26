import folium


def create_outbreak_map():
    # Center map on Bangalore
    outbreak_map = folium.Map(
        location=[12.9716, 77.5946],
        zoom_start=11
    )

    outbreak_locations = [
        {
            "name": "KR Puram",
            "lat": 13.0080,
            "lon": 77.6950,
            "risk": "High Risk 🔴"
        },
        {
            "name": "Whitefield",
            "lat": 12.9698,
            "lon": 77.7499,
            "risk": "Medium Risk 🟠"
        },
        {
            "name": "Indiranagar",
            "lat": 12.9784,
            "lon": 77.6408,
            "risk": "Low Risk 🟢"
        }
    ]

    for place in outbreak_locations:
        folium.Marker(
            location=[place["lat"], place["lon"]],
            popup=f"{place['name']} - {place['risk']}",
            tooltip=place["name"]
        ).add_to(outbreak_map)

    return outbreak_map