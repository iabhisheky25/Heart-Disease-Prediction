# Heart Disease Prediction App

A simple Streamlit app that predicts the risk of heart disease using a pre-trained Decision Tree model.

## Features

- User-friendly interface to input medical information
- Predicts whether a person is at risk of heart disease
- Displays prediction probabilities

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/2003saurabh/heart-disease-prediction-app.git
   cd heart-disease-prediction-app
2. **Create a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For Windows: `.venv\Scripts\activate`
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
5. **Run the app**:
   ```bash
   streamlit run app.py

## Model
The model is a Decision Tree Classifier trained on the UCI Heart Disease dataset. It takes input features like age, gender, blood pressure, cholesterol, etc., and predicts the likelihood of heart disease.

## Dependencies
1. Python 3.x
2. Streamlit
3. scikit-learn
4. Pandas
5. joblib

## License
License



