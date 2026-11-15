import streamlit as st

st.title("🤖 FAQ Chatbot")

faqs = {
    "what is codealpha": "CodeAlpha is an internship platform.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "how to apply": "You can apply through the official website.",
    "what is internship": "An internship provides practical work experience.",
    "thank you": "You're welcome!"
}

question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if question:
        answer = faqs.get(question.lower().strip())

        if answer:
            st.success(answer)
        else:
            st.warning("Sorry, no matching answer found.")
    else:
        st.warning("Please enter a question.")
