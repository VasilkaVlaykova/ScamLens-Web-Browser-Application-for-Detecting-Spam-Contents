import streamlit as st
import joblib

model = joblib.load('models\sms_svm_model.pkl')
vectorizer = joblib.load('models\sms_tfidf.pkl')

st.title('SMS Model Pre-Testing')

sms_text = st.text_area('Pleas enter or copy an SMS message')
if st.button('Test SMS'):
    if sms_text.strip()=="":
        st.warning('Please enter or copy an SMS message')
    else:
        sms_vector = vectorizer.transform([sms_text])
        prediction = model.predict(sms_vector)[0]
        if prediction ==1:
            st.error('Prediction: Spam')
        else:
            st.success('Prediction: Ham')
