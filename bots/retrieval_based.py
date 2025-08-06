import numpy as np
from sentence_transformers import SentenceTransformer

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
