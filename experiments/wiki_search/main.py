# Python 3
# Choose your language, and search for articles.
import os
import requests
from dotenv import load_dotenv

load_dotenv("env/dev.env")

def authenticate() -> str:
    auth_url = "https://meta.wikimedia.org/w/rest.php/oauth2/access_token"

    auth_body = {
      "grant_type": "client_credentials",
      "client_id": os.getenv("WIKI_CLIENT_ID"),
      "client_secret": os.getenv("WIKI_CLIENT_SECRET")
    }

    response = requests.post(auth_url, data=auth_body)
    access_token = response.json()['access_token']
    # print(access_token)
    return access_token
    
def search():
    # print(os.getenv("AUTH"))

    language_code = 'en'
    search_query = 'solar system'
    number_of_results = 1
    headers = {
      'Authorization': f'Bearer {authenticate()}',
      # 'User-Agent': 'aneesh.thedevil@gmail.com'
    }

    base_url = 'https://api.wikimedia.org/core/v1/wikipedia/'
    # base_url = 'https://api.wikimedia.org/core/v1/wikipedia/en/page/Earth/bare'
    endpoint = '/search/page'
    url = base_url + language_code + endpoint
    parameters = {'q': search_query, 'limit': number_of_results}
    response = requests.get(url, headers=headers, params=parameters)

    print(response.json())

if __name__ == "__main__":
    search()
