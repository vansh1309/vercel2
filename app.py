import os
import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set your OpenAI API key as an environment variable
openai.api_key = os.environ["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"]

@app.route("/chatbot", methods=["POST"])
def chatbot():
    try:
        data = request.get_json()
        question = data["question"]

        # Use the GPT-3.5 model to generate a response
        response = openai.Completion.create(
            engine="text-davinci-002",  # Use the GPT-3.5 model (text-davinci-002)
            prompt=question,
            temperature=0.7,
            max_tokens=150
        )

        answer = response.choices[0].text.strip()
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
