from flask import Flask

import os  # <-- Import os to get the Railway port

app = Flask(__name__)

@app.route("/")
def home():
    return "Workout Planner is running!"

# Ensure the app runs on the correct port
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))  # Use Railway-assigned port or default to 8080
    app.run(host="0.0.0.0", port=port)
