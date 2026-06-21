import json
import boto3
from flask import Flask, request, jsonify

app = Flask(__name__)

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

MODEL_ID = "amazon.nova-lite-v1:0"
@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Cloud Support Assistant</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 40px auto;
                padding: 20px;
                background: #f7f9fb;
                color: #222;
            }
            .card {
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            }
            textarea {
                width: 100%;
                font-size: 16px;
                padding: 12px;
                border-radius: 8px;
                border: 1px solid #ccc;
            }
            button {
                margin-top: 15px;
                padding: 12px 20px;
                font-size: 16px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }
            pre {
                white-space: pre-wrap;
                background: #f1f5f9;
                padding: 15px;
                border-radius: 8px;
                line-height: 1.5;
            }
            .examples button {
                margin: 5px;
                padding: 8px 12px;
                font-size: 14px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>AI Cloud Support Assistant</h1>
            <p>Ask an AWS troubleshooting or cloud engineering question.</p>

            <textarea id="question" rows="5"
            placeholder="Example: Why can't my EC2 instance connect to the internet?"></textarea>

            <br>
            <button onclick="askAI()">Ask AI</button>

            <div class="examples">
                <h3>Example Questions</h3>
                <button onclick="setQuestion('What is the difference between a Security Group and a NACL?')">Security Group vs NACL</button>
                <button onclick="setQuestion('How do I troubleshoot an ECS task that keeps stopping?')">ECS troubleshooting</button>
                <button onclick="setQuestion('What is the difference between an ALB and an NLB?')">ALB vs NLB</button>
                <button onclick="setQuestion('Explain NAT Gateway in simple terms.')">NAT Gateway</button>
            </div>

            <h3>Response:</h3>
            <pre id="response">Your answer will appear here.</pre>
        </div>

        <script>
        function setQuestion(text) {
            document.getElementById("question").value = text;
        }

        async function askAI() {
            const question = document.getElementById("question").value;
            const responseBox = document.getElementById("response");

            responseBox.textContent = "Thinking...";

            try {
                const response = await fetch("/ask", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        question: question
                    })
                });

                const data = await response.json();
                responseBox.textContent = data.answer || "No answer returned.";
            } catch (error) {
                responseBox.textContent = "Error: Could not get a response.";
            }
        }
        </script>
    </body>
    </html>
    """
@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "")

    prompt = f"""
You are an AI Cloud Support Assistant.
Answer clearly and practically for a junior cloud engineer.

Question:
{question}
"""

    body = {
        "messages": [
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 500,
            "temperature": 0.4
        }
    }

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body)
    )

    response_body = json.loads(response["body"].read())
    answer = response_body["output"]["message"]["content"][0]["text"]

    return jsonify({
        "question": question,
        "answer": answer
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
