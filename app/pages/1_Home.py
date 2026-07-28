
# Importing Python libraries

import streamlit as st
import joblib 
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
    padding-top: 2rem;
    padding-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""

<style>
/* Make the main content wider */
.block-container {
    #max-width: 1000px;
    #padding-left: 2rem;
    #padding-right: 2rem;
}
</style>
""", unsafe_allow_html=True)



             
# Applying ScamLens image as title/

tab1, tab2 = st.columns([8,20])


with tab2:
     st.image("app/title.png", width=400)

# Creating title  and short introduction of the app.
#st.title('Welcome to ScamLens ',text_alignment='center' )
st.markdown("""
<div style='text-align:center; font-size:18px;'>
<p><b> A detection platform designed to analyse text messages, emails, and URLs for potential threats. 
Simply input your data to scan for spam content 
and receive an instant probability score for the risk level.
</b>
</p>
</div>
""",unsafe_allow_html=True)


# Using HTML to create a custom warning box to provides to the user.
st.markdown(
    """
    <div style='background-color: #fdd835; color: black; padding: 1rem; border-radius: 0.5rem;font-size:14px;'>
    ⚠️ Please do not input any sensitive information such as name, address, phone number, or your personal email address. The platform will analyse your content without storing any data.
    </div>
    """,
    unsafe_allow_html=True
)


# Streamlit function to load global only one time and run the Email and URL models and TF-IDF vectorizer models.

@st.cache_resource(show_spinner=False)
def email_load_models():
    return joblib.load('models/email_pipeline.pkl')


@st.cache_resource(show_spinner=False)
def url_load_model():
    return joblib.load('models/url_pipeline.pkl')



#Runs a text through the given model + vectoriser, displays the
#prediction and probability, and optionally shows the plotly gauge chart.
#Used for both SMS/email and URL analysis to avoid repeating the same
#predict, probability, display logic twice.

def predict_and_display(pipeline, text, spam_label='Spam', ham_label='Legitimate', show_chart=False):

    #vector = vectorizer.transform([text])
    prediction = pipeline.predict([text])[0]
    probability = pipeline.predict_proba([text])[0]

    ham_probability = probability[0] * 100
    spam_probability = probability[1] * 100

    if prediction == 1:
        st.write(f"Prediction: **{spam_label}**")
        st.write(f"Spam probability: **{spam_probability:.2f}%**")
        if show_chart:
            st.plotly_chart(chart(spam_probability, 'Spam Probability'))
    else:
        st.write(f"Prediction: **{ham_label}**")
        st.write(f"Ham probability: **{ham_probability:.2f}%**")
        if show_chart:
          st.plotly_chart(chart(ham_probability, 'Ham Probability'))
             
    return prediction, spam_probability, ham_probability    

st.markdown("""
<style>
    button[data-baseweb="tab"] p {
        font-size: 18px !important;
    }
