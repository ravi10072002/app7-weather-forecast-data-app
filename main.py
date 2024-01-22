import streamlit as st
import plotly.express as px
st.title("weather forecast for the next days")
place=st.text_input("place: ")
days=st.slider("forecast days",min_value=1,max_value=5,
               help="select the number of forecasted days")
option=st.selectbox("select data to view",
                    ("temprature","sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):

    dates=["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures=[10, 11, 15]
    temperatures=[days*i for i in temperatures]
    return dates,temperatures

d, t=get_data(days)


figure=px.line(x=d, y=t, labels={"x":"date", "y":"temperature (c)"})
st.plotly_chart(figure)