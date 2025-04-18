from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

HUGGINGFACE_API = "https://smartreadshelf-smartreadsummarizer.hf.space/run/predict"

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        if not request.is_json:
            return jsonify({"error": "Invalid content-type. Expecting application/json"}), 415
        response = requests.post(HUGGINGFACE_API, json=request.get_json())
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # use Render-provided port
    print("Picked port:", port)
    app.run(host="0.0.0.0", port=port)
