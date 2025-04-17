from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

HUGGINGFACE_API = "https://smartreadshelf-smartreadsummarizer.hf.space/run/predict"

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        response = requests.post(HUGGINGFACE_API, json=request.get_json())
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)