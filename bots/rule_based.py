from flask import jsonify, render_template, request

def handle_rule_based_chat():
    if request.method == 'POST':
        user_message = request.json.get('message', '').lower().strip()

        if not user_message:
            bot_response = "Please type something so I can help!"
        elif 'hello' in user_message or 'hi' in user_message or 'hey' in user_message:
            bot_response = "Hello! How can I assist you today?"
        elif 'time' in user_message:
            bot_response = "I can't tell the time yet, but your device probably can!"
        elif 'date' in user_message or 'day' in user_message:
            bot_response = "I'm not sure of the date. Try checking your calendar."
        elif 'thank' in user_message:
            bot_response = "You're welcome!"
        elif 'bye' in user_message or 'goodbye' in user_message:
            bot_response = "Goodbye! Have a great day."
        elif 'help' in user_message or 'support' in user_message:
            bot_response = "I'm here to help! Please tell me what you need assistance with."
        elif 'joke' in user_message or 'funny' in user_message:
            bot_response = "Why don’t scientists trust atoms? Because they make up everything!"
        elif 'weather' in user_message or 'forecast' in user_message:
            bot_response = "I'm not connected to weather services yet. Try a weather app!"
        else:
            bot_response = "I'm not able to understand your request. Please try asking something else."

        return jsonify({"response": bot_response})

    return render_template('rule_based.html')
