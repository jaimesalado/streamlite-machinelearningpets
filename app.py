import streamlit as st
import pandas as pd
import joblib

# titulo

st.header("Streamlit Machine Learning App Pets")

# input bar 1

height = st.number_input("enter height:")
weight = st.number_input("enter weight:")
eyes = st.selectbox("selecc eye colour",("Blue","Brown"))

if st.button("submit"):
    pet_model = joblid.load("pet_model.pkl")
    X = pd.DataFrame([[height,weight,eyes]], columns = ["height","weight","eyes"])
    X = X.replace(["brown","blue"], [1,0])
    
    prediction = pet_model.predict(X)[0]

    st.text(f"esta instancia es{prediction}")

