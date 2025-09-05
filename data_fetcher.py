"""Only data fetching functions"""
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
REQUEST_URL = "https://api.api-ninjas.com/v1/animals"

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    query_string = "?name=" + animal_name
    url = REQUEST_URL + query_string
    response = requests.get(url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        msg =  f"Error: {response.status_code} {response.text}"
        raise Exception(msg)