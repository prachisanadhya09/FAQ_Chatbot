import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("🤖 Smart FAQ Chatbot")

faqs = {
    "what is codealpha": "CodeAlpha is an internship platform.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "how to apply": "You can apply through the official website.",
    "what is internship": "An internship provides practical work experience.",
    "thank you": "You're welcome!"
}

questions = list(faqs.keys())
answers = list(faqs.values())

def get_best_answer(user_question):
    all_questions = questions + [user_question.lower().strip()]

    try:
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(all_questions)

        similarities = cosine_similarity(
            vectors[-1], vectors[:-1]
        ).flatten()

        best_index = similarities.argmax()

        if similarities[best_index] < 0.2:
            return None

        return answers[best_index]

    except ValueError:
        return None

question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if question.strip():
        answer = get_best_answer(question)

        if answer:
            st.success(answer)
        else:
            st.warning("Sorry, no matching answer found.")
    else:
        st.warning("Please enter your question.")
