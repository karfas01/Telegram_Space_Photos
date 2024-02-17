import os
from dotenv import load_dotenv
import requests

from download_images import download_photo


def get_epic_images(nasa_key):

    number_of_repetitions = 4

    payload = {"api_key": nasa_key}
    epic_url = "https://api.nasa.gov/EPIC/api/natural/images"
    epic_response = requests.get(epic_url, params=payload)
    epic_response.raise_for_status()
    decrypted_epic_response = epic_response.json()
    for epic_picture_number in range(number_of_repetitions):
        epic_picture = decrypted_epic_response[epic_picture_number]
        img_name = f"{epic_picture['image']}.png"
        date = epic_picture["date"].split()[0]
        date_year = date.split("-")[0]
        date_month = date.split("-")[1]
        date_day = date.split("-")[2]
        epic_img_url = f"https://api.nasa.gov/EPIC/archive/natural/{date_year}/{date_month}/{date_day}/png/{img_name}"
        filename = f"EPIC_picture_{epic_picture_number}.png"
        download_photo(filename, epic_img_url, payload)


def main():
    load_dotenv()
    nasa_key = os.getenv("NASA_KEY")
    get_epic_images(nasa_key)


if __name__ == '__main__':
    main()