from flask import Flask, jsonify
from models import UserManager

app = Flask(__name__)
user_manager = UserManager()

@app.route("/")
def home():
    return jsonify({"message": "Selamat datang di aplikasi DevSecOps Pipeline!", "status": "active"})

@app.route("/users")
def get_users():
    return jsonify(user_manager.get_all_users())

if __name__ == "__main__":
app.run(host="0.0.0.0", port=5000)  # nosec B104
