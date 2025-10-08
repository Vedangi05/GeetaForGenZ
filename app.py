from flask import Flask, request, jsonify
from flask_cors import CORS
from agent import StoryAgent
import os

app = Flask(__name__)
CORS(app)  # allow frontend requests

agent = StoryAgent()  # initialize your AI agent

@app.route("/story", methods=["POST"])
def generate_story():
    try:
        data = request.get_json()
        quote = data.get("quote", "")
        if not quote:
            return jsonify({"story": "⚠️ Please provide a quote/shloka"}), 400

        story = agent.create_story(quote)
        return jsonify({"story": story})
    except Exception as e:
        return jsonify({"story": f"⚠️ Error: {str(e)}"}), 500

if __name__ == "__main__":
    # app.run(port=5000)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)