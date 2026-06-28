import streamlit as st
import pandas as pd

CROP_IDEALS = {
    "rice": {
        "water": (70, 100, "%"),
        "nitrogen": (80, 120, "kg/ha"),
        "phosphorus": (30, 60, "kg/ha"),
        "temperature": (20, 35, "°C"),
        "potassium": (40, 80, "kg/ha"),
        "ph": (5.5, 6.5, "")
    },
    "wheat": {
        "water": (40, 70, "%"),
        "nitrogen": (100, 150, "kg/ha"),
        "phosphorus": (40, 60, "kg/ha"),
        "temperature": (15, 25, "°C"),
        "potassium": (40, 70, "kg/ha"),
        "ph": (6.0, 7.5, "")
    }
}


def recommendation(param, value, low, high, unit):
    name = param.title()

    if value < low:
        return "low", f"{name} is low. Increase it toward {low}–{high} {unit}."
    elif value > high:
        return "high", f"{name} is high. Reduce it toward {low}–{high} {unit}."
    else:
        return "normal", f"{name} is within the ideal range."


st.set_page_config(
    page_title="Soil Health Demo",
    layout="wide"
)

st.title("🌱 Soil Health Recommendation System")

crop = st.text_input(
    "Enter crop name",
    placeholder="rice or wheat"
).lower().strip()

st.subheader("Enter Sensor Readings Manually")

water = st.number_input("Water Level (%)", min_value=0.0, max_value=100.0)
nitrogen = st.number_input("Nitrogen (kg/ha)", min_value=0.0)
phosphorus = st.number_input("Phosphorus (kg/ha)", min_value=0.0)
temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=60.0)
potassium = st.number_input("Potassium (kg/ha)", min_value=0.0)
ph = st.number_input("pH", min_value=0.0, max_value=14.0)

if st.button("Analyze Soil Health"):
    if crop not in CROP_IDEALS:
        st.error("Crop not found. Try rice or wheat.")
    else:
        user_values = {
            "water": water,
            "nitrogen": nitrogen,
            "phosphorus": phosphorus,
            "temperature": temperature,
            "potassium": potassium,
            "ph": ph
        }

        results = []
        suggestions = []
        normal_count = 0

        for param, value in user_values.items():
            low, high, unit = CROP_IDEALS[crop][param]

            if value < low:
                status = "Low"
            elif value > high:
                status = "High"
            else:
                status = "Normal"
                normal_count += 1

            results.append({
                "Parameter": param.title(),
                "Your Reading": f"{value} {unit}",
                "Ideal Range": f"{low}–{high} {unit}",
                "Status": status
            })

            suggestions.append(
                recommendation(param, value, low, high, unit)
            )

        score = int((normal_count / len(user_values)) * 100)

        st.divider()

        st.subheader("Soil Analysis Report")

        st.dataframe(
            pd.DataFrame(results),
            use_container_width=True,
            hide_index=True
        )

        st.subheader("Overall Soil Health Score")
        st.progress(score / 100)
        st.write(f"**Score: {score}%**")

        if score >= 80:
            st.success("The soil condition is good for this crop.")
        elif score >= 50:
            st.warning("The soil condition is fair. Some improvements are needed.")
        else:
            st.error("The soil condition is poor. Immediate improvements are recommended.")

        st.divider()

        st.subheader("Recommendations")

        for level, message in suggestions:
            if level == "normal":
                st.success(message)
            elif level == "low":
                st.warning(message)
            else:
                st.error(message)