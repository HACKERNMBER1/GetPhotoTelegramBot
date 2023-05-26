from flask import Flask, request, jsonify, send_file

import requests

import json

from io import BytesIO

app = Flask(__name__)

@app.route('/get_profile_photo/<int:user_id>', methods=['GET'])

def get_profile_photo(user_id):

    bot_token = "6081546024:AAGVLe1Era78QvTNw2FH2BbZJfExMOBKTf0"

    url = f'https://api.telegram.org/bot{bot_token}/getUserProfilePhotos'

    params = {

        'user_id': user_id,

        'limit': 1

    }

    response = requests.get(url, params=params)

    data = json.loads(response.text)

    file_id = data['result']['photos'][0][0]['file_id']

    file_url = f'https://api.telegram.org/bot{bot_token}/getFile?file_id={file_id}'

    response = requests.get(file_url)

    file_path = response.json()['result']['file_path']

    photo_url = f'https://api.telegram.org/file/bot{bot_token}/{file_path}'

    response = requests.get(photo_url)

    photo_bytes = BytesIO(response.content)

    return send_file(photo_bytes, mimetype='image/jpeg')

if __name__ == '__main__':

    app.run()

