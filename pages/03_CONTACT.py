import streamlit as st


st.title("📧 Contact Page")
st.write("Feel free to reach out through the form below.")

# Create a contact form
with st.form(key="contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    # Submit button
    submit_button = st.form_submit_button("Send")

    if submit_button:
        st.success(f"Thank you, {name}! We'll get back to you soon.")
