# from bots.retrieval_based import get_faq_data

# def test_fetch():
#     faqs = get_faq_data()

#     print(f"\nTotal FAQs fetched: {len(faqs)}\n")
#     for faq in faqs:
#         print(f"Q: {faq['question']}")
#         print(f"A: {faq['answer']}")
#         print(f"Keywords: {faq['keywords']}")
#         print("-" * 50)

# if __name__ == "__main__":
#     test_fetch()

from bots.retrieval_based import get_faq_data, generate_embeddings_for_faqs

faqs = get_faq_data()
faqs_with_vectors = generate_embeddings_for_faqs(faqs)

print(f"\nFirst embedding:\n{faqs_with_vectors[0]['embedding']}")
