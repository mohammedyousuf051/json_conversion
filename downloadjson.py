import requests,json

"""
this is a common funtion for getting the json from request url, for reusablity of code it has created as an separate module
"""


def download_json(url):
    """
    this func get the request url and return the data in json format
    """

    response = requests.get(url)
    request_status = False
    data_resp = None
    if response.status_code == 200:
        data_resp = response.json()
        request_status = True
    else:
        print("unexpected response {}".format(response))
    return request_status, data_resp


