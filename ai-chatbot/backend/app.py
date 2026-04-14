from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_response
from database import save_chat

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]

    bot_msg = get_response(user_msg)

    save_chat(user_msg, bot_msg)

    return jsonify({"response": bot_msg})

app.run(debug=True)