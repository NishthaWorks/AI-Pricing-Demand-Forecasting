import shap
import joblib
import pandas as pd

model = joblib.load("models/demand_forecast_model.pkl")


def get_feature_importance(X):

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X)

    importance = pd.DataFrame({

        "Feature": X.columns,

        "Importance": abs(shap_values).mean(axis=0)

    })

    importance = importance.sort_values(

        "Importance",

        ascending=False

    )

    return importance