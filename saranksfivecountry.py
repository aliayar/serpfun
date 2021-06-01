import requests
import json

def reqranks(filename):
    
    keywords = []
    result = {}

    with open(filename) as f:
        for line in f:
            keywords.append(line.rstrip('\n'))
    
    locations = [
        'United States',
        'Canada',
        'United Kingdom',
        'Germany',
        'France'
                ]
    
    for keyword in keywords:
        for loc in locations:
            r = requests.get(
                'https://serpapi.com/search.json?q=' + 
                keyword +
                '&api_key=YOUR_API_KEY' +
                '&loc')
            result[keyword + ' ' +loc] = json.loads(r.text)
        
    
    for item in result:
        count=0
        for serp in result[item]['organic_results']:
            if count == 0:
                if serp['link'].startswith('https://serpapi.com/'):
                    print(item + ' ' + str(serp['position']) + ' ' + serp['link'])
                    count+=1



reqranks('keywords1.txt')