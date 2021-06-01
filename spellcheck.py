from serpapi import GoogleSearch
import serpapi

def spellcheck(q):

    params = {
    "q": q,
    "hl": "en",
    "gl": "us",
    "api_key": "YOUR_API_KEY"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    search_information = results['search_information']['spelling_fix']
    print('Correct search term is: ' + search_information)

spellcheck('comands')
