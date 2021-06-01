from serpapi import GoogleSearch

def tenlocations():

    tenlocresults = {}

    locations = [
        'Los Angeles, California, United States',
        'Austin, Texas, United States',
        'Manhattan, New York',
        'Copenhagen, Denmark',
        'Helsinki, Finland',
        'Berlin, Germany',
        'Paris, France',
        'Warsaw, Poland',
        'Istanbul, Turkey',
        'Tokyo, Japan'
    ]

    for loc in locations:
        search = GoogleSearch({
                                "api_key": "YOUR_API_KEY",
                                "engine": "google",
                                "q": "serpapi",
                                "google_domain": "google.com",
                                "gl": "us",
                                "hl": "en",
                                "location":loc
                                })
        results = search.get_dict()
        tenlocresults[loc] = results

    for item in tenlocresults:
        print(tenlocresults[item]['search_parameters']['location_used'])
        for serp in tenlocresults[item]['organic_results']:
            print(str(serp['position']) + ' ' + serp['link'])

tenlocations()