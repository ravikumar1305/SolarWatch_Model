# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 17:20:01 2023

@author: Sai Ram
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle , joblib
import streamlit as st


import os

# Loading the saved model 
loaded_model = pickle.load(open("rfc.pkl", 'rb')) # rb = reading binary
std = joblib.load('std')

# Creating a function for prediction 
def fault_prediction(input_data):    
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    return(prediction)
    
    
   
def main():
    # Every good app has a title, so let's add one
    #st.title("Innodatatic")
    html_temp = """
    
    
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Fault prediction</h2>
    </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
   
   
   # Getting input data from user
    Ipv = st.text_input("IPV")
    Vpv = st.text_input("VPV")
    Vdc = st.text_input("VDC")
    ia = st.text_input("ia")
    ib = st.text_input("ib")
    ic = st.text_input("ic")
    va = st.text_input("va")
    vb = st.text_input("vb")
    vc = st.text_input("vc")
    Iabc= st.text_input("Iabc")
    If = st.text_input("if")
    Vabc= st.text_input("Vabc")
    Vf = st.text_input("vf")
    
    
    
    # Code for prediction
    fault = ''
    
  
             
    # Creating a button for prediction
    if st.button('Fault prediction'):
        fault=fault_prediction([Ipv,Vpv,Vdc,ia,ib,ic,
                                va,vb,vc,Iabc,If,Vabc,Vf])
        if fault==1:
            fault= "solar pannel is not faulty"
        else:
            fault = "solar pannel is faulty"
   
    st.info(fault)



     
    

if __name__=="__main__":
    main()