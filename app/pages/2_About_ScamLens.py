import streamlit as st

st.markdown("""
<style>
/* Make the main content wider */
.block-container {
    max-width: 1000px;
    padding-left: 1rem;
    padding-right: 1rem;
}
</style>
""", unsafe_allow_html=True)



col1, col2, col3 = st.columns([20,1,15])
with col1:
     st.markdown("""
     <div style='text-align:center; color:white; font-size:40px;padding-bottom:30px;'>
     <b>Welcome to ScamLens</b>
     </div>
     """,unsafe_allow_html=True)



     st.markdown("""
     <div style='text-align:center;font-size:20px; color:white;'>
     <p><b>ScamLens is a simple and free online tool that helps you check whether a message, email,
     or website link might be a scam. It is designed for everyday users and does not require any installation, subscription, or account.
     </b>
     </p>
     </div>
     """, unsafe_allow_html=True)
with col3:
    st.image('app/about.png', width= 400)


with st.container():
    st.subheader('What You Can Check',text_alignment='center')
    col1, col2, col3 = st.columns(3, gap='small')
    with col1:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 20px;color: #79E2B3;'>
        💬 SMS Messages
        </div>
        """,unsafe_allow_html=True)
        
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;'>
        Check suspicious SMS messages, unusual wording, urgency and common scam patterns.
        </div>
        """,unsafe_allow_html=True)
        

    with col2:
        st.markdown("""
            <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 20px;color: #79E2B3;'>
             ✉️ Emails
            </div>
                """,unsafe_allow_html=True)
                
        st.markdown("""
            <div style = 'background-color:#133B28;padding: 20px;'>
                Analyse emails that may contain phishing, fraudulent requests or suspicious language.
            </div>
            """,unsafe_allow_html=True)
        
        

    with col3:
        st.markdown("""
            <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 20px;color: #79E2B3;'>
                🔗 URLs
            </div>
        """,unsafe_allow_html=True)
                        
        st.markdown("""
            <div style = 'background-color:#133B28;padding: 20px;'>
                Check URLs for malicious patterns, misleading domain and unusual or hidden characters.
            </div>
            """,unsafe_allow_html=True)

with st.container():
    st.subheader('How It Works', text_alignment='center')
    col1, col2, col3= st.columns(3,gap='small')
    with col1:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 20px;color: #79E2B3;'>
        <span style="color:#79E2B3; font-size:42px;">①</span>
        <span style="color:#79E2B3;">➤</span> Choose
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;'>
        Select the type of content you want to check: SMS message, email or website link.
        </div>
        """,unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 20px;color: #79E2B3;'>
           <span style="color:#79E2B3; font-size:42px;">②</span>
           <span style="color:#79E2B3;">➤</span> Paste
        </div>
         """, unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;'>
            Enter or paste the message, email or website link you want ScamLens to analyse.
        </div>
        """,unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 20px;color: #79E2B3;'>
            <span style="color:#79E2B3; font-size:42px;">③</span>
            <span style="color:#79E2B3;">➤</span> Review
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;'>
        See the prediction, probability score and safety guidance before deciding what to do next.
        </div>
        """,unsafe_allow_html=True)


st.markdown("""
    <div style='background-color: #fdd835; color: black; padding: 1rem; border-radius: 0.5rem;font-size:14px; margin-top: 18px;'>
    ⚠️ Please do not input any sensitive information such as name, address, phone number, or your personal email address. The platform will analyse your content without storing any data.
    </div>
      """,unsafe_allow_html=True)

with st.container():
    st.subheader('Why Use ScamLens >', text_alignment='center')
    col1, col2, col3, col4= st.columns(4,gap='small')

    with col1:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 20px;color: #79E2B3;'>
        <span style="color:#79E2B3; font-size:34px;">🔒</span> No account required:
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 15px;'>
        Use ScamLens instantly without creating an account or signing in.
        </div>
        """,unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 20px;color: #79E2B3;'>
        <span style="color:#79E2B3; font-size:34px;">£</span> Free to use:
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 15px;'>
         Use all ScamLens features for free, with no subscription or charges.
        </div>
        """,unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 20px;color: #79E2B3;'>
        <span style="color:#79E2B3; font-size:34px;">🛡</span> Content protected:
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 15px;'>
        Your content is analysed without being stored or shared
        </div>
        """,unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 20px;color: #79E2B3;'>
        <span style="color:#79E2B3; font-size:34px;">↯</span> Fast results:
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 15px;'>
         Receive your ScamLens analysis in seconds.       
        </div>
        """,unsafe_allow_html=True)


st.markdown("""
    <div style='background-color: #fdd835; color: black; padding: 1rem; border-radius: 0.5rem;font-size:14px; margin-top: 18px;'>
    ⚠️ ScamLens can make mistakes. Always double-check the result before clicking a link, replying, or sharing personal information.
    </div>
    """,unsafe_allow_html=True)


st.subheader('Feedback',text_alignment='center')
with st.container(border=True):
     st.write('For any questions or complaints about the ScamLens feel free to contact us using the link below.')
     st.write('➤ [GitHub Profile] https://github.com/VasilkaVlaykova')
