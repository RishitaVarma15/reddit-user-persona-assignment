# Reddit User Persona Generator
# Requirements: requests, openai (if using GPT), or use basic analysis

import requests
import os
import time

# --- SETUP ---
HEADERS = {'User-Agent': 'Mozilla/5.0'}

# Optional: Use OpenAI GPT to build persona (requires API key)
USE_OPENAI = False
OPENAI_API_KEY = "your_openai_api_key"

# --- FUNCTIONS ---
def fetch_json(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch {url} - Status Code: {response.status_code}")
        return None

def extract_user_data(username):
    base_url = f"https://www.reddit.com/user/{username}"
    posts = fetch_json(base_url + "/submitted/.json")
    comments = fetch_json(base_url + "/comments/.json")

    all_texts = []
    citations = []

    if posts:
        for post in posts['data']['children']:
            title = post['data'].get('title', '')
            text = post['data'].get('selftext', '')
            permalink = post['data'].get('permalink', '')
            full_text = f"POST: {title}\n{text}"
            all_texts.append(full_text)
            citations.append(f"https://reddit.com{permalink}")

    if comments:
        for comment in comments['data']['children']:
            body = comment['data'].get('body', '')
            permalink = comment['data'].get('permalink', '')
            all_texts.append(f"COMMENT: {body}")
            citations.append(f"https://reddit.com{permalink}")

    return all_texts, citations

def build_persona(texts):
    if USE_OPENAI:
        import openai
        openai.api_key = OPENAI_API_KEY

        joined = "\n".join(texts[:10])  # limit input size
        prompt = f"""
Analyze the following Reddit posts and comments, and write a persona with traits, tone, interests, and behaviors. Include quotes as evidence:

{joined}

Persona:
"""
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    else:
        # Simple manual summary
        keywords = {}
        for text in texts:
            for word in text.lower().split():
                if len(word) > 4:
                    keywords[word] = keywords.get(word, 0) + 1
        top_keywords = sorted(keywords.items(), key=lambda x: x[1], reverse=True)[:10]
        persona = "Likely interests include: " + ", ".join([k for k, _ in top_keywords])
        return persona

def save_persona(username, persona, citations):
    with open(f"{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(f"Reddit User Persona: {username}\n\n")
        f.write(persona + "\n\n")
        f.write("Citations (source posts/comments):\n")
        for cite in citations:
            f.write(f"- {cite}\n")

usernames = ["kojied", "Hungry-Move-6603"]

for username in usernames:
    texts, citations = extract_user_data(username)
    persona = build_persona(texts)
    save_persona(username, persona, citations)
    print(f"Done with {username}")
