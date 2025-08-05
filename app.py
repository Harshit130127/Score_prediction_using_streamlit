import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title='Student Exam Score Predictor', layout='centered')

st.title('Student Exam Score Predictor')
st.write('Input student details to predict their expected exam score using the trained model.')

# Load model
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.sidebar.header('Student Parameters')

hours_studied = st.sidebar.slider('Hours Studied', 0, 10, 5)
previous_score = st.sidebar.slider('Previous Exam Score', 0, 100, 70)
extracurricular = st.sidebar.selectbox('Extracurricular Activities', ['No', 'Yes'])
sleep_hours = st.sidebar.slider('Sleep Hours', 0, 12, 7)
papers_practiced = st.sidebar.slider('Sample Question Papers Practiced', 0, 10, 3)

# input DataFrame
input_df = pd.DataFrame({
    'Hours Studied': [hours_studied],
    'Previous Scores': [previous_score],
    'Extracurricular Activities': [extracurricular],
    'Sleep Hours': [sleep_hours],
    'Sample Question Papers Practiced': [papers_practiced]
})

if st.button('Predict'):
    prediction = model.predict(input_df)[0]
    st.success(f'📚 Predicted Exam Score: {prediction:.2f}')
