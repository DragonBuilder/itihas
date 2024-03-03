# Python 3
# Choose your language, and search for articles.
import os
import requests
from dotenv import load_dotenv

load_dotenv("env/dev.env")

def search():
    url = "https://serpapi.com/search"
    parameters = {
        "api_key": os.getenv("SERP_API_KEY"),
        "q": "chanakya",
        "start": 0,
        "num": 1
    }
    response = requests.get(url, params=parameters)
    print(response.json())

if __name__ == "__main__":
    search()
