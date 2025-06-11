import streamlit as st, pandas as pd
st.title("Breakout Radar v0.1 – Irish Emerging Artists")

df = pd.read_csv("latest_metrics.csv")
st.dataframe(df.sort_values("followers_delta_%", ascending=False),
             use_container_width=True)

st.bar_chart(df.set_index("artist")["followers_delta_%"])
