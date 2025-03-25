
import streamlit as st
import pandas as pd
import altair as alt

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('../data/labeled_events.csv', parse_dates=['date'])
    return df

df = load_data()

st.title("📊 ChainPulseAI: Token Risk Dashboard")

token_list = df['token'].unique().tolist()
selected_token = st.selectbox("Select Token", token_list)

filtered_df = df[df['token'] == selected_token]

st.subheader(f"📈 Metrics for {selected_token}")
st.write(f"Showing data from {filtered_df['date'].min().date()} to {filtered_df['date'].max().date()}")

# Altair charts
chart = alt.Chart(filtered_df).mark_line(point=True).encode(
    x='date:T',
    y=alt.Y('avg_sentiment:Q', title='Avg Sentiment'),
    tooltip=['date', 'avg_sentiment', 'volume', 'volatility', 'event_label']
).properties(title='Daily Average Sentiment').interactive()

volume_chart = alt.Chart(filtered_df).mark_bar().encode(
    x='date:T',
    y=alt.Y('volume:Q', title='Volume'),
    tooltip=['date', 'volume']
).properties(title='Transaction Volume').interactive()

vol_chart = alt.Chart(filtered_df).mark_line(color='orange').encode(
    x='date:T',
    y=alt.Y('volatility:Q', title='Volatility'),
    tooltip=['date', 'volatility']
).properties(title='Volatility').interactive()

st.altair_chart(chart, use_container_width=True)
st.altair_chart(volume_chart, use_container_width=True)
st.altair_chart(vol_chart, use_container_width=True)

# Show flagged risk events
st.subheader("⚠️ Risk Flags (Events)")
risk_events = filtered_df[filtered_df['event_label'].isin(['pump', 'dump'])]
st.dataframe(risk_events[['date', 'event_label', 'avg_sentiment', 'volume', 'volatility']])
