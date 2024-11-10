# app.py

import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure the gemini-pro model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Streamlit app UI
st.title("CyberSecurity Specialist")
st.write("Tell us about your issue.")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# User input
user_input = st.text_input("You:", "")

# Generate response
if user_input:
    # Append user input to chat history
    st.session_state["chat_history"].append(("User", user_input))
    
    # Generate response from gemini-pro model
    response = model.generate_content(f"As an CyberSecurity Specialist tell me my incidence reponse for : {user_input}")
    
    # Append bot response to chat history
    bot_reply = response.text
    st.session_state["chat_history"].append(("Bot", bot_reply))
    
    # Display the response
    st.text_area("Expert:", bot_reply, height=150)

# Display chat history
for role, message in st.session_state["chat_history"]:
    if role == "User":
        st.write(f"**You:** {message}")
    else:
        st.write(f"**Expert:** {message}")