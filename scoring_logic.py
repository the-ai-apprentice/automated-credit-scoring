import joblib
import numpy as np
import pandas as pd

data = joblib.load("artifacts/risk_model_data.joblib")


def preprocess_data(df):
    # engineering features
    df["loan_to_income"] = round(df.loan_amount / df.income, 2)
    df["delinquency_ratio"] = (df.delinquent_months * 100 / df.loan_tenure_months).round(1)
    df["average_dpd_per_delinquency"] = np.where(
        df.delinquent_months != 0,
        (df.total_dpd / df.delinquent_months).round(1),
        0
    )

    # drop operational columns
    x = df.drop(["cust_id", "loan_id"], axis="columns", errors="ignore")
    x = x.drop(data["cols_to_drop"], axis="columns")

    # scale numerical features
    x[data["cols_to_scale"]] = data["scaler"].transform(x[data["cols_to_scale"]])

    # drop redundant features identified by VIF analysis
    x = x.drop(data["features_to_drop_vif"], axis="columns")

    # filter for highly predictive features based on IV
    x_reduced = x[data["selected_features_iv"]].copy()

    # apply one-hot encoding to categorical columns
    dummy_encoded_array = data["categorical_encoder"].transform(x_reduced[data["cat_cols"]])
    dummy_encoded_df = pd.DataFrame(
        dummy_encoded_array,
        columns=data["train_encoded_cols"],
        index=x_reduced.index
    )

    # concat encoded features to create the final prediction ready dataframe
    x_processed = pd.concat(
        [x_reduced.drop(columns=data["cat_cols"], axis="columns"), dummy_encoded_df],
        axis=1
    )

    return x_processed


def predict_risk(input_dict):
    cleaned_dict = {}
    for key, value in input_dict.items():
        if isinstance(value, list):
            cleaned_dict[key] = value[0]
        else:
            cleaned_dict[key] = value
    # Fix: Wrap input_dict in a list to prevent scalar value error
    input_df = pd.DataFrame([cleaned_dict])
    x_processed = preprocess_data(input_df)

    # Fix: Access dictionary using bracket notation
    model = data["best model"]
    base_score = 300
    scale_length = 600
    limits = [300, 500, 650, 750, 900]
    rate = ["Poor", "Average", "Good", "Excellent"]
    rating = None

    prediction_probability = model.predict_proba(x_processed)
    default_probability = prediction_probability[0,1]
    non_default_probability = prediction_probability[0,0]

    credit_score = base_score + non_default_probability * scale_length
    for i in range(len(limits)-1):
        if limits[i] <= credit_score < limits[i+1]:
            rating = rate[i]
            break

    return default_probability, credit_score, rating