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



tab1, tab2 = st.columns([8,20])
with tab2:
    st.image('app/title.png', width=450)

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



st.subheader('What ScamLens Can Detect', text_alignment='center')
st.markdown("""
<div style='text-align:left; font-size:20px;background-color:#204635;padding: 24px; border-radius: 12px;'>
    <ul>
        <li><span style="color:#F4C542; margin-right:8px;">☎</span> Suspicious or scam text messages</li>
        <li><span style="color:#F4C542; margin-right:8px;">✉</span> Phishing emails</li>
        <li><span style="color:#F4C542; margin-right:8px;">⛓</span> Malicious or unsafe website links</li>
        <li><span style="color:#F4C542; margin-right:8px;">⚠</span> Hidden characters or mixed alphabets inside URLs</li>
    </ul>
</div>
""", unsafe_allow_html=True)


st.subheader("How ScamLens Works",text_alignment='center')
st.markdown("""
<div style = 'text-align:center; padding-bottom: 30px;font-size:20px;'>
ScamLens uses machine learning algorithms to analyse your text or link and estimate
how likely it is to be a scam. You will receive a clear result, a percentage score, and
a simple visual chart to help you understand the analysis.
</div>
""", unsafe_allow_html=True)

st.warning("""
⚠️ ScamLens provides an estimated probability score.  
This score may not always be correct — always double check the original message or link.
""")


st.subheader("Your Privacy Matters",text_alignment='center')
st.markdown("""
<div style='text-align:left; padding-bottom: 30px;font-size:20px;background-color:#204635;padding: 24px; border-radius: 12px;'>
    <ul>
        <li> <span style="color:#F4C542;margin-right:8px;">✓</span> ScamLens does not store your messages, emails, or links</li>
        <li> <span style="color:#F4C542;margin-right:8px;">✓</span> No personal data is saved or shared</li>
        <li> <span style="color:#F4C542;margin-right:8px;">✓</span> No installation or download is required</li>
        <li> <span style="color:#F4C542;margin-right:8px;">✓</span> ScamLens is completely free to use</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.subheader("Coming Soon", text_alignment='center')
st.markdown("""
<div style='text-align:left; padding-bottom: 30px;font-size:20px;background-color:#204635;padding: 24px; border-radius: 12px;'>
    <ul>
        <li><span style="color:#F4C542;">▸</span> Support for more languages</li>
        <li><span style="color:#F4C542;">▸</span> Improved scam detection accuracy</li>
        <li><span style="color:#F4C542;">▸</span> More visual tools to help you understand results</li>
    </ul>
</div> 
""", unsafe_allow_html=True)


st.subheader("Feedback & Support",text_alignment='center')
st.markdown("""
Have suggestions or found an issue?  
You can share feedback on GitHub:  
▸ https://github.com/VasilkaVlaykova
""")

