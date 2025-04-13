import streamlit as st

# Streamlit UI Configuration
st.set_page_config(page_title="Seizure Prevention System", layout="centered")

# Title and Description
st.title("🩺 Seizure Prevention System")
st.write("Enter patient details to predict seizure risk.")

# User Input Fields
temperature = st.number_input("Body Temperature (°C)", min_value=90.0, max_value=101.9, step=0.1)
heart_rate = st.number_input("Heart Rate (BPM)", min_value=70, max_value=200, step=1)
motion_level = st.number_input("Motion Level (0 - 2)", min_value=15.00, max_value=20.00, step=0.1)

# Predict Button
if st.button("Predict Seizure Risk Validation 🚑"):
    if temperature and heart_rate and motion_level:
        # Dummy prediction logic
        if temperature > 100 or heart_rate > 150 or motion_level > 18:
            prediction = "HIGH"
        else:
            prediction = "LOW"

        st.success(f"Seizure Risk: **{prediction}**")
        if prediction == "HIGH":
            st.error("⚠️ Immediate medical attention required!")
    else:
        st.warning("⚠️ Please enter all values before predicting.")

# Footer
st.write("---")
st.write("🔬 **Machine Learning-Based Seizure Risk Prediction** | Developed with ❤️")
