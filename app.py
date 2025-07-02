import streamlit as st
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=st.secrets["API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("💬 Text Message Sentiment Analyzer")

st.markdown("""
Analyze the tone of your messages and get AI-powered suggestions to improve or adjust your communication!
""")

# User input
user_message = st.text_area("Enter your text message:")

if st.button("Analyze Sentiment"):
    if not user_message.strip():
        st.error("Please enter a message to analyze.")
    else:
        prompt = f"""
        Analyze the following text message for sentiment. Tell me if it is Positive, Negative, or Neutral.
        Then, provide:
        - A short explanation of why it is categorized that way.
        - Suggestions on how to make it sound more positive or polite, if needed.
        - Keep it short, friendly, and easy to understand.

        Message: {user_message}
        """

        with st.spinner("Analyzing with Gemini..."):
            response = model.generate_content(prompt)
            analysis = response.text

        st.subheader("🔎 Analysis Result")
        st.markdown(analysis)

st.caption("✨ Built with Python, Streamlit & Gemini API")
