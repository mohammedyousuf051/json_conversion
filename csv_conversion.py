import pandas as pd
from downloadjson import *


def csv_conversion(input_json):
    """
    this func converts the trackerwise json to csv file and saves it inside the output folder
    """
    tracking_id, frame_id, label = [], [], []
    for tracker_data in input_json['answer_key']['video2d']['data']['trackers']:
        for frame in tracker_data['frames']:
            tracking_id.append(tracker_data['_id'])
            frame_id.append(frame)
            label.append(tracker_data['frames'][frame]['label'])

    result = {
        'frame_id': frame_id,
        'tracking_id': tracking_id,
        'label': label
    }
    df = pd.DataFrame(result)
    df.to_csv('output\\tracker.csv', index=False)

    return "success"



def convert_csv(url):
    """
    this func will receive the json data and status code from dwonloadjson module and call the conversion func if status code 200
    """
    status, input_json = download_json(url)
    if status:
        csv_conversion(input_json)
        return "success"
    else:
        print("status received",status)
        return None



if __name__ == '__main__':
    json_url = "https://api.jsonbin.io/b/5de5fae79987a06bfbea6f46"
    convert_csv(json_url)