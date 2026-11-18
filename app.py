import streamlit as st
import requests

st.title("🐧 Zoologist Front")
st.markdown("Enter the penguin's measurements below to predict its species.")

# 1. Input controllers for the user
island = st.selectbox("Island", ["Biscoe", "Dream", "Torgersen"])
bill_length_mm = st.number_input(
    "Bill length (mm)", min_value=0.0, value=39.1, step=0.1
)
bill_depth_mm = st.number_input(
    "Bill depth (mm)", min_value=0.0, value=18.7, step=0.1
)
flipper_length_mm = st.number_input(
    "Flipper length (mm)", min_value=0.0, value=181.0, step=1.0
)
body_mass_g = st.number_input(
    "Body mass (g)", min_value=0.0, value=3750.0, step=10.0
)
sex = st.selectbox("Sex", ["Male", "Female"])

url = "https://zoo-api-953497524187.asia-northeast1.run.app/predict"

if st.button("Predict Species"):
  params = {
      "island": island,
      "bill_length_mm": bill_length_mm,
      "bill_depth_mm": bill_depth_mm,
      "flipper_length_mm": flipper_length_mm,
      "body_mass_g": body_mass_g,
      "sex": sex,
  }
  try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    prediction = response.json()
    st.success(f"Predicted Species: **{prediction}**")
  except requests.exceptions.RequestException as e:
    st.error(f"Error calling the API: {e}")
