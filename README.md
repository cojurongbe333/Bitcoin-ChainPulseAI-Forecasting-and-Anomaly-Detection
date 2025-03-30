# 📈 ChainPulseAI: Bitcoin Forecasting and Anomaly Detection

**Enhanced Streamlit App + GRU/Transformer Forecasting + Anomaly Evaluation**

---

## 🔍 Project Overview
This project builds a complete short-term Bitcoin price forecasting and anomaly detection system using:

- GRU (tuned via Optuna)
- Transformer model (tuned)
- Streamlit frontend with Docker deployment
- Anomaly detection and precision/recall evaluation with labeled data

---

## 🚀 Features (Post-Enhancement)

### ✅ Forecasting
- Hourly Bitcoin Close Price resampled and scaled.
- Sequence modeling using:
  - 📊 **GRU (Initial + Tuned with Optuna)**
  - 🧠 **Transformer Model (Tuned with Attention)**
- Full evaluation using:
  - MAE, RMSE
  - Visual plots of Actual vs Predicted

### ✅ Deployment
- Fully functional **Streamlit App** for real-time forecasting.
- Dockerized app with `Dockerfile` and easy deployment instructions.

### ✅ Anomaly Detection
- Residual-based anomaly detection using dynamic thresholds.
- Labeled anomalies comparison with:
  - `True_Anomaly` from ground-truth dataset.
  - Detected anomaly points.
- Evaluation metrics:
  - Precision, Recall, F1 Score.
  - Scatter plot with true vs detected anomalies.

### ✅ File Exports
- Forecast results exported to `forecast_results.csv`
- Anomaly detection exported to `anomalies_detected.csv`
- Evaluation reports in `anomaly_eval_with_labels.xls`

---

## 📂 File Structure

```bash
├── app/
│   ├── app.py                 # Streamlit app
│   ├── model_gru_tuned.h5     # Tuned GRU model
│   ├── Dockerfile             # Docker config
│   └── requirements.txt       # Python dependencies
├── data/
│   ├── btcusd_1-min_data.csv  # Raw 1-minute BTC data
│   ├── forecast_results.csv   # Model predictions
│   ├── labeled_anomalies.csv # Ground-truth anomalies
│   └── anomaly_eval_with_labels.xls
├── notebooks/
│   ├── bitcoin_forecasting.ipynb  # Final enhanced notebook
├── README.md
```

---

## 🧪 Models Performance (Summary)

| Model         | MAE     | RMSE   |
|---------------|---------|--------|
| Prophet       | 56.06   | 63.32  |
| ARIMA         | 40.94   | 52.63  |
| LSTM          | 50.79   | 51.40  |
| GRU (Initial) | 18.60   | 20.10  |
| GRU (Tuned)   | **8.14** | **17.77** |
| Transformer   | 379.79  | 381.32 |

> 🔥 GRU (Tuned) performed best in both MAE and RMSE.

---

## 🐳 Streamlit + Docker Usage

### 1. Clone the repo
```bash
git clone https://github.com/yourname/chainpulseai.git
cd chainpulseai/app
```

### 2. Build the Docker image
```bash
docker build -t chainpulseai .
```

### 3. Run the container
```bash
docker run -p 8501:8501 chainpulseai
```

### 4. Access the app
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧠 Future Enhancements
- ✅ Add real-time streaming pipeline
- ✅ Implement Transformer + GRU hybrid
- ✅ Add auto retraining from updated data
- ✅ Deploy to cloud (e.g., GCP, AWS)

---

## 🙌 Credits
- Data: [Kaggle BTC-USD Minute Data](https://www.kaggle.com)
- Libraries: TensorFlow, Scikit-learn, Pandas, Streamlit, Optuna

---
