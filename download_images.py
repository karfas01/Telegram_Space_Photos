import requests
import os


def download_photo(filename, url, payload=""):

    foldername = 'images'
    full_path = f"{foldername}/{filename}"

    os.makedirs(foldername, exist_ok=True)

    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(full_path, 'wb') as file:
        file.write(response.content)