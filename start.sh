#!/bin/bash
# Start both the Streamlit dashboard and FastAPI backend

# Start FastAPI in background
uvicorn api.fastapi_backend:app --host 0.0.0.0 --port 8000 &

# Start Streamlit on port 8501
streamlit run app/streamlit_dashboard_postgres.py --server.port=8501 --server.address=0.0.0.0
