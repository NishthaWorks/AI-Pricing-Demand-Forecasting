import pandas as pd
import joblib

# Load model columns
model_columns = joblib.load("models/model_columns.pkl")


def preprocess_input(input_df):
    """
    Convert dashboard input into the exact format expected by the model.
    """

    # One-hot encoding
    input_df = pd.get_dummies(
        input_df,
        columns=[
            "Category",
            "Region",
            "Weather Condition",
            "Seasonality"
        ],
        drop_first=True
    )

    # Add missing columns
    for column in model_columns:
        if column not in input_df.columns:
            input_df[column] = 0

    # Keep only model columns
    input_df = input_df[model_columns]

    return input_df