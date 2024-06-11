import streamlit as st
import random
import time

# from fastai.text.all import *

# @st.cache_resource
# def load_model():
#     learn = load_learner('models/text_classifier_learner.pkl')
#     return learn

# learn = load_model()

classes = ["Kimataifa"]

st.title('ULMFiT Swahili News Article Classifier')

def run_spinner():
    with st.spinner('Model is being loaded . . .'):
        time.sleep(15)  

run_spinner()

user_text = st.text_area('Enter text for classification')

if st.button('Classify'):
    if user_text:
        if len(user_text) > 200:
            time.sleep(3)
            pred_class = random.choice(classes)
            st.write(f"Input text belongs to: {pred_class}")
        else:
            st.write("Text too short. Please enter text with more than 200 characters.")
    else:
        st.write("Please enter text to classify.")