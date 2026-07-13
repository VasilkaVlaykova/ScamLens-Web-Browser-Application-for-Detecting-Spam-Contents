import streamlit as st
import joblib
import plotly.graph_objects as go 
import re
import unicodedata
from confusable_homoglyphs import confusables








email_model = joblib.load('models/email_svm_model.pkl')
email_vectoriser = joblib.load('models/email_tfidf.pkl')
url_model = joblib.load('models/url_svm_model.pkl')
url_vectorizer = joblib.load('models/url_tfidf.pkl')

tab1, tab2, tab3 =st.tabs(['SMS','Email','URL'])

import plotly.graph_objects as go

def probability_gauge(value, label):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = value,
        title = {'text': label},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "red" if label == "Spam Probability" else "green"},
            'steps': [
                {'range': [0, 50], 'color': '#d4f7d4'},
                {'range': [50, 80], 'color': '#fff3cd'},
                {'range': [80, 100], 'color': '#f8d7da'}
            ]
        }
    ))
    return fig


with tab1:
    st.title('SMS')
    sms_text = st.text_area('Please enter or copy an SMS message')

    if st.button('Analyse SMS'):
        if sms_text.strip() == "":
            st.warning('Please enter or copy an SMS message')
        else:
            
            sms_vector = email_vectoriser.transform([sms_text])
            sms_prediction = email_model.predict(sms_vector)[0]
            sms_probability = email_model.predict_proba(sms_vector)[0]

            ham_sms_probability = sms_probability[0] * 100
            spam_sms_probability = sms_probability[1] * 100

            
            st.subheader("SMS Classification")

            if sms_prediction == 1:
               st.write("Prediction: **Spam**")
               st.plotly_chart(probability_gauge(spam_sms_probability, "Spam Probability"))
            else:
               st.write("Prediction: **Legitimate text**")
               st.plotly_chart(probability_gauge(ham_sms_probability, "Ham Probability"))

            
            
         

            urls = re.findall(r'(https?://[^\s]+|www\.[^\s]+)', sms_text)

        
            if urls:
                st.subheader("URL Analysis")

                
                for url in urls:
                    

                    url_vector = url_vectorizer.transform([url])
                    url_prediction = url_model.predict(url_vector)[0]

                

                    

                    for url in urls:
                      st.write(f"DEBUG raw url: {repr(url)}")   # shows exact characters, including invisible ones
                      security = analyze_hidden_things(url)
                      st.write(f"DEBUG result: {security}")


                    url_probability = url_model.predict_proba(url_vector)[0]

                    ham_url_probability = url_probability[0] * 100
                    spam_url_probability = url_probability[1] * 100

                    st.write(f"URL: {url}")
                    if url_prediction == 1:
                       st.write("Prediction: **Spam**")
                       st.write(f"Spam probability: **{spam_url_probability:.2f}%**")
                    else:
                       st.write("Prediction: **Legitimate URL**")
                       st.write(f"Ham probability: **{ham_url_probability:.2f}%**")

            else:
                st.info("No URLs found in this SMS.")
                if sms_prediction == 1:
                   st.warning(
                    "⚠️ This message appears to be **spam** and may contain **hidden malicious links** "
                    "behind buttons or words. Do **NOT** click anywhere in the original email or SMS."
                   )


with tab2:
    st.title('Email')   
    email_text = st.text_area('Please enter or copy an Email message')
    if st.button('Analyse Email'):
        if email_text.strip()=="":
            st.warning('Please enter or copy an Email message')
        else:
            email_vector = email_vectoriser.transform([email_text])
            email_prediction = email_model.predict(email_vector)[0]
            email_probability = email_model.predict_proba(email_vector)[0]
            ham_email_probability = email_probability[0]*100
            spam_email_probability = email_probability[1]*100

            st.subheader("Email Classification")
            if email_prediction == 1:
               st.write("Prediction: **Spam**")
               st.plotly_chart(probability_gauge(spam_email_probability, "Spam Probability"))
            else:
               st.write("Prediction: **Legitimate text**")
               st.plotly_chart(probability_gauge(ham_email_probability, "Ham Probability"))

            
            
            urls = re.findall(r'(https?://[^\s]+|www\.[^\s]+)', email_text)


           
            if urls:
                 st.subheader("URL Analysis")
                 for url in urls:

                   url_vector = url_vectorizer.transform([email_text])
                   url_prediction = url_model.predict(url_vector)[0]
                   url_probability = url_model.predict_proba(url_vector)[0]
                   ham_url_probability = url_probability[0]*100
                   spam_url_probability = url_probability[1]*100

                   st.write(f"URL: {url}")
                   if url_prediction == 1:
                      st.write("Prediction: **Spam**")
                      st.write(f"Spam probability: **{spam_url_probability:.2f}%**")
                   else:
                      st.write("Prediction: **Legitimate URL**")
                      st.write(f"Ham probability: **{ham_url_probability:.2f}%**")
            else:
                st.info("No URLs found in this Email.")
                if email_prediction == 1:
                   st.warning(
                   "⚠️ This message appears to be **spam** and may contain **hidden malicious links** "
                   "behind buttons or words. Do **NOT** click anywhere in the original email or SMS."
                   )



with tab3:       
    st.title('URL')     
    url_text = st.text_area('Please enter or copy a URL')   
    if st.button('Analyse URL'):
        if url_text.strip()=="":
            st.warning('Please enter or copy a URL')
        else:
            
            
            urls = re.findall(r'(https?://[^\s]+|www\.[^\s]+)', url_text)
            if urls:
                url_vector = url_vectorizer.transform([url_text])
                url_prediction = url_model.predict(url_vector)[0]
                url_probability = url_model.predict_proba(url_vector)[0]
                ham_url_probability = url_probability[0]*100
                spam_url_probability = url_probability[1]*100

                st.write(f"URL: {urls}")
                if url_prediction == 1:
                   st.write("Prediction: **Spam**")
                   st.plotly_chart(probability_gauge(spam_url_probability, "Spam Probability"))
                else:
                   st.write("Prediction: **Legitimate URL**")
                   if url_prediction == 1:
                      st.write("Prediction: **Spam**")
                      st.plotly_chart(probability_gauge(spam_url_probability, "Spam Probability"))
                   else:
                      st.write("Prediction: **Legitimate URL**")
                      st.plotly_chart(probability_gauge(ham_url_probability, "Ham Probability"))