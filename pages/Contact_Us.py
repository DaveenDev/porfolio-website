import streamlit as st
import send_email

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your Email: ")
    subject = st.text_input("Subject: ")
    message = st.text_area("Message: ")
    submit_btn = st.form_submit_button("Submit")

    if submit_btn:
        send_email.send(user_email, subject, message)
        st.info("email was sent")
