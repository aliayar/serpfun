from serpapi import GoogleSearch

def reqsubs(company):
    """
    Uses serpapi library to bring
    a company's subsidiaries.
    :example: reqsubs('Apple')
    :param company: Company's full name, str.
    :type company: str
    :return: Company's subsidiaries
    :rtype: list
    """
    companies = []

    search = GoogleSearch({
        'q': f'{company} subsidiaries',
        'location': 'Manhattan, New York, United States',
        'api_key': 'YOUR_API_KEY',
        'no_cache': 'true',
        'hl': 'en',
        'gl':'us'
    })

    response = search.get_dict()['knowledge_graph']['subsidiaries']
    
    for company in response:
        companies.append(company['name'])

    print(companies)


reqsubs('Apple')

