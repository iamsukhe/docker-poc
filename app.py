from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health_check():
    """
    Standard health check endpoint to verify the service is up.
    """
    return jsonify({
        "status": "healthy",
        "container": "active"
    }), 200 

@app.route("/api/data", methods=["GET", "POST"])
def handle_data():
    if request.method == "GET":
        return jsonify({
            "message": "This is a GET request!",
            "status": "success"
        }), 200

    if request.method == "POST":
        data = request.json  
        if not data:
            return jsonify({"error": "No data provided"}), 400

        name = data.get("name", "Unknown")
        return jsonify({
            "message": f"Data received for {name}!",
            "received_data": data,
            "status": "success"
        }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)