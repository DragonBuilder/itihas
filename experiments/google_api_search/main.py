# Python 3
# Choose your language, and search for articles.
import os
import requests
from dotenv import load_dotenv

load_dotenv("env/dev.env")

def search():
    url = "https://www.googleapis.com/customsearch/v1"
    parameters = {
        "key": os.getenv("GOOGLE_SEARCH_API_KEY"),
        "cx": os.getenv("GOOGLE_SEARCH_ENGINE_ID"),
        "q": "Chankaya",
    }
    response = requests.get(url, params=parameters)
    print(response.json())

if __name__ == "__main__":
    search()
