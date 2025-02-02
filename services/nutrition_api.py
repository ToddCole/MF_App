import requests
import config

import requests
import config


def get_nutrition_data():
    """
    Fetch nutrition data from the WGER API.
    """
    url = f"{config.WGER_BASE_URL}/ingredient/"
    headers = {"Authorization": f"Token {config.WGER_API_KEY}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Returns nutrition data
    else:
        return {"error": f"Failed to fetch nutrition data. Status code: {response.status_code}"}
