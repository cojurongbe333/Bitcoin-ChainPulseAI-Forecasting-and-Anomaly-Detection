
import pandas as pd
from db_config import engine

# Load the enhanced CSV
df = pd.read_csv('../data/labeled_events_enhanced.csv', parse_dates=['date'])

# Save to PostgreSQL (replace if exists)
df.to_sql('crypto_metrics', engine, if_exists='replace', index=False)

print("✅ Data migrated to PostgreSQL table 'crypto_metrics'")
