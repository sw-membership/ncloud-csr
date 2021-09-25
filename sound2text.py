import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

LANGUAGE = 'Kor'
URL = f'https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang={LANGUAGE}'
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
HEADERS = {
    "Content-Type": "application/octet-stream",
    "X-NCP-APIGW-API-KEY-ID": CLIENT_ID,
    "X-NCP-APIGW-API-KEY": CLIENT_SECRET,
}


def sound2text(video_path):
    data = open(video_path, "rb")

    response = requests.post(URL, data=data, headers=HEADERS)

    if (response.status_code == 200):
        text = json.loads(response.text)
        return text['text']
    else:
        return f'Error: {response.text}'
