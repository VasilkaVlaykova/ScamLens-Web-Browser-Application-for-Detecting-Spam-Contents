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

st.markdown("""
   <div style='text-align:center; color:white; font-size:40px;padding-bottom:30px;'>
   User Tips
   </div>
   """,unsafe_allow_html=True)

st.markdown("""
    <div style='text-align:center; font-size:18px;margin-bottom:18px;'>
        This page highlights common warning signs that can help you recognise
        suspicious messages, emails and website links before you interact with them..
    </div>
     """,
    unsafe_allow_html=True)


with st.container(border=True):
    st.subheader('How to Spot a Suspicious Text Message', text_alignment='center')
    col1, col2 = st.columns([10,15])
    with col1:
        st.image('app/phone2.png', width=300)
    with col2:
        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;'>
        Unknown sender
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;'>
        Be cautious when a message comes from an unfamiliar number.
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;'>
         Urgent language       
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;'>
        Scammers may pressure you to act immediately or threaten negative consequences.
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;'>
        Unexpected reward or refund       
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;'>
        Do not trust messages claiming you have won money, received a refund or qualify for a prize.
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;'>
        Suspicious link       
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;'>
        Avoid opening shortened, misspelled or unfamiliar website links.
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;'>
        Request for personal information       
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;'>
        Never send passwords, banking details, security codes or other sensitive information by SMS.
        </div>
        """,unsafe_allow_html=True)
        





with st.container(border=True):
    st.subheader('How to Recognise a Scam Email', text_alignment='center')
    col1, col2 = st.columns([10,10])
    with col1:
        st.image('app/email2.png', width=600)


with st.container(border=True):
    st.subheader('How to Recognise a Suspicious Website Link',text_alignment='center')
    col1, col2 = st.columns([10,10])
    with col1:
        st.image('app/url2.png', width=600)
