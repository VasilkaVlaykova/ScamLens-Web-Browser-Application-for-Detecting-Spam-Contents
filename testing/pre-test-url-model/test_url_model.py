import streamlit as st
import joblib
import re
import plotly.graph_objects as go


url_model = joblib.load('models/url_svm_model.pkl')
url_vectorizer = joblib.load('models/url_tfidf.pkl')

st.title('URL Model Pre-Testing')

url_text = st.text_area('Please enter or copy an URL')

def extract_urls(text):
    return re.findall(r'https?://\S+|www\.\S+',text)

if st.button('Test URL'):
    if url_text.strip()=="":
        st.warning('Please enter or copy an URL')
    else:
        
        
      

        
        urls = extract_urls(url_text)
        url_prediction = None

        if urls:
            url_vector = url_vectorizer.transform([url_text])
            url_prediction = url_model.predict(url_vector)[0]
        
        st.write("SMS model prediction:", url_prediction)
        st.write("Detected URL:", urls if urls else "No URL found")
        st.write("URL model prediction:", url_prediction if url_prediction is not None else "Not tested")

        if url_prediction ==1:
            st.error('Final Prediction: Spam')
        elif url_prediction == 1:
            st.error('Final Prediction: Spam')
        else:
            st.success('Final Prediction: Ham')
        


