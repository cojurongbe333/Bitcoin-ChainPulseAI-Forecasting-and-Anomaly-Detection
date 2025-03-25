
# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command (override with Compose)
CMD ["streamlit", "run", "app/streamlit_dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
