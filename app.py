
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import seaborn as sns

# --- Page Config ---
st.set_page_config(page_title="ChainPulseAI Dashboard", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("btc_hourly.csv", parse_dates=['datetime'], index_col='datetime')
    return df

from tensorflow.keras.models import load_model

@st.cache_resource
def load_transformer_model():
    return load_model("transformer_model.keras")

df = load_data()
model = load_transformer_model()

import tensorflow as tf

import numpy as np
from tensorflow.keras.models import load_model

# Load model and test data
model = load_model("transformer_model.keras")
X_test = np.load("X_test.npy"

# Enable dropout at inference by setting training=True
def predict_mc_dropout_tf(model, X, n_iter=50):
    @tf.function
    def call_with_dropout(x):
        return model(x, training=True)

    return np.array([call_with_dropout(X).numpy() for _ in range(n_iter)])

y_dropout = predict_mc_dropout_tf(model, X_test, n_iter=50)


# --- Load Forecast Arrays ---
y_pred = np.load("y_pred_transformer.npy")         # shape: (samples, 7, features)
y_true = np.load("y_test_transformer.npy")
y_dropout = np.load("y_preds_dropout.npy")         # shape: (50, samples, 7, features)

feature_names = df.columns.tolist()
close_idx = feature_names.index("Close")
forecast_horizon = y_pred.shape[1]

# --- Title ---
st.title("📈 ChainPulseAI: BTC Multistep Forecasting Dashboard")

# --- Sidebar ---
step = st.sidebar.slider("Forecast Step (t+)", 1, forecast_horizon, 1)
show_interval = st.sidebar.checkbox("Show Prediction Intervals", value=True)
start_idx = st.sidebar.slider("Start Index", 0, len(y_pred)-100, 0)

# --- Forecast Plot (Close Price) ---
st.subheader(f"🪙 Step {step}: Close Price Forecast (USD)")

y_pred_step = y_pred[:, step-1, close_idx]
y_true_step = y_true[:, step-1, close_idx]

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(y_true_step[start_idx:start_idx+100], label="Actual", linewidth=2)
ax.plot(y_pred_step[start_idx:start_idx+100], label="Predicted", linestyle='--')

if show_interval:
    interval_samples = y_dropout[:, :, step-1, close_idx]
    lower = np.percentile(interval_samples, 5, axis=0)
    upper = np.percentile(interval_samples, 95, axis=0)
    ax.fill_between(range(100), lower[start_idx:start_idx+100], upper[start_idx:start_idx+100], alpha=0.3, color='orange', label="90% Interval")

ax.set_ylabel("Price ($)")
ax.set_xlabel("Time Step")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# --- Attention Map Placeholder ---
st.subheader("🔍 Stepwise Attention Weights")
try:
    attention_df = pd.read_csv("data/attention_stepwise.csv", index_col=0)
    st.dataframe(attention_df.style.background_gradient(axis=1, cmap='viridis'))
except:
    st.warning("⚠️ Attention data not found. Please export `attention_stepwise.csv` first.")

# --- Metrics Table Placeholder ---
st.subheader("📊 Forecast Evaluation (MAE / RMSE)")
try:
    metrics_df = pd.read_csv("data/forecast_metrics.csv", index_col=0)
    st.dataframe(metrics_df.style.format("{:.2f}").background_gradient(axis=0, cmap='Blues'))
except:
    st.warning("⚠️ Forecast metrics not found. Please export `forecast_metrics.csv` first.")
