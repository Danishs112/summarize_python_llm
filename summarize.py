from openai import OpenAI
from dotenv import load_dotenv
from scrape import fetch_website_contents
import os
from app import url
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

system_prompt = """You analyse the contents of a website
 and give a short, friendly summmary. Ignore navigation menus.
 Respond in markdown."""

website = fetch_website_contents(url),
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "system", "content": system_prompt,
            "role": "user", "content": f"Summarize this website data: {website}"}
    ],
)

print(response.choices[0].message.content)