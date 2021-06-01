from serpapi import GoogleSearch

def localbiz(name):
    """ 
    Uses serpapi library to bring
    local business information.
    :example: localbiz('dominos')
    :param name: Local business' full name, str.
    :type name: str
    :return: Local business information
    :rtype: list
    """
    
    params = {
    "api_key": "YOUR_API_KEY",
    "engine": "google_maps",
    "q": name,
    "type": "search",
    "ll": "@40.9990779,29.0281445,16.26z",
    "google_domain": "google.com",
    "hl": "en",
    "gl": "us"
    }

    search = GoogleSearch(params)
    results = search.get_dict()['local_results']
    
    for item in results:
        print(item['title'] + " has " +
        str(item['reviews']) + " reviews" + 
        " and their rating is " +
        str(item['rating'])
        + ' and they are ' +
        item['hours'] if "hours" in item
        else print('No hours')
        )

localbiz('dominos')

#TODO Send a second request for the place to get other information.


