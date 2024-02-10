import requests
import argparse

from download_images import download_photo


def fetch_spacex_last_launch(img_id):
    spacex_url = f'https://api.spacexdata.com/v5/launches/{img_id}'
    response_spacex = requests.get(spacex_url)
    response_spacex.raise_for_status()
    spacex_links = response_spacex.json()["links"]
    spacex_photos = spacex_links["flickr"]["original"]
    for image_number, spacex_photo_url in enumerate(spacex_photos):
        filename = f'SpaceX_photo_{image_number}.jpeg'
        download_photo(filename, spacex_photo_url)


def main():

    parser = argparse.ArgumentParser(
        description='получение фото запусков'
    )
    parser.add_argument('--id', help='id нужного вам запуска', default="5eb87d47ffd86e000604b38a")
    args = parser.parse_args()

    fetch_spacex_last_launch(args.id)


if __name__ == '__main__':
    main()