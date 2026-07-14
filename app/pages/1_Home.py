
# Importing Python libraries

import streamlit as st
import joblib
import plotly.graph_objects as go 
import re
import unicodedata






# Using markdown and CSS to hide the deploy menu of the interface.
st.markdown("""
<style>
[data-testid="stToolbar"] {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# Removing all header and footer space from the page.
st.markdown("""
<style>
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}
</style>
""", unsafe_allow_html=True)


# Creating title  and short introduction of the app.
st.title('Welcome to ScamLens ',text_alignment='center' )
st.write('A detection platform designed to analyse text messages, emails, and URLs for potential threats. ' \
'Simply input your        data to scan for spam content and receive an instant ' \
'                  probability score for the risk level')

# Using HTML to create a custom warning box to provides to the user.
st.markdown(
    """
    <div style='background-color: #fbc02d; color: black; padding: 1rem; border-radius: 0.5rem; font-size: 0.85rem; margin-bottom: 0.5rem;'>
    ⚠️ Please do not input any sensitive information such as name, address, phone number, or your personal email address. The platform will analyse your content without storing any data.
    </div>
    """,
    unsafe_allow_html=True
)

# Calling email SVM model, email SVM TF-IDF vectorizer model.
# Because the SMS model could not capture and classify the text, 
# in application will be applay only the email model.

# Calling url SVM model and url TF-IDF vectorizer.

email_model = joblib.load('models/email_svm_model.pkl')
email_vectoriser = joblib.load('models/email_tfidf.pkl')
url_model = joblib.load('models/url_svm_model.pkl')
url_vectorizer = joblib.load('models/url_tfidf.pkl')


#Creating 3 tabs SMS, Email, URL, user to has a option to choose what type of service he wants to use.
tab1, tab2, tab3 = st.tabs(['SMS', 'Email','URL'])


# Creating a function to apply the plotly chart Indicator into tabs SMS, Email, and URL.
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
                {'range': [0,50], 'color': '#2E8B57'},
                {'range': [50,75], 'color': '#F4C542'},
                {'range': [75,100], 'color':'#D62828'}
            ]
        }
    ))
    return fig

# Creating Tab 1 for SMS section input
with tab1:
    st.subheader('SMS')

# Using st.form to clean the text from the imput box, an dreaedy to be use for another analysis of text.
    with st.form(key='sms_form', clear_on_submit=True):
        sms_text = st.text_area('Please enter or paste an SMS message')
    
        analyse_Sbt = st.form_submit_button('Analyse SMS', type='primary')

# Using the IF condition and HTML for custom style box to provide to the user a warning message if he dit not paste any text in the input box.
        if sms_text.strip()=="":
               
               st.markdown(
    """
    <div style='background-color: #fbc02d; color: black; padding: 1rem; border-radius: 0.5rem; font-size: 0.85rem; margin-bottom: 0.5rem;'>
    ⚠️ Please enter or paste an SMS message.
    </div>
    """,
    unsafe_allow_html=True
)
               #The ELSE block represent that TF-IDF vectorizer takes the raw text and passes intto trained TF-IDF email model.
               # after that the result is converted into vectors and passes into email model to define if the content is Spam or Ham.
               # With email_predict_proba instead of simple YES or No , it returns probability score to the user.
        else:
               sms_vector = email_vectoriser.transform([sms_text])
               sms_prediction = email_model.predict(sms_vector)[0]
               sms_probability = email_model.predict_proba(sms_vector)[0]

               ham_sms_probability = sms_probability[0]*100
               spam_sms_probability = sms_probability[1]*100

               st.header('SMS Analysis')

               
               # Applying IF condition to specify that if the content is Spam to provide to the user probability score and applying the function ,
               # of the plotly chart to represents also the content into a graphical chart.
        
               if sms_prediction == 1:
                    st.write('Prediction: Spam')
                    st.write(f"Spam probability: **{spam_sms_probability:.2f}%**")
                    st.plotly_chart(chart(spam_sms_probability, 'Spam Probability'))
               else:
                    st.write('Prediction: Legitimate')
                    st.write(f"Ham probability: **{ham_sms_probability:.2f}%**")
                    st.plotly_chart(chart(ham_sms_probability, 'Ham Probability'))

               # Using Regular Expression to extract the link characteristics.
               urls = re.findall(r'(https?://[^\s]+|www\.[^\s]+)', sms_text)

            
                # Using FOR IN Loop to add the URL model and URL TF-IDF vectorizer model,
                # to find chrck if the text content has url, and if is TRUE to extract this URL.
                # The system combined and both trained  model Email and URL in on place to handle if the text has any link inside.
               if urls:
                     st.subheader("URL Analysis")
                     for url in urls:
                        url_vector = url_vectorizer.transform([url])
                        url_prediction = url_model.predict(url_vector)[0]
                        url_probability = url_model.predict_proba(url_vector)[0]

                        ham_url_probability = url_probability[0] * 100
                        spam_url_probability = url_probability[1] * 100

                        st.write(f"URL: {url}")

                        mix_char = r"[\u0370-\u03FF\u0400-\u04FF\u0530-\u058F]"
                        zero_width = r"[\u200B\u200C\u200D\u2060]"
                        hidden = re.findall(mix_char,url)
                        zero = re.findall(zero_width, url)
                        if hidden:
                           st.warning('⚠️ The link has mixed alphabet characters:')
                           for i in hidden:
                                 
                                 name = unicodedata.name(i)          
                                 script = name.split()[0].capitalize() 
                                 st.write(f"{i} → {hex(ord(i))}→ {script} alphabet")
                              
                        else:
                              st.write('The link does not have any hidden mixed alphabets letter')
                        if zero:
                              st.warning('⚠️ Hidden zero-width characters found:')
                              for j in zero:
                                st.write(f"- `{j}` → `{hex(ord(j))}`")
                        else:
                            st.write(' The link does not have any hidden numbers')










                        
                        if url_prediction == 1:
                          st.write("Prediction: **Spam**")
                          st.write(f"Spam probability: **{spam_url_probability:.2f}%**")
                        else:
                          st.write("Prediction: **Legitimate URL**")
                          st.write(f"Ham probability: **{ham_url_probability:.2f}%**")
               
               # If the text is classified as Spam the ELSE condition will provide a warning ,essage to the user
               # about that probably the text contains a hiddin link and do not click anywhere inside.
               else:
                     st.info("No URLs found in this SMS.")
                     if sms_prediction == 1:
                       st.warning(
                       "⚠️ This message appears to be **spam** and may contain **hidden malicious links** "
                       "behind buttons or words. Do **NOT** click anywhere in the original SMS."
                       )

# For development of Tab 2 Email section is used the same code , only the name of the text box and model SVM and model TF-IDF are changed.
with tab2:
    st.subheader('Email')
    with st.form(key='email_form', clear_on_submit=True):
        email_text = st.text_area('Please enter or paste an SMS message')
    
        analyse_Sbt = st.form_submit_button('Analyse Email', type='primary')

        if email_text.strip()=="":
            st.markdown(
    """
    <div style='background-color: #fbc02d; color: black; padding: 1rem; border-radius: 0.5rem; font-size: 0.85rem; margin-bottom: 0.5rem;'>
    ⚠️ Please enter or paste an SMS message.
    </div>
    """,
    unsafe_allow_html=True
        )
            
        else:

            email_vector = email_vectoriser.transform([email_text])
            email_prediction = email_model.predict(email_vector)[0]
            email_probability = email_model.predict_proba(email_vector)[0]

            ham_email_probability = email_probability[0]*100
            spam_email_probability = email_probability[1]*100

            st.header('Email Analysis')

            if email_prediction == 1:
                st.write('Prediction: Spam')
                st.write(f"Spam probability: **{spam_email_probability:.2f}%**")
                st.plotly_chart(chart(spam_email_probability, 'Spam Probability'))
            else:
                st.write('Prediction: Legitimate')
                st.write(f"Ham probability: **{ham_email_probability:.2f}%**")
                st.plotly_chart(chart(ham_email_probability, 'Ham Probability'))

            urls = re.findall(r'(https?://[^\s]+|www\.[^\s]+)', email_text)

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
                st.info("No URLs found in this Email.")
                if sms_prediction == 1:
                    st.warning(
                       "⚠️ This Email appears to be **spam** and may contain **hidden malicious links** "
                       "behind buttons or words. Do **NOT** click anywhere in the original email."
                       )
                    
# For tab3 the URL section was used the same code only was removed the email model and TF-IDF model representation of the code.
with tab3:
    st.subheader('URL link')
    with st.form(key='url_form', clear_on_submit=True):
        url_text = st.text_area('Please enter or paste an URL link')
    
        analyse_Sbt = st.form_submit_button('Analyse URL link', type='primary')

        if url_text.strip()=="":
            st.markdown(
    """
    <div style='background-color: #fbc02d; color: black; padding: 1rem; border-radius: 0.5rem; font-size: 0.85rem; margin-bottom: 0.5rem;'>
    ⚠️ Please enter or paste an SMS message.
    </div>
    """,
    unsafe_allow_html=True
        )
        else:
            urls = re.findall(r'(https?://[^\s]+|www\.[^\s]+)', url_text)

            if urls:
                url_vector = url_vectorizer.transform([url_text])
                url_prediction = url_model.predict(url_vector)[0]
                url_probability = url_model.predict_proba(url_vector)[0]

                ham_url_probability = url_probability[0]*100
                spam_url_probability = url_probability[1]*100

                
                st.header(' URL link Analysis')
                st.write(f"URL: {urls}")
                

                if url_prediction == 1:
                   st.write('Prediction: Spam')
                   st.write(f"Spam probability: **{spam_url_probability:.2f}%**")
                   st.plotly_chart(chart(spam_url_probability, 'Spam Probability'))
                else:
                   st.write('Prediction: Legitimate')
                   st.write(f"Ham probability: **{ham_url_probability:.2f}%**")
                   st.plotly_chart(chart(ham_url_probability, 'Ham Probability'))













            

