</style>
""", unsafe_allow_html=True)

#Creating 3 tabs SMS, Email, URL, user to has a option to choose what type of service he wants to use.
tab1, tab2, tab3 = st.tabs(['SMS', 'Email','URL'])
# Creating a function to apply the plotly chart Indicator into tabs SMS, Email, and URL.
def chart(value, label):
    import plotly.graph_objects as go 
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

# Using st.form to clean the text from the imput box, and reaedy to be use for another analysis of text.
    with st.form(key='sms_form',clear_on_submit=True,):
        sms_text = st.text_area('Please enter or paste an SMS message')
        analyse_Sbt = st.form_submit_button('Analyse SMS', type='primary')

# Using the IF condition and HTML for custom style box to provide to the user a warning message if he dit not paste any text in the input box.
        if sms_text.strip()=="":
               
               st.markdown(
               """
               <div style='background-color: #fff59d; color: #333333;padding-bottom:20px; padding: 1rem; border-radius: 0.5rem;font-size:14px;'>
               🔒 This system does not store your messages. Your text is deleted automatically right after it is analyzed.
               </div>
               """,
               unsafe_allow_html=True
               )          
        else:
               email_pipeline = email_load_models()
               # calling the probability function and plotly chart to be display.
               st.header('SMS Analysis')
               sms_prediction, spam_sms_probability, ham_sms_probability = predict_and_display(
               email_pipeline, sms_text,
               spam_label='Spam', ham_label='Legitimate', show_chart=True
               )

               # Using Regular Expression to extract from the text input URL.
               urls = re.findall(r'(https?://[^\s]+|www\.[^\s]+)', sms_text)

            
                # IF Nested condition for URL detected from the text, applying  probability function.
               if urls:
                     st.subheader("URL Analysis")
                     for url in urls:
                      url_pipeline = url_load_model()
                      url_prediction, spam_url_probability, ham_url_probability = predict_and_display(
                      url_pipeline, url,
                      spam_label='Spam', ham_label='Legitimate URL', show_chart=False
                      )

                     st.write(f"URL: {url}")

                     # Unicode for mixed letters and hidden zero-width characters.
                     mix_char = r"[\u0370-\u03FF\u0400-\u04FF\u0530-\u058F]"
                     zero_width = r"[\u200B\u200C\u200D\u2060]"
                     hidden = re.findall(mix_char,url)
                     zero = re.findall(zero_width, url)
                     if hidden:
                           st.warning('⚠️ The link has mixed alphabet characters:')
                           for i in hidden:
                                 # For loop to extraxt the mixed letters 
                                 # displaying as well the name of the found letters.
                                 name = unicodedata.name(i)          
                                 script = name.split()[0].capitalize() 
                                 st.write(f"{i} → {hex(ord(i))}→ {script} alphabet")        
                     else:
                              st.info('The link does not have any hidden mixed alphabets letter')
                     if zero: # Diplaying the zero-width to the user with a warning message.
                              st.warning('⚠️ Hidden zero-width characters found:')
                              for j in zero:
                                st.write(f"- `{j}` → `{hex(ord(j))}`")
                     else:  # If the link does not have any hidden numbers will display a message to the user.
                            st.info(' The link does not have any hidden numbers')
               
               # If the text is classified as Spam the ELSE condition will provide a warning ,essage to the user
               # about that probably the text contains a hiddin link and do not click anywhere inside.
               else:
                     st.info("No URLs found in this SMS.")
                     if sms_prediction == 1: #  If the sms is spam and do not detect any link, display a message to the user
                                              #a warning probaby the text containts a hidden link do not click anywhere.
                       st.warning(
                       "⚠️ This message appears to be **spam** and may contain **hidden malicious links** "
                       "behind buttons or words. Do **NOT** click anywhere in the original SMS."
                       )

# For development of Tab 2 Email section is used the same code , only the name of the text box and model SVM and model TF-IDF are changed.
with tab2:
    st.subheader('Email')
    with st.form(key='email_form', clear_on_submit=True):
        email_text = st.text_area('Please enter or paste an Email message')
        analyse_Sbt = st.form_submit_button('Analyse Email', type='primary')
        if email_text.strip()=="":
            st.markdown(
            """
            <div style='background-color: #fff59d; color: #333333; padding: 1rem; border-radius: 0.5rem;'>
            🔒 This system does not store your email. Your text is deleted automatically right after it is analyzed.
            </div>
            """,
            unsafe_allow_html=True
            )      
        else:
            email_pipeline=email_load_models()
            st.header('Email Analysis')
            email_prediction, spam_email_probability, ham_email_probability = predict_and_display(
               email_pipeline, email_text,
               spam_label='Spam', ham_label='Legitimate', show_chart=True
               )
            
            urls = re.findall(r'(https?://[^\s]+|www\.[^\s]+)', email_text)
            if urls:
                st.subheader("URL Analysis")
                for url in urls:
                    url_pipeline=url_load_model()
                    url_prediction, spam_url_probability, ham_url_probability = predict_and_display(
                    url_pipeline, url,
                    spam_label='Spam', ham_label='Legitimate URL', show_chart=False
                    )
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
                        st.info('The link does not have any hidden mixed alphabets letter')
                    if zero:
                        st.warning('⚠️ Hidden zero-width characters found:')
                        for j in zero:
                            st.write(f"- `{j}` → `{hex(ord(j))}`")
                    else:
                         st.info(' The link does not have any hidden numbers')
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
            <div style='background-color: #fff59d; color: #333333; padding: 1rem; border-radius: 0.5rem;'>
            🔒 This system does not store your URL link. Your text is deleted automatically right after it is analyzed.
            </div>
            """,
            unsafe_allow_html=True
            )
        else:
            urls = re.findall(r'(https?://[^\s]+|www\.[^\s]+)', url_text)
            if urls:
                 for url in urls:
                  url_pipeline=url_load_model()
                  st.header(' URL link Analysis')
                  url_prediction, spam_url_probability, ham_url_probability = predict_and_display(
                      url_pipeline, url,
                      spam_label='Spam', ham_label='Legitimate URL', show_chart=True
                      )
                  st.write(f"URL: {urls}")
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
                    st.info('The link does not have any hidden mixed alphabets letter')
                 if zero:
                    st.warning('⚠️ Hidden zero-width characters found:')
                    for j in zero:
                        st.write(f"- `{j}` → `{hex(ord(j))}`")
                 else:
                    st.info(' The link does not have any hidden numbers')
            else:
                st.info("No URLs found in this Email.")
                if sms_prediction == 1:
                    st.warning(
                       "⚠️ This Email appears to be **spam** and may contain **hidden malicious links** "
                       "behind buttons or words. Do **NOT** click anywhere in the original email."
                       )
email_load_models()
url_load_model()
            













            

















