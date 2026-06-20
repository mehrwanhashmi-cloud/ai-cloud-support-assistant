from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Cloud Support Assistant is running."

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")

    return jsonify({
        "question": question,
        "answer": "Bedrock integration will be added next."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
