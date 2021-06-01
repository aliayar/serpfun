import aiohttp
import asyncio
import time
import json

start_time = time.time()

def getkeywords():

    keywords = []
    with open('keywords.txt') as f:
        for line in f:
            keywords.append(line.rstrip('\n'))
    return keywords
    
async def main():

    result = {}
    
    async with aiohttp.ClientSession() as session:

        for keyword in getkeywords():
            r = 'https://serpapi.com/search.json?q=' + keyword + '&api_key=YOUR_API_KEY&hl=en&gl=us&no_cache=True'
            async with session.get(r) as resp:
                output = await resp.json()
                result[keyword] = output
    
    print("--- %s seconds ---" % (time.time() - start_time))

    for item in result:
        count=0
        for serp in result[item]['organic_results']:
            if count == 0:
                if serp['link'].startswith('https://serpapi.com/'):
                    print(item + ' ' + str(serp['position']) + ' ' + serp['link'])
                else:
                    print(item + ' ' + 'not in the first page.')
                    count+=1

asyncio.run(main())

# With no cache, takes 696.0895049571991 seconds before printing
#                      696.1489968299866 seconds after printing.
# Why so long?

