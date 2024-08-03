import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="ChatGPT-like Chatbot", page_icon="🤖")

# Title for the Streamlit app
st.title("ChatGPT-like Chatbot")

# Embed the Langflow chat using HTML component
chatbot_html = """
    <script src="https://cdn.jsdelivr.net/gh/logspace-ai/langflow-embedded-chat@v1.0.4/dist/build/static/js/bundle.min.js"></script>
    <langflow-chat
        window_title="Basic Prompting (Hello, World)"
        flow_id="9f7f38bb-e82f-4711-a885-4c124dd48745"
        host_url="http://localhost:7860"
    ></langflow-chat>
"""

# Display the chatbot within the Streamlit app
st.components.v1.html(chatbot_html, height=600, scrolling=True)

# Add some explanation or instructions if needed
st.markdown("""
    ### Instructions
    - Type your message in the chat box.
    - The chatbot will respond in real-time.
    - Enjoy the conversation!
""")
