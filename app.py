import pickle
import streamlit as st
import numpy as np
import pandas as pd

with open('knn_model.pkl','rb') as f:
    model = pickle.load(f)

st.title('Affected Population in Disasters')






latitude = int(st.number_input('latitude',value=00.00))
longitude = int(st.number_input('longitude',value=00.00))
severity_level = int(st.number_input('severity_level',value=00.00))
affected_population = st.number_input("Affected Population", min_value=00.00)
estimated_economic_loss_usd   = int(st.number_input('estimated_economic_loss_usd',value=00.00))
response_time_hours = int(st.number_input('response_time_hours',value=00.00))
infrastructure_damage_index = int(st.number_input('infrastructure_damage_index',value=00.00))
is_major_disaster = int(st.number_input('is_major_disaster',value=00.00))

if st.button('affected_population % '):


    input_df = pd.DataFrame([{
        'latitude':latitude,
        'longitude':longitude,
        'severity_level':severity_level,
        'affected_population':affected_population,
        'estimated_economic_loss_usd':estimated_economic_loss_usd,
        'response_time_hours':response_time_hours,
        'infrastructure_damage_index':infrastructure_damage_index,
        'is_major_disaster':is_major_disaster
    }])


    result = model.predict(input_df)[0]

    st.success(f'affected_population % :{result:.2f}')
