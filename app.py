import streamlit as st
from fastai.text.all import *

@st.cache_resource
def load_model():
    learn = load_learner('text_classifier_learner.pth')
    return learn

learn = load_model()

# Streamlit app
st.title('ULMFiT Swahili News Article Classifier')

# Text input
user_text = st.text_area('Enter text for classification')

if st.button('Classify'):
    if user_text:
        pred_class, pred_idx, outputs = learn.predict(user_text)
        st.write(f"Predicted Class: {pred_class}")
    else:
        st.write("Please enter text to classify.")

if __name__ == '__main__':
    st.run()
