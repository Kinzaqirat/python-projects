import streamlit as st

# Page setup

about_page=st.Page(
    page="pages/about_me.py",
    title="About me",
    icon="👩‍💻",
    default=True
)
chatbot_page=st.Page(
    page="pages/chatbot.py",
    title="Chatbot",
    icon="🤖"
    
)

# page navigation

# pg=st.navigation(pages=[about_page,chatbot_page])

pg=st.navigation(
    {
        "Info" :[about_page],
        "projects":[chatbot_page],
    }
)


# logo

st.logo("assets/logo.png")
st.sidebar.text("Made by Kinza Saeed")
# run navigation
pg.run()