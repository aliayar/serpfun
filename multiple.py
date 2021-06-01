from serpapi import GoogleSearch
import aiohttp
import asyncio
import time

start_time = time.time()


async def main():
    
    keywords = []
    results = []
    
    with open('keywords.txt') as f:
        for line in f:
            keywords.append(line.rstrip('\n'))

    async with aiohttp.ClientSession() as session:

        for keyword in keywords:
            r = 'https://serpapi.com/search.json?q=' + keyword + '&async=True' + '&api_key=YOUR_API_KEY'
            async with session.get(r) as resp:
                result = await resp.json()
                results.append(result['search_metadata']['id'])
    
    async with aiohttp.ClientSession() as session:

        for id in results:
            r = 'https://serpapi.com/searches/' + id + '.json?api_key=YOUR_API_KEY'
            async with session.get(r) as resp:
                result = await resp.json()
                print(result['search_parameters']['q'])
                for rank in result['organic_results']:
                    print(str(rank['position']) + ' ' + rank['link'])

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
