from typing import Dict

import requests

BASE_URL = "https://www.googleapis.com/customsearch/v1"

def search(query, cx=None, key=None) -> Dict:
    if cx is None:
        raise Exception("CX Required. Please see https://joeyism.medium.com/custom-google-search-api-fbbafe4711eb on how to obtain the API Key")

    if key is None:
        raise Exception("API Key required. Please see https://joeyism.medium.com/custom-google-search-api-fbbafe4711eb on how to obtain the API Key")

    req = requests.get(BASE_URL, params={"q": query, "key": key, "cx": cx})
    return req.json()
