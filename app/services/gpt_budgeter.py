import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_budget_tips(summary, categories):
    prompt = f"""
    Based on the following summary of spending by month: {summary.to_dict()},
    and top categories: {categories.to_dict()},
    give 3 personalized budgeting tips.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
