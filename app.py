from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure the Gemini API
API_KEY = "AIzaSyByUnAzut8c-MMBgD1EtzDDBIntCZwXHC4"
genai.configure(api_key=API_KEY)

# Initialize chatbot model
model = genai.GenerativeModel("gemini-pro")
chat_session = model.start_chat()

# Serve the HTML page
@app.route("/")
def home():
    return render_template("chat.html")

# Handle chatbot responses
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # Custom responses
    if user_message.lower() in ["what is your name?", "who are you?"]:
        bot_response = "My name is AUE-Chatbot!"
    elif user_message.lower() in ["what is your version?", "what version are you?"]:
        bot_response = "I am version 1.0."
    else:
        response = chat_session.send_message(user_message)
        bot_response = response.text if response else "Sorry, I couldn't understand that."

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
