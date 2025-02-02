import openai
import config

openai.api_key = config.OPENAI_API_KEY


def generate_plan(goal, diet):
    prompt = f"Create a workout and meal plan for a person whose goal is {goal} and follows a {diet} diet."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a fitness and nutrition expert."},
                  {"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
