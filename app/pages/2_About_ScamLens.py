import streamlit as st

st.markdown("""
<style>
/* Make the main content wider */
.block-container {
    max-width: 1200px;
    padding-left: 2rem;
    padding-right: 2rem;
}
</style>
""", unsafe_allow_html=True)





st.markdown("""
<div style='text-align:center; color:white; font-size:50px;'>
<h1><b>Welcome to ScamLens</b></h1>
</div>
""",unsafe_allow_html=True)



st.markdown("""
<div style='text-align:center; padding-bottom:30px; font-size:20px; color:white;'>
<p><b>ScamLens is a simple and free online tool that helps you check whether a message, email,
or website link might be a scam. It is designed for everyday users and does not require any installation, subscription, or account.
</b>
</p>
</div>
""", unsafe_allow_html=True)


with st.container():
    st.subheader('What You Can Check',text_alignment='center')
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:20px;padding: 20px;color: #79E2B3;'>
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
            <div style = 'background-color:#133B28;padding-bottom:5px;font-size:20px;padding: 20px;color: #79E2B3;'>
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
            <div style = 'background-color:#133B28;padding-bottom:5px;font-size:20px;padding: 20px;color: #79E2B3;'>
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
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:20px;padding: 20px;color: #79E2B3;'>
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
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:20px;padding: 20px;color: #79E2B3;'>
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
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:20px;padding: 20px;color: #79E2B3;'>
            <span style="color:#79E2B3; font-size:42px;">③</span>
            <span style="color:#79E2B3;">➤</span> Review
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;'>
        See the prediction, probability score and safety guidance before deciding what to do next.
        </div>
        """,unsafe_allow_html=True)

