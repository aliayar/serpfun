import aiohttp
import asyncio
import time

start_time = time.time()

def getkeywords():

    keywords = []
    with open('keywords.txt') as f:
        for line in f:
            keywords.append(line.rstrip('\n'))
    return keywords

async def get_serps(session, r):
    async with session.get(r) as resp:
        serp = await resp.json()
        return serp


async def main():

    result = {}

    async with aiohttp.ClientSession() as session:

        tasks = []
        for keyword in getkeywords():
            r = 'https://serpapi.com/search.json?q=' + keyword + '&api_key=YOUR_API_KEY&hl=en&gl=us&no_cache=True'
            tasks.append(asyncio.ensure_future(get_serps(session, r)))

        original_serps = await asyncio.gather(*tasks)
        for serpresult in original_serps:
            result[serpresult['search_parameters']['q']] = serpresult

    for item in result:
        count=0
        for serp in result[item]['organic_results']:
            if count == 0:
                if serp['link'].startswith('https://serpapi.com/'):
                    print(item + ' ' + str(serp['position']) + ' ' + serp['link'])
                    count+=1

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))

## --- 20.398730754852295 seconds ---