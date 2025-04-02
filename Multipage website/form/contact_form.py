import streamlit as st
import re
import requests

WEBHOOK_URL=""
# def is_email_valid(email):
#    email_patterm=r"^[\w.-]+@[a-zA-Z\d.-]+\.[a-zA-Z]{2,}$"
#    return re.match(email_patterm,email) is not None


def contact_form():
  with st.form("contact_form"):
    name=st.text_input("Enter Name")
    email=st.text_input("Enter Email")
    message=st.text_input("Your Message")
    submit=st.form_submit_button("Submit")

    if submit:
        st.success("Done!")

    

