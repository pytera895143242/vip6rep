from aiogram import types
from misc import dp, bot
from .sqlit import proverka_channel,cheak_traf,reg_user,reg_pod,reg_traf_support,cheack_keyboard_postinga,cheack_status_postinga,cheack_mes_id_postinga
from .sqlit import cheak_chat_id
import asyncio
import random

reg_user(1,1)

list_channel = cheak_traf()

name_channel_1 = list_channel[0][0][1:]
link_channel_1 = list_channel[0][1]

name_channel_2 = list_channel[1][0][1:]
link_channel_2 = list_channel[1][1]

name_channel_3 = list_channel[2][0][1:]
link_channel_3 = list_channel[2][1]

channel_posts = -1001525589284

list_channel = cheak_traf()
name_channel_1 = list_channel[0]
name_channel_2 = list_channel[1]
name_channel_3 = list_channel[2]
# name_channel_4 = list_channel[3]

def obnovlenie():
    global name_channel_1,name_channel_2,name_channel_3,name_channel_4
    list_channel = cheak_traf()
    name_channel_1 = list_channel[0]
    name_channel_2 = list_channel[1]
    name_channel_3 = list_channel[2]

@dp.callback_query_handler(text_startswith='start_watch')  # Нажал кнопку Начать смотреть
async def start_watch(call: types.callback_query):
    name_channel = call.data[12:]

    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='🥤Я ПОДПИСАЛСЯ🥤', callback_data=f'check{name_channel}')
    markup.add(bat_a)

    await bot.send_message(call.message.chat.id, '❌ ДОСТУП ЗАКРЫТ ❌\n\n '
                                                 '👉Для доступа к приватному каналу нужно быть подписчиком <b>Кино-каналов.</b>\n\n'
                                                 'Подпишись на <b>каналы</b> ниже 👇 и нажми кнопку <b>Я ПОДПИСАЛСЯ</b> для проверки!\n\n'
                                                 f'<b>Канал 1</b> - {name_channel_1[8:]}\n'
                                                 f'<b>Канал 2</b> - {name_channel_2[8:]}\n'
                                                 f'<b>Канал 3</b> - {name_channel_3[8:]}', parse_mode='html', reply_markup=markup, disable_web_page_preview=True)
    await bot.answer_callback_query(call.id)

@dp.callback_query_handler(text_startswith='check')  # Нажал кнопку Я ПОДПИСАЛСЯ. ДЕЛАЕМ ПРОВЕРКУ
async def check(call: types.callback_query):

    await bot.send_message(call.message.chat.id,"<tg-spoiler><b><a href = 'http://t.me/ChatAnonimkaBot?start=vip'>💋 Тебе отправило сообщение 2 пользователя, показать их?</a></b></tg-spoiler>",parse_mode='html')

    name_channel = call.data[5:]

    id_list = cheak_chat_id()
    try:
        proverka1 = (await bot.get_chat_member(chat_id=id_list[0], user_id=call.message.chat.id)).status
    except:
        proverka1 = 'member'
        reg_pod(id=call.message.chat.id, channel=name_channel_1)  # Регистрация статистики 1к

    try:  # Канал 2
        proverka2 = (await bot.get_chat_member(chat_id=id_list[1], user_id=call.message.chat.id)).status
        if proverka2 == 'member':
            reg_pod(id=call.message.chat.id, channel=name_channel_2)  # Регистрация статистики 2к
    except:
        proverka2 = 'member'
        reg_pod(id=call.message.chat.id, channel=name_channel_2)  # Регистрация статистики 2к

    try:  # Канал 3
        proverka3 = (await bot.get_chat_member(chat_id=id_list[0], user_id=call.message.chat.id)).status
        if proverka3 == 'member':
            reg_pod(id=call.message.chat.id, channel=name_channel_3)  # Регистрация статистики 3к
    except:
        proverka3 = 'member'
        reg_pod(id=call.message.chat.id, channel=name_channel_3)  # Регистрация статистики 3к

    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='🥤Я ПОДПИСАЛСЯ🥤', callback_data=f'check{name_channel}')
    markup.add(bat_a)

    if (
            proverka1 == 'member' and proverka2 == 'member' and proverka3 == 'member') or proverka1 == 'administrator' or proverka2 == 'administrator' or proverka3 == 'administrator' or proverka1 == 'creator' or proverka2 == 'creator' or proverka3 == 'creator':  # Человек прошел все 3 проверки
        if random.randint(1, 3) == 2:
            reg_traf_support(id=call.message.chat.id, channel=name_channel)
        if name_channel == '':
            ######  Человек перещел без реферальной ссылке    #####
            markup_2 = types.InlineKeyboardMarkup()
            bat_b = types.InlineKeyboardButton(text='🥤ПОДПИСАТЬСЯ🥤',
                                               url=f'{name_channel_1}')  # Cсылка на приват канал # ВАЖНО!!!!!
            markup_2.add(bat_b)
            await bot.send_message(call.message.chat.id, '✅ ДОСТУП ОТКРЫТ\n\n'
                                                         'Все новинки 2021 сливаем на наш приватный канал.<b> Подпишись</b> 👇',
                                   parse_mode='html', reply_markup=markup_2)

            ###########   Человек перешел по реферальной ссылке    ##########

        else:
            status = 1  ## Возвращает 1, если телеграмм канал проверен. 0 - Если нет

            if status == 0:
                markup_2 = types.InlineKeyboardMarkup()
                bat_b = types.InlineKeyboardButton(text='🥤ПОДПИСАТЬСЯ🥤',
                                                   url=f'{name_channel_1}')  # ВАЖНО!!!!!
                markup_2.add(bat_b)
                await bot.send_message(call.message.chat.id, '✅ ДОСТУП ОТКРЫТ\n\n'
                                                             'Все новинки 2021 сливаем на наш приватный канал.<b> Подпишись</b> 👇',
                                       parse_mode='html', reply_markup=markup_2)
            else:
                markup_2 = types.InlineKeyboardMarkup()
                bat_b = types.InlineKeyboardButton(text='🥤ПОДПИСАТЬСЯ🥤',
                                                   url=f'https://t.me/{name_channel}')  # Cсылка на приват канал
                markup_2.add(bat_b)
                await bot.send_message(call.message.chat.id, '✅ ДОСТУП ОТКРЫТ\n\n'
                                                             'Все новинки 2021 сливаем на наш приватный канал.<b> Подпишись</b> 👇',
                                       parse_mode='html', reply_markup=markup_2)


    else:
        await bot.send_message(call.message.chat.id, '❌Вы не подписались на каналы ниже\n\n'
                                                     'Проверьте еще раз подписку на всех каналах. И нажми кнопку <b>Я ПОДПИСАЛСЯ</b> для проверки!\n\n'
                                                     f'<b>Канал 1</b> - {name_channel_1[8:]}\n'
                                                     f'<b>Канал 2</b> - {name_channel_2[8:]}\n'
                                                     f'<b>Канал 3</b> - {name_channel_3[8:]}',
                               parse_mode='html', reply_markup=markup, disable_web_page_preview=True)
    await bot.answer_callback_query(call.id)