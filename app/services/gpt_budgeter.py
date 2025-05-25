import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_budget_tips(summary_df, top_categories):
    prompt = f"""
    Based on this monthly spending summary: {summary_df.to_dict()},
    and top spending categories: {top_categories.to_dict()},
    provide 3 smart budgeting tips.
    """

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # ✅ Model that most accounts have access to
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
