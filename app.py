from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Docker + Flask! This is a simple web application running inside a Docker container."

@app.route("/user")
def user():
    return "Hello User! This is a user-specific endpoint. I am chaning the code to test the hot reload feature of Flask in development mode."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)