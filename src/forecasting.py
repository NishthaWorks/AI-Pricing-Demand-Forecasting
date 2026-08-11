import joblib

from src.preprocessing import preprocess_input

# Load trained model
model = joblib.load("models/demand_forecast_model.pkl")


def predict_demand(input_df):

    processed_data = preprocess_input(input_df)

    prediction = model.predict(processed_data)

    return prediction[0]