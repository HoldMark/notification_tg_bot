# Notification TG Bot

The project is a Telegram bot designed to send regular notifications throughout the day.
The bot operates by sending notifications at various intervals, creating an element of surprise and preventing user from becoming complacent.

### Features

- Notification Setting - Users can set notification for current day
- Notification Extension - Users have the option to extend notifications for a specified number of hours
- Notification Deletion - Users can delete notifications scheduled for the current day
- Notification Listing - The bot provides users with a list of all scheduled notifications.
- Notification Reset - Users can reset notifications for the current day

### Stack

- Python 3.10
- Aiogram - Asynchronous framework to create telegram bots
- APScheduler - Library that supports the scheduling of code to be executed later

### How To Start

1. Activate venv

2. Install requirements

```shell
pip install -r requirements.txt
```

3. Create .env file and fill it

4. Run

```shell
python main.py
```
