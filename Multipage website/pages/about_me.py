import streamlit as st

from form.contact_form import contact_form

# contact form
@st.dialog("Contact")
def contact():
    contact_form()


# hero section
col1,col2=st.columns(2,gap="small",vertical_alignment="center")
with col1:
    st.image("./assets/profile.jpeg", width=250)
with col2:
    st.title("Kinza Saeed",anchor=False)
    st.write("Hi, I'm Kinza Saeed, a UI/UX designer and developer skilled in Next.js, TypeScript, and Python, crafting seamless digital experiences.")    
    if st.button("Contact me ✉️"):
        contact()

st.write("\n")
st.subheader("Skills ",anchor=False)
st.write("""
- UI/UX Designer – Crafting intuitive and user-friendly digital experiences.
- Next.js Developer – Building fast and scalable web applications.
- TypeScript Enthusiast – Writing clean and maintainable code.
- Python Programmer – Automating tasks and backend development.
- Problem Solver – Passionate about innovative and efficient solutions.
""")        