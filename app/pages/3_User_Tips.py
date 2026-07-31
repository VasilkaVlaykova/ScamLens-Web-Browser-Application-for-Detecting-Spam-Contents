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
   <b>User Tips</b>
   </div>
   """,unsafe_allow_html=True)

st.markdown("""
    <div style='text-align:center; font-size:18px;margin-bottom:18px;'>
       <b> This page highlights common warning signs that can help you recognise
        suspicious messages, emails and website links before you interact with them.
       </b>
    </div>
     """,
    unsafe_allow_html=True)


with st.container(border=True):
    st.subheader('How to Spot a Suspicious Text Message', text_alignment='center')
    col1, col2 = st.columns([10,15])
    with col1:
        st.image('app/phone2.png', width=350)
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
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;margin-top:20px;'>
         Urgent language       
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;'>
        Scammers may pressure you to act immediately or threaten negative consequences.
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;margin-top:20px;'>
        Unexpected reward or refund       
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;'>
        Do not trust messages claiming you have won money, received a refund or qualify for a prize.
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;margin-top:20px;'>
        Suspicious link       
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;'>
        Avoid opening shortened, misspelled or unfamiliar website links.
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;margin-top:20px;'>
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
    col1, col2 = st.columns([12,10],gap='large')
    with col1:
        st.image('app/email2.png', width=700)
        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;'>
        Hidden or misleading links
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;'>
        A button may hide the real website address behind text such as<mark> <b>Confirm My Identity</b> </mark>, or<mark> <b>Claim Your Reward</b> </mark>.
         Avoid clicking unexpected buttons or links,
        especially when the destination cannot be verified.  
        </div>
        """,unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;'>
        Suspicious sender address
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;margin-bottom:20px;'>
        Check whether the sender’s email address matches the organisation’s official domain. Look for misspellings, 
        extra numbers<mark> <b>[0-9]</b> </mark>, unusual symbols<mark> <b>[!, $, %, &, _, -, .,]</b> </mark>or letters that imitate the original address.
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;margin-top:19px;'>
         Urgent or threatening language
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;margin-bottom:20px;'>
           <ul>
               <li>Your account will be suspended.</li>
               <li>You must pay a penalty within 24 hours.</li>
               <li>Your delivery has been stopped.</li>
               <li>Your cloud storage is full.</li>
               <li>Unusual activity was detected.</li>
               <li>Verify your identity immediately.</li>
           </ul>
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;margin-top:19px;'>
        Unexpected rewards or offers
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;'>
         Be cautious of emails claiming that you have won money, received a refund, qualified for a reward or been selected for a special offer. 
         These messages may encourage you to click a button and complete a form.      
        </div>
        """,unsafe_allow_html=True)

        
        
        


with st.container(border=True):
    st.subheader('How to Recognise a Suspicious Website Link',text_alignment='center')
    col1, col2 = st.columns([12,10])
    with col1:
        st.image('app/url2.png', width=600)
        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;'>
         Hidden zero-width characters
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;'>
        A link may contain invisible characters placed between parts of a familiar name. 
        The address can appear normal even though an extra hidden character is present.
        <br><br>
        <mark> <b>Example:</b> https://microsoft-account-security.example/verify </mark>
        <br><br>
        <mark> <b>Visible Example:</b> https://micro[ZWSP]soft-account-security.example/verify </mark>
        <br><br>
        <b>Explanation:</b><mark> <b>[ZWSP]</b> </mark>represents an invisible zero-width space.
        </div>
        """,unsafe_allow_html=True)
        

    with col2:
        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;'>
         Numbers replacing letters
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;'>
        Scammers may replace letters with similar-looking numbers to imitate a trusted website name. For example, 
        the<mark> <b>number 1</b> </mark>may replace the<mark> <b>letter l</b> </mark>, or<mark> <b>0</b> </mark>may replace the letter<mark> <b>o</b> </mark>.
        <br><br> 
        <mark> <b>Example:</b> https://paypa1-secure-login.example </mark>
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;margin-top:80px;'>
        Encoded or unusual symbols
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;margin-bottom:80px;'>
        Suspicious links may contain encoded characters such as<mark> <b>%40</b> </mark>, extra symbols or unusual punctuation.
          These can make the address difficult to read and may hide the real destination.
          <br><br>
          <mark> <b>Example:</b> https://bank-security.example/&40account-confirmation </mark>
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div style = 'padding-bottom:5px;font-size:14px;color: #79E2B3;margin-top:30px;'>
        Mixed alphabet characters
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 20px;  border: 1px solid #79E2B3;'>
        Some links use letters from another alphabet that look almost identical to English letters. For example,
        <mark> <b>Cyrillic о</b> </mark>may be used instead of the<mark> <b>English o<b> </amrk>.
        <br><br>
        <b>Example:</b> https://gооgle-security-check.example/login
        </div>
        """,unsafe_allow_html=True)


st.markdown("""
           <div style='background-color: #fdd835; color: black; padding: 1rem; border-radius: 0.5rem;font-size:14px;margin-top:10px;'>
           ⚠️ <b>Do not panic or act immediately.</b> Pause and check the sender, website domain and urgent wording carefully. Do not click links or share personal information. Verify the message through the organisation’s official website or trusted phone number,
             and ask someone you trust for a second opinion when you are unsure.
           </div>
           """,unsafe_allow_html=True)

with st.container():
    st.header('General Online Safety Tips',text_alignment='center')
    col1, col2, col3, col4 =st.columns(4,gap='small')
    with col1:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 10px;color: #79E2B3;'>
        <b>Keep devices updated</b>
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 15px;padding-bottom:34px;'>
        Install software, browser and security updates regularly to protect your devices from known threats.
        </div>
        """,unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 10px;color: #79E2B3;'>
        <b>Use strong, unique passwords</b>
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 15px;'>
        Use a different password for every account. Change it immediately when you believe it has been exposed or stolen.
        </div>
        """,unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 10px;color: #79E2B3;'>
        <b>Enable two-factor authentication</b>
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 15px;padding-bottom:34px;'>
        Add an extra security step to important accounts such as email, banking and social media.
        </div>
        """,unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 10px;color: #79E2B3;'>
        <b>Protect personal information</b>
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 15px;padding-bottom:32px;'>
        Avoid sharing your address, phone number, date of birth, 
        travel plans or financial information publicly online
        </div>
        """,unsafe_allow_html=True)

with st.container():
    col1, col2, col3, col4 =st.columns(4, gap='small')
    with col1:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 10px;color: #79E2B3;margin-top:5px;'>
        <b>Review privacy settings</b>
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 15px;padding-bottom:34px;'>
        Check who can see your posts, profile details and contact information on social media
        </div>
        """,unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 10px;color: #79E2B3;margin-top:5px;'>
        <b>Download from trusted sources</b>
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 15px;padding-bottom:34px;'>
        Only install applications, files and browser extensions from official websites or recognised app stores.
        </div>
        """,unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 10px;color: #79E2B3;margin-top:5px;'>
        <b>Back up important files</b>
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 15px;padding-bottom:34px;'>
        Keep secure copies of important documents and photographs in case your device is lost, 
        damaged or attacke
        </div>
        """,unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div style = 'background-color:#133B28;padding-bottom:5px;font-size:14px;padding: 10px;color: #79E2B3;margin-top:4px;'>
        <b>Stop and verify</b>
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""
        <div style = 'background-color:#133B28;padding: 15px;padding-bottom:36px;'>
        Take time to check unexpected messages, requests and links before clicking,
          replying or making a payment.
        </div>
        """,unsafe_allow_html=True)







        


