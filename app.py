import requests
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

API_KEY = os.getenv("HEVY_API_KEY")
BASE_URL = "https://api.hevy.com/v1"

headers = {
    "api-key": API_KEY,
    "Content-Type": "application/json",
    "accept": "application/json"
}

@app.route('/api/workouts/all', methods=['GET'])
def get_all_workouts_endpoint():
    try:
        page = int(request.args.get('page', 1))
        pageSize = int(request.args.get('pageSize', 5))
        response = requests.get(
            f"{BASE_URL}/workouts",
            headers=headers,
            params={"page": page, "pageSize": pageSize}
        )
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching workouts: {e}")
        return jsonify({"error": "Failed to fetch workouts"}), 500

@app.route('/api/workouts/count', methods=['GET'])
def get_workouts_count_endpoint():
    try:
        response = requests.get(
            f"{BASE_URL}/workouts/count",
            headers=headers
        )
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching workout count: {e}")
        return jsonify({"error": "Failed to fetch workout count"}), 500

if __name__ == "__main__":
    if not API_KEY:
        print("Error: HEVY_API_KEY is not set in the environment")
        exit(1)
    print(f"Starting Flask server with API_KEY: {API_KEY[:4]}****")
    app.run(debug=True, host='0.0.0.0', port=5000)