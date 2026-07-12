import streamlit as st
import joblib
import re
import plotly.graph_objects as go

sms_model =joblib.load('models/email_svm_model.pkl')
sms_vectorizer = joblib.load('models/email_tfidf.pkl')

url_model = joblib.load('models/url_svm_model.pkl')
url_vectorizer = joblib.load('models/url_tfidf.pkl')

st.title('SMS and URL Model Pre-Testing')

sms_text = st.text_area('Please enter or copy an SMS message')

def extract_urls(text):
    return re.findall(r'https?://\S+|www\.\S+',text)

if st.button('Test SMS'):
    if sms_text.strip()=="":
        st.warning('Please enter or copy an SMS message')
    else:
        sms_vector = sms_vectorizer.transform([sms_text])
        sms_prediction = sms_model.predict(sms_vector)[0]
        
        sms_prediction = sms_model.predict(sms_vector)[0]

        
      

        
        urls = extract_urls(sms_text)
        url_prediction = None

        if urls:
            url_vector = url_vectorizer.transform([sms_text])
            url_prediction = url_model.predict(url_vector)[0]
        
        st.write("SMS model prediction:", sms_prediction)
        st.write("Detected URL:", urls if urls else "No URL found")
        st.write("URL model prediction:", url_prediction if url_prediction is not None else "Not tested")

        if sms_prediction ==1:
            st.error('Final Prediction: Spam')
        elif url_prediction == 1:
            st.error('Final Prediction: Spam')
        else:
            st.success('Final Prediction: Ham')
        if sms_prediction == 1:
            st.error("🚫 **Spam Detected** — this message shows suspicious patterns.")
        else:
            st.success("✅ **Legitimate** — no significant spam indicators found.")


