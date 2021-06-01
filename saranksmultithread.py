import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

start_time = time.time()

apireqs = {}

def reqtoserp(link):
    r = requests.get(link)
    response = json.loads(r.text)
    return response

def reqranks(filename):
   
    keywords = []
    results = {}
    
    with open(filename) as f:
        for line in f:
            keywords.append(line.rstrip('\n'))
    
    for keyword in keywords:
        r = 'https://serpapi.com/search.json?q=' + keyword + '&api_key=YOUR_API_KEY&hl=en&gl=us&no_cache=True&location=Austin%2C+Texas%2C+United+States'
        apireqs[keyword] = r

    threads= []
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url in apireqs.keys():
            threads.append(executor.submit(reqtoserp, apireqs[url]))
        
        for task in as_completed(threads):
            results[task.result()['search_parameters']['q']] = task.result()
    

    print("--- %s seconds ---" % (time.time() - start_time))
    
    for item in results:
        isserp = False
        count=0
        for serp in results[item]['organic_results']:
            if count == 0:
                if serp['link'].startswith('https://serpapi.com/'):
                    print(item + ' ' + str(serp['position']) + ' ' + serp['link'])
                    count+=1



reqranks('keywords1.txt')

# With 4 workers:
## 675.8903057575226 seconds before printing.
## 675.9279325008392 seconds after printing.

# With 2 workers:
## 808.905341386795 seconds before printing.
## 808.9475939273834 seconds after printing.

# With 8 workers
# 755.0360751152039 seconds seconds before printing.