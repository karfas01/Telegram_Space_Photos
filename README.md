# Космический Telegram.

Программа создана для получения фотографий каосмоса из 3-х источников и парсинг их через telegram-bot в telegram канал.

## Как установить / Требования для работы:

### Для работы требуется:

- Python версии [3.12.1](https://www.python.org/downloads/release/python-3121/) и выше должен быть уже установлен.
Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей воспользуйтель данной комндой:
```
pip install -r requirements.txt
```

- Для работы программы в дерриктории программы должен быть создан файл `.env`, с следующем содержимым:
```
KEY_NASA="token_NASA_APIs"
KEY_BOT="token_telegram_bot"
CHANNEL_NAME="@Telegram_Channel_Name"
```
Чтобы получить token от: [NASA APIs](https://api.nasa.gov/).

Чтобы получить token от telegram_bot воспользуйтесь: [BotFather](https://t.me/BotFather) и добавте Telegram бота в telegram канал по [этим](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/) пунктам - настройкам (канала).

## Как пользоваться:

### Для скачивания фотографий из SpaceX:

- Запустите скрипт вставив ID нужного вам запуска:
```
python fetch_spacex_images.py --id здесь ваш id запуска
```
- Есть второй вориант запуска без ID тогда будут загружены фото с последнего запуска SpaceX:
```
python fetch_spacex_images.py
```

### Для скачивания фотографий из EPIC-NASA:

- Запустить скрипт:
```
python fetch_NASA_EPIC_images.py
```

### Для скачивания фотографий из APOD-NASA:

1. Запустить скрипт, указав желаемое кол-во фотографий для скачивания.
1. Команда для запуска скриптa:
```
python fetch_NASA_APOD_images.py --c 50
```
   
-  Если кол-во не указано, то устанавливается кол-во по умолчанию равное 50.

1. Команда для запуска скриптa:
```
python fetch_NASA_APOD_images.py
```

### Для запуска Telegram бота:

- Запустить скрипт указав желаемый интервал в секундах публикации фотографий.

```
python sending_photos_bot_telegram.py --sst время в секундах
```
- Если время не указано, то устанавливается время по умолчанию равное 4 часам.

```
python sending_photos_bot_telegram.py
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
