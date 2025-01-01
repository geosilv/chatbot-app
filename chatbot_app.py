import streamlit as st
import openai
from openai import OpenAIError

# Set up OpenAI API key
openai.api_key = "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"

# Streamlit app
st.title("OpenAI Chatbot")

# Initialize chat messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Use a form for user input
with st.form(key="user_input_form"):
    user_input = st.text_input("You:", key="user_input")
    submit_button = st.form_submit_button(label="Send")

if submit_button and user_input:
    # Add user input to the conversation history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # OpenAI API call
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if available
            messages=st.session_state.messages,  # Use updated 'messages' syntax
        )
        # Extract the assistant's reply
        assistant_message = response["choices"][0]["message"]["content"]
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})

    except OpenAIError as e:
        st.error(f"OpenAI API error: {e}")

# Display the conversation history
st.write("### Conversation History")
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**Assistant:** {message['content']}")
