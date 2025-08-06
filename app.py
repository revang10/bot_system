from flask import Flask, render_template, request, jsonify
from bots.rule_based import handle_rule_based_chat
from bots.retrieval_based import handle_retrieval_based_chat


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')


# # RULE BASED ROUTE
@app.route('/rule-based')
def rule_based_page():
    return render_template('rule_based.html')

@app.route('/chat/rule-based', methods=['GET', 'POST'])
def rule_based():
    return handle_rule_based_chat()



# RETRIEVAL BASED ROUTE


@app.route('/retrieval-based')
def retrieval_based():
    return render_template('retrieval_based.html')

@app.route("/chat/retrieval-based", methods=["POST"])
def retrieval_chat():
    return handle_retrieval_based_chat()




@app.route('/llm-api')
def llm_api():
    return render_template('llm_api.html')




@app.route('/local-llm')
def local_llm():
    return render_template('local_llm.html')




@app.route('/fine-tuned')
def fine_tuned():
    return render_template('fine_tuned.html')




@app.route('/rag-based')
def rag_based():
    return render_template('rag_based.html')




if __name__ == '__main__':
    app.run(debug=True)
