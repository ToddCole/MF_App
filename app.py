from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from services.workout_api import get_workout_data
from services.nutrition_api import get_nutrition_data

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return "Welcome to the AI Workout & Nutrition Planner"

@app.route('/workout', methods=['GET'])
def workout():
    category_id = request.args.get('category', 10)  # Default to Abs (10)
    data = get_workout_data(category_id)
    return jsonify(data)

@app.route('/nutrition', methods=['GET'])
def nutrition():
    data = get_nutrition_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
