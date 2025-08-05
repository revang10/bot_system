from flask import jsonify, render_template, request

def handle_rule_based_chat():
    if request.method == 'POST':
        user_message = request.json.get('user-input')

        if user_message and 'hello' in user_message.lower():
            bot_response = "Hello! How can I assist you today?"
        else:
            bot_response = "I am not able to understand your request. Please try again later."

        return jsonify({"response": bot_response})

    return render_template('rule_based.html')