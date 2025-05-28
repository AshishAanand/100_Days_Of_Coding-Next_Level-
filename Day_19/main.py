import streamlit as st
import joblib
# Load the pre-trained model
model = joblib.load('spam_detector.pkl')


st.title("Spam Detector App")
st.write("This is a simple spam detector app built with Streamlit.")
st.write("You can use this app to check if a message is spam or not.")
st.write("Please enter a message below:")
user_input = st.text_area("Message", placeholder="Type your message here...")
if st.button("Check"):
    if user_input:
        # Placeholder for spam detection logic
        is_spam = model.predict([user_input])[0]
        # Display the result
        if is_spam:
            st.error("This message is likely spam.")
            print(is_spam)
        else:
            st.success("This message is not spam.")
            print(is_spam)
    else:
        st.warning("Please enter a message to check.")
st.write("Developed by Ashish Ananad")
st.write("You can find the source code on [GitHub]")