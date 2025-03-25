
# 🚀 Deploying ChainPulseAI on Render

## 🔧 Requirements

- PostgreSQL database provisioned on Render
- Environment variables:
  - `DATABASE_URL=postgresql://<username>:<password>@<host>:5432/chainpulse`

---

## 🧱 Folder Structure

```
📁 chainpulse-ai/
├── app/                       # Streamlit app
├── api/                       # FastAPI backend
├── data/                      # (optional) for local runs
├── scripts/                   # PostgreSQL migration
├── models/                    # ML models
├── notebooks/                 # Jupyter notebooks
├── Dockerfile
├── start.sh
├── requirements.txt
└── Procfile
```

---

## ▶️ One-Click Deploy to Render

1. Push this repo to GitHub
2. Create a new Render Web Service:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `sh start.sh`
   - **Port**: `8501`
   - Set environment variable: `DATABASE_URL`

3. Set up a separate **PostgreSQL database** from Render dashboard

4. Run `scripts/migrate_to_postgres.py` locally to upload your dataset

---

You’ll have both:
- 🔮 Streamlit on `https://your-app.onrender.com`
- ⚡ FastAPI on `https://your-app.onrender.com:8000/docs`
