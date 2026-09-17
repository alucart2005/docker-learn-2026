from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    base_url=os.environ.get("LLM_URL", "http://model-runner.docker.internal/v1/"),
    api_key="no-es-necesaria"
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask")
def ask():
    question = request.args.get("q", "¿Qué es un contenedor de Docker?")
    try:
        response = client.chat.completions.create(
            model="ai/smollm2",
            messages=[{"role": "user", "content": question}],
            max_tokens=100
        )
        return jsonify({
            "question": question,
            "answer": response.choices[0].message.content,
            "tokens": response.usage.total_tokens
        })
    except Exception as e:
        return jsonify({
            "error": str(e),
            "message": "Asegúrate de haber corrido 'docker model pull ai/smollm2' en tu Host antes de llamar este endpoint."
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
