from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "Flask CI/CD Microservice",
        "version": "1.0.0",
        "status": "online",
        "message": "Welcome to the CI/CD learning project!"
    }), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }), 200

@app.route("/api/add", methods=["POST"])
def add_numbers():
    data = request.get_json() or {}
    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Missing required parameters 'a' and 'b'"}), 400

    try:
        result = float(a) + float(b)
        return jsonify({"a": a, "b": b, "result": result}), 200
    except (ValueError, TypeError):
        return jsonify({"error": "Parameters 'a' and 'b' must be numbers"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
