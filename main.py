import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("anushka.pkl" , "rb"))

st.header("Online Payment Fraud Detection")
st.image("fraud detection.jpg")

Type = st.number_input("Type")
Amount = st.number_input("Amount")
Oldbalorg = st.number_input("Old Balance Org")
Newbalanceorig = st.number_input("New Balance Orig")


if st.button("Submit"):
    st.balloons()
    features = np.array([[Type , Amount , Oldbalorg , Newbalanceorig]])
    result = model.predict(features)
    st.header(result[0])

