import streamlit as st
import pandas as pd
import joblib

# Load your pre-trained model
try:
    model = joblib.load('heart_decision_tree.pkl')  # Ensure the path is correct
except Exception as e:
    st.error(f"Error loading the model: {e}")

# Title of the app
st.title("Heart Disease Prediction App")

# Sidebar for user input
st.sidebar.header("User Input Features")

# Define original to encoded mappings
chest_pain_mapping = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
fasting_blood_sugar_mapping = {'> 120 mg/dl': 1, '<= 120 mg/dl': 0}
resting_ecg_mapping = {'Normal': 0, 'ST-T wave abnormality': 1, 'Left ventricular hypertrophy': 2}
exercise_angina_mapping = {'Yes': 1, 'No': 0}
slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
thalassemia_mapping = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2, 'Other': 3}
number_of_vessels_mapping = {0: 0, 1: 1, 2: 2, 3: 3}


# Define input fields
def user_input_features():
    age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=25)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])

    # Show original values for Chest Pain Type
    chest_pain_type = st.sidebar.selectbox("Chest Pain Type", list(chest_pain_mapping.keys()))

    resting_blood_pressure = st.sidebar.number_input("Resting Blood Pressure", min_value=0, max_value=300, value=120)
    cholesterol = st.sidebar.number_input("Cholesterol", min_value=0, max_value=600, value=200)

    # Show original values for Fasting Blood Sugar
    fasting_blood_sugar = st.sidebar.selectbox("Fasting Blood Sugar", list(fasting_blood_sugar_mapping.keys()))

    # Show original values for Resting ECG
    resting_ecg = st.sidebar.selectbox("Resting ECG", list(resting_ecg_mapping.keys()))

    max_heart_rate = st.sidebar.number_input("Max Heart Rate", min_value=60, max_value=200, value=150)

    # Show original values for Exercise Angina
    exercise_angina = st.sidebar.selectbox("Exercise Angina", list(exercise_angina_mapping.keys()))

    st_depression = st.sidebar.number_input("ST Depression", min_value=0.0, max_value=10.0, value=1.0)

    # Show original values for Slope
    slope = st.sidebar.selectbox("Slope", list(slope_mapping.keys()))

    # Show original values for Number of Major Vessels
    number_of_vessels = st.sidebar.selectbox("Number of Major Vessels", list(number_of_vessels_mapping.keys()))

    # Show original values for Thalassemia
    thalassemia = st.sidebar.selectbox("Thalassemia", list(thalassemia_mapping.keys()))

    # Map original values to encoded values
    data = {
        'age': age,
        'sex': 1 if gender == 'Male' else 0,  # Assuming binary encoding
        'cp': chest_pain_mapping[chest_pain_type],  # Map to encoded value
        'trestbps': resting_blood_pressure,
        'chol': cholesterol,
        'fbs': fasting_blood_sugar_mapping[fasting_blood_sugar],  # Map to encoded value
        'restecg': resting_ecg_mapping[resting_ecg],  # Map to encoded value
        'thalach': max_heart_rate,
        'exang': exercise_angina_mapping[exercise_angina],  # Map to encoded value
        'oldpeak': st_depression,
        'slope': slope_mapping[slope],  # Map to encoded value
        'ca': number_of_vessels_mapping[number_of_vessels],  # Map to encoded value
        'thal': thalassemia_mapping[thalassemia]  # Map to encoded value
    }

    features = pd.DataFrame(data, index=[0])
    return features


# Get user input
user_input = user_input_features()

# Display user input
st.subheader("User Input")
st.write(user_input)

# Prediction button
if st.sidebar.button("Predict"):
    try:
        # Prediction
        prediction = model.predict(user_input)
        prediction_proba = model.predict_proba(user_input)

        # Display the prediction
        st.subheader("Prediction")
        st.write("Heart Disease" if prediction[0] == 1 else "No Heart Disease")

        st.subheader("Prediction Probability")
        st.write(f"Probability of Heart Disease: {prediction_proba[0][1]:.2%}")
        st.write(f"Probability of No Heart Disease: {prediction_proba[0][0]:.2%}")

    except Exception as e:
        st.error(f"Error making predictions: {e}")

# Footer
st.sidebar.write("Built with Streamlit")
