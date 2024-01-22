import streamlit as st

st.title("weather forecast for the next days")
place=st.text_input("place: ")
days=st.slider("forecast days",min_value=1,max_value=5,
               help="select the number of forecasted days")
option=st.selectbox("select data to view",
                    ("temprature","sky"))
st.subheader(f"{option} for the next {days} days in {place}")
