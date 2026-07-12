import streamlit as st
import joblib
import plotly.graph_objects as go 
import re

st.markdown("""
<style>
[data-testid="stToolbar"] {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}
</style>
""", unsafe_allow_html=True)



st.title('Welcome to ScamLens ',text_alignment='center' )
st.write('A detection platform designed to analyse text messages, emails, and URLs for potential threats. ' \
'Simply input your        data to scan for spam content and receive an instant ' \
'                  probability score for the risk level')


st.markdown(
    """
    <div style='background-color: #fbc02d; color: black; padding: 1rem; border-radius: 0.5rem; font-size: 0.85rem; margin-bottom: 0.5rem;'>
    ⚠️ Please do not input any sensitive information such as name, address, phone number, or your personal email address. The platform will analyse your content without storing any data.
    </div>
    """,
    unsafe_allow_html=True
)


email_model = joblib.load('models/email_svm_model.pkl')
email_vectoriser = joblib.load('models/email_tfidf.pkl')
url_model = joblib.load('models/url_svm_model.pkl')
url_vectorizer = joblib.load('models/url_tfidf.pkl')

tab1, tab2, tab3 = st.tabs(['SMS', 'Email','URL'])

def chart(value, label):
    fig = go.Figure(go.Indicator(
        mode='gauge+number',
        value = value,
        number={'suffix': '%', 'valueformat': '.2f'},
        title ={'text': label},
        gauge= {
            'axis':{'range':[0,100]},
            'bar':{'color': 'red' if label == 'Spam Probability' else 'green'},
            'steps':[
                {'range': [0,50], 'color': '#9abc05'},
                {'range': [50,75], 'color': '#ffc926'},
                {'range': [75,100], 'color':'#d52518'}
            ]
        }
    ))
    return fig


with tab1:
    #st.title('SMS')

    with st.form(key='sms_form', clear_on_submit=True):
        sms_text = st.text_area('Please enter or copy an SMS message')
        



 
        analyse_Sbt = st.form_submit_button('Analyse SMS', type='primary')

        if sms_text.strip()=="":
               #st.warning('Please enter or copy an SMS message')
               st.markdown(
    """
    <div style='background-color: #3c7027; color: white; padding: 1rem; border-radius: 0.5rem; font-size: 0.85rem; margin-bottom: 0.5rem;'>
    ⚠️ Please enter or copy an SMS message.
    </div>
    """,
    unsafe_allow_html=True
)
        else:
               sms_vector = email_vectoriser.transform([sms_text])
               sms_prediction = email_model.predict(sms_vector)[0]
               sms_probability = email_model.predict_proba(sms_vector)[0]

               ham_sms_probability = sms_probability[0]*100
               spam_sms_probability = sms_probability[1]*100

               st.header('SMS Analysis')

               
               
        
               if sms_prediction == 1:
                    st.write('Prediction: Spam')
                    st.write(f"Spam probability: **{spam_sms_probability:.2f}%**")
                    st.plotly_chart(chart(spam_sms_probability, 'Spam Probability'))
               else:
                    st.write('Prediction: Legitimate')
                    st.write(f"Ham probability: **{ham_sms_probability:.2f}%**")
                    st.plotly_chart(chart(ham_sms_probability, 'Ham Probability'))

               urls = re.findall(r'(https?://[^\s]+|www\.[^\s]+)', sms_text)

               if urls:
                     st.subheader("URL Analysis")
                     for url in urls:
                        url_vector = url_vectorizer.transform([url])
                        url_prediction = url_model.predict(url_vector)[0]
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
