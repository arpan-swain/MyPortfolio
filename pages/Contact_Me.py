import streamlit as st
from send_email import send_email
st.header("Contact Me")

form = st.form(key = "email_form")
print(form)

with form:
    user_email = st.text_input("Your email here")
    raw_message = st.text_area("Your message")

    # selected_option = st.selectbox("Select an option",)
    # important : there should be an empty line after subject
    message = f"""\
Subject: New Message from {user_email}
 
{raw_message}
{user_email}
"""
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(message)
        st.info("Your email was sent successfully !")
