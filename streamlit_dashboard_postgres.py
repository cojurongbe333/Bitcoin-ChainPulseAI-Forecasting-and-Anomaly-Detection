
import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime
from sqlalchemy import create_engine

st.set_page_config(page_title="ChainPulseAI Dashboard", layout="wide")

# PostgreSQL connection
DATABASE_URL = "postgresql://username:password@localhost:5432/chainpulse"  # Replace with your creds
engine = create_engine(DATABASE_URL)

# Load from PostgreSQL
@st.cache_data(ttl=60)
def load_data():
    query = "SELECT * FROM crypto_metrics"
    df = pd.read_sql(query, engine, parse_dates=['date'])
    return df

df = load_data()
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

st.title("🔮 ChainPulseAI: Live Crypto Risk Dashboard (PostgreSQL)")
st.markdown(f"⏱️ Last updated: `{current_time}` — Pulls directly from database")

# Sidebar filtering
tokens = df['token'].unique().tolist()
selected_tokens = st.multiselect("Select Token(s)", tokens, default=tokens[:2])
start_date = st.date_input("Start Date", value=df['date'].min())
end_date = st.date_input("End Date", value=df['date'].max())

# Filter dataset
filtered_df = df[
    (df['token'].isin(selected_tokens)) &
    (df['date'] >= pd.to_datetime(start_date)) &
    (df['date'] <= pd.to_datetime(end_date))
]

st.markdown(f"Showing **{len(filtered_df)}** records from {start_date} to {end_date}")

# Token selector
for token in selected_tokens:
    token_df = filtered_df[filtered_df['token'] == token]

    st.subheader(f"📈 {token} Metrics")

    # Risk score trend (event encoded)
    token_df['event_score'] = token_df['event_label'].map({
        'neutral': 0,
        'spike': 1,
        'dip': -1,
        'pump': 2,
        'dump': -2
    })

    chart = alt.Chart(token_df).mark_line(point=True).encode(
        x='date:T',
        y='event_score:Q',
        tooltip=['date', 'event_label']
    ).properties(title='Risk Trend').interactive()

    sentiment_chart = alt.Chart(token_df).mark_line().encode(
        x='date:T',
        y='avg_sentiment:Q',
        tooltip=['avg_sentiment']
    ).properties(title='Avg Sentiment Over Time').interactive()

    volume_chart = alt.Chart(token_df).mark_bar().encode(
        x='date:T',
        y='volume:Q'
    ).properties(title='Transaction Volume').interactive()

    volatility_chart = alt.Chart(token_df).mark_line(color='orange').encode(
        x='date:T',
        y='volatility:Q'
    ).properties(title='Volatility').interactive()

    st.altair_chart(chart, use_container_width=True)
    st.altair_chart(sentiment_chart, use_container_width=True)
    st.altair_chart(volume_chart, use_container_width=True)
    st.altair_chart(volatility_chart, use_container_width=True)

    with st.expander("⚠️ View Risk Events"):
        risk_events = token_df[token_df['event_label'].isin(['pump', 'dump'])]
        st.dataframe(risk_events[['date', 'event_label', 'avg_sentiment', 'volume', 'volatility']])
