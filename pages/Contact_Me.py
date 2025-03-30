import streamlit as st
# Adding contact me page
st.header("Contact Me")

with st.form(key="Enter_your_email"):
    email=st.text_input("Your email address")
    message=st.text_area("Your message")
    submit_button=st.form_submit_button("Submit")
    if submit_button:
        print(submit_button)
        Message= message + email
