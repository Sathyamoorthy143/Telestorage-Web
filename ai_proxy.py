from flask import Flask, request, jsonify
from google import genai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_message
        )

        return jsonify({
            "reply": response.text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run on 127.0.0.1:5000
    app.run(host="127.0.0.1", port=5000, debug=True)
