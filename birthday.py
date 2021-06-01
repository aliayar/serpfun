import requests
import json

def rawreq(person):
    """
    Uses GET request to bring
    a famous person's birthday.
    :param person: Person's full name, str.
    :type person: str
    :return: Person's birthday
    :rtype: str
    """
    r = requests.get(
        'https://serpapi.com/search.json?q=' + 
        person +
        '&api_key=YOUR_API_KEY')
    response = json.loads(r.text)['knowledge_graph']['born']
    print(f'{person} was born in {response}')

# rawreq('Jean Seberg')

from serpapi import GoogleSearch

def libreq(person):
    """
    Uses serpapi library to bring
    a famous person's birthday.
    :param person: Person's full name, str.
    :type person: str
    :return: Person's birthday
    :rtype: str
    """
    search = GoogleSearch({
        'q': person,
        'location': 'Manhattan, New York',
        'api_key': 'YOUR_API_KEY'
    })
    response = search.get_dict()['knowledge_graph']['born']
    print(f'{person} was born in {response}')

# libreq('Jean Seberg')