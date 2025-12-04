import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"MSE: {mse}")
    print(f"R2: {r2}")
    
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.show()
    
    return mse, r2

def plot_residuals(model, X_test, y_test):
    y_pred = model.predict(X_test)
    residuals = y_test - y_pred
    plt.figure(figsize=(6,4))
    plt.scatter(y_pred, residuals, alpha=0.5)
    plt.axhline(0, color="red")
    plt.title("Residuals vs Predictions")
    plt.xlabel("Predictions")
    plt.ylabel("Residuals")
    plt.show()

def shap_explain(model, X_test):
    explainer = shap.Explainer(model.predict, X_test)
    shap_values = explainer(X_test)
    shap.summary_plot(shap_values, X_test)
