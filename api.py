from flask import Flask, request, jsonify
import openllm

app = Flask(__name__)
llm = openllm.load("gpt2")

@app.route("/generate", methods=["POST"])
def generate_text():
    data = request.json
    prompt = data.get("prompt", "")
    response = llm(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(port=5000)
