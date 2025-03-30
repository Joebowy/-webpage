import streamlit as st
from sending_email import send_email
# Adding contact me page
st.header("Contact Me")

with st.form(key="Enter_your_email"):
    user_email=st.text_input("Your email address")
    raw_message=st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    submit_button=st.form_submit_button("Submit")
    if submit_button:
        send_email(message)
        st.info("Your message was sent successfully")

