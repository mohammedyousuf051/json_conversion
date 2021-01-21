from collections import defaultdict
from downloadjson import *


def callconversion(input_json):
    """
    this func converts the trackerwise json to framewise json and returns it
    """
    result = {'frames' : defaultdict(list)}

    for tracker_data in input_json['answer_key']['video2d']['data']['trackers']:
        for frame in tracker_data['frames']:
            tracker_data['frames'][frame].update({'tracker_id':tracker_data['_id']})
            temp = tracker_data['frames'][frame]
            result['frames'][frame].append(temp)

    input_json['answer_key']['video2d']['data'] = result

    return input_json


def convert_json(url):
    """
    this func will receive the json data and status code from dwonloadjson module and call the conversion func if status code 200
    """
    status,input_json = download_json(url)
    if status:
        return callconversion(input_json)
    else:
        print("status received", status)
        return None


if __name__ == '__main__':
    json_url = "https://api.jsonbin.io/b/5de5fae79987a06bfbea6f46"
    converted_json = convert_json(json_url)
    if converted_json:
        with open("output\\frame.json", "w") as outfile:
        	json.dump(converted_json,outfile,indent=4)

