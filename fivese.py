from serpapi import GoogleSearch

def fivesearch():

    engineresults = {}

    engines = [
        'google',
        'Baidu',
        'bing',
        ]

    for engine in engines:
        search = GoogleSearch({
                                "api_key": "YOUR_API_KEY",
                                "engine": engine,
                                "q": "serpapi",
                                })
        results = search.get_dict()
        engineresults[engine] = results
    
    params = {
            "engine": "yandex",
            "text": "serpapi",
            "api_key": "YOUR_API_KEY"
            }

    search = GoogleSearch(params)
    results = search.get_dict()
    engineresults['yandex'] = results

    params = {
            "engine": "yahoo",
            "p": "serpapi",
            "api_key": "YOUR_API_KEY",
            'no_cache': 'True'
            }

    search = GoogleSearch(params)
    results = search.get_dict()
    engineresults['yahoo'] = results



    for item in engineresults:
        print(item)
        for serp in engineresults[item]['organic_results']:
                if item == 'Baidu' and 'displayed_link' in serp.keys():
                    print(str(serp['position']) + ' ' + serp['displayed_link'])
                if 'link' in serp.keys():
                    print(str(serp['position']) + ' ' + serp['link'])


fivesearch()