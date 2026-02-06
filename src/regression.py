import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def fit_regression(df, axis):
    X = df["seconds_from_start"].values.reshape(-1, 1)
    y = df[axis].values

    model = LinearRegression()
    model.fit(X, y)

    predictions = model.predict(X)
    residuals = y - predictions

    return model, predictions, residuals