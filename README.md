# 📈 ChainPulseAI: Bitcoin Forecasting and Anomaly Detection

**Enhanced Streamlit App + GRU/Transformer Forecasting + Anomaly Evaluation**
**Build in Progress**
---

## 🔍 Project Overview
This project builds a complete short-term Bitcoin price forecasting and anomaly detection system using:

- GRU (tuned via Optuna)
- Transformer model (tuned)
- Streamlit frontend with Docker deployment
- Anomaly detection and precision/recall evaluation with labeled data
- Post-forecast anomaly classification using XGBoost with CV evaluation

---

## 🚀 Features (Post-Enhancement)

### ✅ Forecasting
- Hourly Bitcoin Close Price resampled and scaled.
- Sequence modeling using:
  - 📊 **GRU (Initial + Tuned with Optuna)**
  - 🧠 **Transformer Model (Tuned with Attention, retained only if accurate)**
- Full evaluation using:
  - MAE, RMSE
  - Visual plots of Actual vs Predicted

### ✅ Deployment
- Fully functional **Streamlit App** for real-time forecasting.
- Dockerized app with `Dockerfile` and easy deployment instructions.

### ✅ Anomaly Detection + Classification
- Residual-based anomaly detection using dynamic thresholds.
- Labeled anomalies evaluation using `True_Anomaly` values.
- Precision, Recall, and F1 score computed.
- Post-anomaly classification using:
  - 🔍 **XGBoost** with Stratified K-Fold CV
  - Aggregate confusion matrix
  - Average classification reports

### ✅ File Exports
- Forecast results exported to `forecast_results.csv`
- Anomaly detection exported to `anomalies_detected.csv`
- Evaluation reports in `anomaly_eval_with_labels.xls`
- Enhanced notebooks: hourly and daily forecasting versions

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
│   ├── labeled_anomalies.csv # Ground-truth anomalies (to be regenerated)
│   └── anomaly_eval_with_labels.xls
├── notebooks/
│   ├── ChainPulse_Hourly_Forecasting_Unified.ipynb  # Hourly version (master)
│   ├── 08a_BTC_Forecasting_Daily.ipynb               # Daily forecasting version
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
- ✅ Implement Transformer + GRU hybrid if it improves accuracy
- ✅ Add auto retraining from updated data
- ✅ Deploy to cloud (e.g., GCP, AWS)

---

## 🙌 Credits
- Data: [Kaggle BTC-USD Minute Data](https://www.kaggle.com)
- Libraries: TensorFlow, Scikit-learn, Pandas, Streamlit, Optuna, XGBoost
- Author: Chantal Ojurongbe

---

**Let ChainPulseAI guide your next crypto move 📊⚡**
