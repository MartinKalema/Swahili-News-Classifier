import streamlit as st
from fastai.text.all import *

@st.cache_resource
def load_model():
    with st.spinner('Model is being loaded...'):
        learn = load_learner('models/text_classifier_model.pkl')
    return learn

st.title('ULMFiT Swahili News Article Classifier')

st.markdown("""
ULMFiT (Universal Language Model Fine-tuning) is an effective transfer learning method for NLP tasks.
""")

user_text = st.text_area('Enter text for classification')

if st.button('Classify'):
    if user_text:
        pred_class, pred_idx, outputs = learn.predict(user_text)
        st.write(f"Input text belongs to: {pred_class}")
    else:
        st.write("Please enter text to classify.")