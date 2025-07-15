# Reddit User Persona Generator

This project is a **48-hour internship assignment** for BeyondChats. It demonstrates scraping Reddit user data, analyzing posts and comments, and generating a simple user persona with supporting citations.

---

## 📌 Project Overview

Given a Reddit username, this script:
- Scrapes all posts and comments from the user using Reddit’s public `.json` endpoints.
- Analyzes the text to build a user persona highlighting interests, tone, and behaviors.
- Outputs the persona in a `.txt` file along with direct links to posts/comments as evidence.

---

## ✅ Features

- Takes multiple Reddit usernames as input.
- Simple scraping — no official Reddit API key required.
- Optionally uses OpenAI GPT for richer persona generation.
- Outputs clear `.txt` files for each user with citations.
- Follows PEP-8 guidelines for Python code.

---

## 🚀 Requirements

- **Python 3.7+**
- Libraries:
  - `requests`
  - `openai` (optional, if you enable GPT)

Install dependencies:
```bash
pip install requests openai
