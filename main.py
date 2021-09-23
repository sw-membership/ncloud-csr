import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
LANGUAGE = 'Kor'

url = f'https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang={LANGUAGE}'
video_path = './audio.mp3'
result_path = './result.txt'
data = open(video_path, "rb")
headers = {
    "Content-Type": "application/octet-stream", # Fix
    "X-NCP-APIGW-API-KEY-ID": CLIENT_ID,
    "X-NCP-APIGW-API-KEY": CLIENT_SECRET,
}

response = requests.post(url, data = data, headers = headers)
rescode = response.status_code

if (rescode == 200):
    print(response.text)
    with open(result_path, 'w') as f:
        f.write(response.text)
else:
    print("Error : " + response.text)
