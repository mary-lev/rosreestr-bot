import os
import re
import requests
import random, vk_api, vk
import pandas as pd
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

#from settings import TOKEN, GROUP_ID, KEY, SERVER
from data_handlers import regions
from utils import get_old_price
from keyboards import region_keyboard
from keyboards import new_keyboard
from keyboards import first_keyboard
from keyboards import local_keyboard

TOKEN = os.environ.get("TOKEN")
GROUP_ID = os.environ.get("GROUP_ID")
KEY = os.environ.get("KEY")
SERVER = os.environ.get("SERVER")

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()
last_users_region = dict()
user_lands = dict()


def select_region(event):
    for region in regions:
        if region.name in str(event).lower():
            return region


def send_message(event, keyboard, answer):
    vk.messages.send(
        keyboard = keyboard.get_keyboard(),
        key = (KEY),
        server = (SERVER),
        ts=('6'),
        random_id = get_random_id(),
        message=answer,
        chat_id = event.chat_id,
        peer_id = event.message.peer_id,
        user_id=event.message.from_id,
    )

def clean_number(text):
    regex = r"60[:]\d\d[:]\d*[:]\d*"
    text = text.replace(" ", "")
    matches = re.search(regex, text, re.MULTILINE)
    if matches:
        return matches.group()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        message = {"date": event.message.date, "user_id": event.message.from_id, "text": event.message.text}
        print(f"Message {message}")
        if "Выбрать" in event.message.text:
            send_message(event, region_keyboard, answer="Выберите район Псковской области")
        if any(region.name in event.message.text.lower() for region in regions):
            region = select_region(event.message.text)
            last_users_region[str(event.message.from_id)] = region
            print(f"User region: {last_users_region}")
            answer=f'Загружаем данные по {region.case}. Какой кадастровый номер проверить?'
            send_message(event, new_keyboard, answer)

        elif 'Привет' in str(event) or 'привет' in str(event):
            print(event.message)
            answer = "Привет!"
            send_message(event, first_keyboard, answer)
            
        elif "60" in str(event):
            user = str(event.message.from_id)
            if user not in last_users_region:
                answer = 'Пожалуйста, выберите район'
                send_message(event, region_keyboard, answer)
            else:
                with open(region.filename, "r") as f:
                    df = pd.read_csv(f)
                #df = last_user_region[user].df
                number = clean_number(event.message.text)
                #old_price = get_old_price(number)
                #print(old_price)
                price = df[df["КН"]==number]
                if price.empty:
                    answer = f"""
                    Мы не нашли в {region.local_case} участка с таким кадастровым номером. Введите верный номер или выберите другой район.
                    Кадастровый номер состоит из цифр и двоеточий (без пробелов), например: 60:27:0050212:228
                    """
                    send_message(event, local_keyboard, answer)
                else:
                    if user in user_lands:
                        user_lands[user].append(number)
                    else:
                        user_lands[user] = [number]
                    print("User lands: ", user_lands)
                    answer = f"""
                        Участок {number}
                        Новая кадастровая стоимость участка: {price['КС'].values[0]} рублей.
                        Адрес: {price['Адрес'].values[0]}.
                        Площадь участка: {price['Площадь'].values[0]}.
                        
                        Будущая сумма земельного налога (при ставке 0.3% от кадастровой стоимости) с 2022 года: {round(price['КС'].values[0] * 0.01 * 0.3, 2)} рублей.

                        Если хотите проверить другой участок, укажите его кадастровый номер или выберите другой район.
                        """

                        # Старая кадастровая стоимость участка: {old_price}. <br>
                        # Категория земель: {price['Категория'].values[0]}.
                        # Разрешенное использование: {price['РИ клс'].values[0]}. {price[' РИ док'].values[0]}
                        # УПКС (удельный показатель кадастровой стоимости): {price['УПКС'].values[0]}.

                    send_message(event, new_keyboard, answer)


                    