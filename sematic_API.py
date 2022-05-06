import requests
def paper_search(offset = None,
                 limit = None,
                 fields = None,
                 query = None):
    
    # api-endpoint
    URL_BASE = 'https://api.semanticscholar.org/graph/v1/paper/search'
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'offset': offset,
              'limit':limit, 
              'fields': fields,
              'query': query}

    # add params parameters
    if offset:
        PARAMS['offset'] = offset
    if limit:
        PARAMS['limit'] = limit
    if fields:
        PARAMS['fields'] = fields
    if query:
        PARAMS['query'] = query

    # sending get request and saving the response as response object
    r = requests.get(url=URL_BASE, params=PARAMS)
    if r.status_code != 200:
        out = r.json()
        print(f"status: {out['status']}")
        print(f"Code error: {out['code']}")
        print(f"Message: {out['message']}")
    return r.json()
