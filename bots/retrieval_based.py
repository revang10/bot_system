import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from flask import request, jsonify


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_connection import get_connection


model = SentenceTransformer('all-MiniLM-L6-v2')  # 🔍 Lightweight and fast

def load_faqs_with_embeddings():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM hosp_data")
    rows = cursor.fetchall()
    conn.close()

    faqs = []
    questions = [row[0] for row in rows]
    answers = [row[1] for row in rows]
    
    # 🔍 Embed all questions at once for performance
    question_embeddings = model.encode(questions)

    for i in range(len(questions)):
        faqs.append((questions[i], answers[i], question_embeddings[i]))

    return faqs




def find_best_answer(user_question, faqs, threshold=0.6):
    user_embedding = model.encode([user_question])  # Embed user query (as a list)

    best_score = -1
    best_answer = "I'm sorry, I couldn't find a relevant answer."

    for question, answer, embedding in faqs:
        score = cosine_similarity([user_embedding[0]], [embedding])[0][0]

        if score > best_score:
            best_score = score
            best_answer = answer

    # Optional: only return if above confidence threshold
    if best_score < threshold:
        return "I'm not sure how to answer that. Could you rephrase?"

    return best_answer


# faqs = load_faqs_with_embeddings()
# response = find_best_answer("Where are you located?", faqs)
# print(response)


# 🔁 Reuse existing load function only once to avoid reloading for every request
faqs_cache = load_faqs_with_embeddings()

def handle_retrieval_based_chat():
    if request.method == 'POST':
        user_question = request.json.get("user-input", "")
        if not user_question:
            return jsonify({"response": "Please enter a valid question."})

        answer = find_best_answer(user_question, faqs_cache)
        return jsonify({"response": answer})

    # Fallback if accessed via GET
    return jsonify({"response": "Please use POST to chat."})
