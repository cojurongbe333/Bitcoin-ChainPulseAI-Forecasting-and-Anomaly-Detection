
# 🔮 ChainPulseAI

**Real-Time Crypto Sentiment + On-Chain Risk Detection**

ChainPulseAI combines social media sentiment and on-chain activity to build a predictive crypto risk scoring engine.

---

## 🧠 Project Workflow

1️⃣ **Tweet Sentiment Analysis**  
→ Preprocess tweets using VADER  
→ Compute daily average sentiment per token  
📄 [`01_sentiment_processing.ipynb`](notebooks/01_sentiment_processing.ipynb)

2️⃣ **On-Chain Transaction Monitoring**  
→ Detect spikes and whale/bot behavior  
📄 [`02_onchain_analysis.ipynb`](notebooks/02_onchain_analysis.ipynb)

3️⃣ **Merge with Market Data**  
→ Calculate volatility, candlestick patterns  
📄 [`03_merge_and_volatility.ipynb`](notebooks/03_merge_and_volatility.ipynb)

4️⃣ **Label Events**  
→ Tag spikes, dips, pump/dumps  
📄 [`04_event_labeling.ipynb`](notebooks/04_event_labeling.ipynb)

5️⃣ **Train ML Model**  
→ Predict “Risk score” or event category  
→ Includes SHAP explainability  
📄 [`05_model_training.ipynb`](notebooks/05_model_training.ipynb)

6️⃣ **Streamlit Dashboard**  
→ Visualize sentiment, volume, risk alerts  
🖥️ [`streamlit_dashboard.py`](app/streamlit_dashboard.py)

7️⃣ **FastAPI Backend (Optional)**  
→ Serve real-time model predictions  
🌐 [`fastapi_backend.py`](api/fastapi_backend.py)

---

## 🧱 Tech Stack

| Layer       | Tools |
|-------------|-------|
| Data        | CoinGecko, Twitter API, Etherscan |
| Processing  | Python, Pandas, NLTK, Scikit-learn |
| Modeling    | Random Forest, SHAP |
| Storage     | CSV / SQLite (dev), PostgreSQL (prod) |
| Dashboard   | Streamlit + Altair |
| API         | FastAPI |
| Deployment  | Docker + Docker Compose |

---

## 🚀 Running Locally

```bash
# Build and run Streamlit + FastAPI
docker-compose up --build
```

Access:

- Streamlit: [http://localhost:8501](http://localhost:8501)
- FastAPI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📂 Project Structure

```
chainpulse-ai/
├── data/
│   ├── raw_tweets.csv
│   ├── onchain_tx.csv
│   ├── merged_market_data.csv
│   └── labeled_events.csv
├── notebooks/
│   ├── 01_sentiment_processing.ipynb
│   ├── 02_onchain_analysis.ipynb
│   ├── 03_merge_and_volatility.ipynb
│   ├── 04_event_labeling.ipynb
│   └── 05_model_training.ipynb
├── models/
│   └── risk_model.pkl
├── app/
│   └── streamlit_dashboard.py
├── api/
│   └── fastapi_backend.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 📬 Contact

For questions, collabs, or contributions — feel free to open an issue or reach out!
