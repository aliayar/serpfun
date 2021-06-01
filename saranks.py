import requests
import json
import time

start_time = time.time()

def reqranks(filename):

    keywords = []
    result = {}
    
    with open(filename) as f:
        for line in f:
            keywords.append(line.rstrip('\n'))
    
    
    for keyword in keywords:
        r = requests.get(
            'https://serpapi.com/search.json?q=' + 
            keyword +
            '&api_key=YOUR_API_KEY&hl=en&gl=us&no_cache=True')
        result[keyword] = json.loads(r.text)
    
    print("--- %s seconds ---" % (time.time() - start_time))    
    
    for item in result:
        count=0
        for serp in result[item]['organic_results']:
            if count == 0:
                if serp['link'].startswith('https://serpapi.com/'):
                    print(item + ' ' + str(serp['position']) + ' ' + serp['link'])
                    count+=1

reqranks('keywords.txt')

# With no cache, takes 652.8980522155762 seconds before printing
#                      652.9503345489502 seconds after printing.