import streamlit as st

# Using CSS to increase the font aize of side menu and icona
st.markdown("""
<style>

section[data-testid="stSidebar"] .st-emotion-cache-1v0mbdj {
    font-size: 20px !important;
}


section[data-testid="stSidebar"] * {
    font-size: 18px !important;
}
</style>
""", unsafe_allow_html=True)


st.logo("app/logo2.png", size="large")



pages = {
    "": [
        st.Page("pages/1_Home.py", title="Home", icon = ':material/home:'),
        st.Page("pages/2_About_ScamLens.py", title="About ScamLens", icon = ':material/info:'),
        st.Page("pages/3_User_Tips.py", title="User Tips", icon = ':material/lightbulb:'),
        st.Page("pages/4_Useful_Links.py", title="Useful Links", icon = ':material/link:'),
    ]
}

pg = st.navigation(pages, position='sidebar')
pg.run()