import os
import random
import telegram
import argparse
from time import sleep
from dotenv import load_dotenv


def main():
    
    time_delay = 4

    parser = argparse.ArgumentParser(
        description='отправка фотографий в telegram канал'
    )
    parser.add_argument('--periodicity_time', type= int, help='время задержни сводки фото в секундах', default=14400)
    args = parser.parse_args()

    load_dotenv()
    tg_bot_key = os.getenv("TG_BOT_KEY")
    tg_chanal_name = os.getenv("TG_CHANNEL_NAME")

    bot = telegram.Bot(token=tg_bot_key)
    bot.send_message(text='Hi John!', chat_id=tg_chanal_name)

    while True:
        all_files = os.walk("images")

        for array_of_files in all_files:
            folder, nested_folder, files = array_of_files
            random.shuffle(files)

            for tg_file_image in files:
                with open(f"images/{tg_file_image}", "rb") as file:
                    bot.send_document(chat_id=tg_chanal_name, document=file)
                sleep(time_delay)
        sleep(args.periodicity_time)


if __name__ == '__main__':
    main()