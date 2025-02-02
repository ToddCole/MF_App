import requests
import re
from langdetect import detect
import config


def clean_html(raw_text):
    """Remove HTML tags from text."""
    clean_text = re.sub(r'<.*?>', '', raw_text)  # Removes all HTML tags
    return clean_text.strip()  # Removes extra spaces


def is_english(text):
    """Check if the text is in English."""
    try:
        return detect(text) == "en"
    except:
        return False  # If detection fails, assume non-English


def get_equipment_name(equipment_ids):
    """Fetch equipment names from WGER API given a list of equipment IDs."""
    url = f"{config.WGER_BASE_URL}/equipment/"
    headers = {"Authorization": f"Token {config.WGER_API_KEY}"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        equipment_data = response.json()
        id_to_name = {item["id"]: item["name"] for item in equipment_data["results"]}
        return [id_to_name.get(e_id, "Unknown") for e_id in equipment_ids]
    return ["Unknown"]


def get_workout_data(category_id=10, language=2):
    """Fetch workout exercises from WGER API and include equipment names."""
    url = f"{config.WGER_BASE_URL}/exercise/"
    headers = {"Authorization": f"Token {config.WGER_API_KEY}"}

    params = {"category": category_id, "language": language}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        exercises = []
        for exercise in data["results"]:
            equipment_names = get_equipment_name(exercise.get("equipment", []))
            clean_description = clean_html(exercise.get("description", "No description available."))

            # Filter out non-English exercises
            if is_english(clean_description):
                exercises.append({
                    "name": exercise.get("name", "Unknown"),
                    "description": clean_description if clean_description else "No description available.",
                    "equipment": equipment_names,
                    "id": exercise.get("id")
                })

        return {"count": len(exercises), "exercises": exercises}

    else:
        return {"error": f"Failed to fetch workouts. Status code: {response.status_code}"}
