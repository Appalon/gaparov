from ast import Return
from crypt import methods
from http import server
import json
import os
from turtle import update
import telebot
from telebot import types
from flask import Flask, request
# from config import TOKEN
TOKEN = '5705923789:AAGEZ5_7Y9hVUrKpl9vWaofbTEq2s_2vwZo'
APP_URL = f'https://yaham.herokuapp.com/{TOKEN}'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)



@bot.message_handler(commands=['start'])
def start(message):
    

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    # item1 = types.KeyboardButton('Рандомные число')
    item2 = types.KeyboardButton('Группа❄️')
    item3 = types.KeyboardButton('Новости📌')
    item4 = types.KeyboardButton('Другое🔍')

    markup.add(item2,item3,item4)

    bot.send_message(message.chat.id, 'Здравствуйте, {0.first_name}!'.format(message.from_user), reply_markup = markup)
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Всё нормально!':
            bot.send_message(message.chat.id, '')

       
        elif message.text == 'Группа❄️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('CS👨‍💻👩')
            item2 = types.KeyboardButton('IC👨‍🎓')
            item3 = types.KeyboardButton('FM🕵️‍♂️')
            item4 = types.KeyboardButton('D👨‍🎨')
            # item5 = types.KeyboardButton('CS-5-22')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2,item3,item4, back)

            bot.send_message(message.chat.id,'Группы', reply_markup = markup)

        # elif message.text == 'Новости📌':
        #     markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        #     item1 = types.KeyboardButton('о боте')
        #     back = types.KeyboardButton('⬅️назад')
        #     markup.add(item1,item2, back)

        #     bot.send_message(message.chat.id,'информация', reply_markup = markup)

        elif message.text == '⬅️назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            # item1 = types.KeyboardButton('рандомные число')
            item2 = types.KeyboardButton('Группа❄️')
            item3 = types.KeyboardButton('Новости📌')
            item4 = types.KeyboardButton('Другое🔍')

            markup.add(item2,item3,item4)

            bot.send_message(message.chat.id, 'Выберите функцию', reply_markup = markup)

        elif message.text == 'CS👨‍💻👩':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('CS-1-22')
            item2 = types.KeyboardButton('CS-2-22')
            item3 = types.KeyboardButton('CS-3-22')
            item4 = types.KeyboardButton('CS-4-22')
            item5 = types.KeyboardButton('CS-5-22')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2,item3,item4,item5, back)

            bot.send_message(message.chat.id,'Группы', reply_markup = markup)


        # --------------------------------------------------------------------------------
        elif message.text == 'CS-1-22':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('💸Понедельник')
            item2 = types.KeyboardButton('💵Вторник')
            item3 = types.KeyboardButton('💴Среда')
            item4 = types.KeyboardButton('💶Четверг')
            item5 = types.KeyboardButton('💷Пятница')
            item6 = types.KeyboardButton('💰Суботта')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2,item3,item4,item5,item6, back)

            bot.send_message(message.chat.id,'Выберите день недели', reply_markup = markup)

        elif message.text == 'CS-2-22':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Понедельник')
            item2 = types.KeyboardButton('Вторник')
            item3 = types.KeyboardButton('Среда')
            item4 = types.KeyboardButton('Четверг')
            item5 = types.KeyboardButton('Пятница')
            item6 = types.KeyboardButton('🌚Суботта')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2,item3,item4,item5,item6, back)

            bot.send_message(message.chat.id,'Выберите день недели', reply_markup = markup)
        
        elif message.text == 'CS-3-22':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('📕Понедельник')
            item2 = types.KeyboardButton('📗Вторник')
            item3 = types.KeyboardButton('📘Среда')
            item4 = types.KeyboardButton('📙Четверг')
            item5 = types.KeyboardButton('📔Пятница')
            item6 = types.KeyboardButton('Суботта')
            item7 = types.KeyboardButton('🖇Список')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2,item3,item4,item5,item6,item7, back)

            bot.send_message(message.chat.id,'Выберите день недели', reply_markup = markup)

        elif message.text == 'CS-4-22':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('😡Понедельник')
            item2 = types.KeyboardButton('😤Вторник')
            item3 = types.KeyboardButton('🫠Среда')
            item4 = types.KeyboardButton('😉Четверг')
            item5 = types.KeyboardButton('🤪Пятница')
            item6 = types.KeyboardButton('🥳Суббота')
            item7 = types.KeyboardButton('📄Список')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2,item3,item4,item5,item6,item7, back)

            bot.send_message(message.chat.id,'Выберите день недели', reply_markup = markup)

        elif message.text == 'CS-5-22':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🐶Понедельник')
            item2 = types.KeyboardButton('🐱Вторник')
            item3 = types.KeyboardButton('🐼Среда')
            item4 = types.KeyboardButton('🐨Четверг')
            item5 = types.KeyboardButton('🐹Пятница')
            item6 = types.KeyboardButton('🦁Суботта')
            item7 = types.KeyboardButton('🔎Список')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2,item3,item4,item5,item6,item7, back)

            bot.send_message(message.chat.id,'Выберите день недели', reply_markup = markup)
# --------------------------расписания4-----------------------------------------------------------------

        elif message.text == '😡Понедельник':
            text =  '''
    8:00		----------
9:00		----------
10:00		----------
11:20	Кыргызский язык    116.k
12:20	Русский язык       
13:20	Русский язык       108А.k
14:20	----------	
15:20	----------	
            '''
            bot.send_message(message.chat.id, text)
        
        elif message.text == '😤Вторник':
            text = '''
8:00	----------	
9:00	Химия      106
10:00	Химия      106
11:20	Граждановедение   205
12:20	Французский язык / Корейский язык                                                                                                                                	
13:20	Французский язык / Корейский язык    
14:20	Математика      116
15:20	----------
            '''
            bot.send_message(message.chat.id, text)

        elif message.text == '🫠Среда':
            text = '''
    8:00	Физика    104 аудитория
    9:00	Физика    104 аудитория
    10:00	Начальная военная подготовка  113 аудитория
    11:20	География     116 аудитория
    12:20	Эдвайзерский час 107 аудитория
    13:20	Математика    116 аудитория
    14:20	----------
    15:20	----------	
                '''         
            bot.send_message(message.chat.id, text)
        elif message.text == '😉Четверг':
            text = '''
    8:00	----------	
    9:00	Истроия КР  108
    10:00	Начальная военная подготовка  108
    11:20	Французский язык / Корейский язык 
    12:20	Французский язык / Корейский язык                                                                                                                              	
    13:20	Кыргызская Литратура  114 
    14:20	Кыргызская Литратура  114 
    15:20	----------
                '''
            bot.send_message(message.chat.id, text)
        elif message.text == '🤪Пятница':
            text = '''
    8:00    Англиский язык
    9:00	Англиский язык
    10:00	Биология 115
    11:20	Математика   115
    12:20	Математика  115
    13:20	----------
    14:20	Физическая культура
    15:20	Физическая культура	
                ''' 
            bot.send_message(message.chat.id, text)

            
        elif message.text == '🥳Суббота':
            text = '''
    8:00    Кыргызский язык  116
    9:00	Физика    104
    10:00	Всеобщая история  201
    11:20	Основы критическое мышления 108
    12:20	Основы критическое мышления 108
    13:20	Математика   115
    14:20	----------
    15:20	----------	
                ''' 
            bot.send_message(message.chat.id, text)

        elif message.text == '📄Список':
             text = '''
    1. Абдыганыев Бекзат 
    2. Абдукаимов Аман 
    3. Абдусаттаров Маруфф 
    4. Асанбаев Самат 
    5. Базарбаев Назар 
    6. Беделбаев Умар 
    7. Бейшенбеков Марсель 
    8. Алекова Мээрим
    9. Нурманбекова Бегимай
    10. Гапаров Байел 
    11. Камилов Карыбек 
    12. Камчыбеков Эрбол  
    13. Аманатов Куткелди
    15. Маралбаева Уулжан
    16. Мырзакулов Даниел
    17. Нурканов Айтенир
    18. Раимбердиев Азатбек
    19. Райымбеков Кыдырсейит
    20. Сабыров Байсалбек 
    21. Узакбаев Даниель

            ''' 
             bot.send_message(message.chat.id, text)

# --------------------------cs3--------------------------------------
        elif message.text == '📕Понедельник':
            text =  '''
8:00 Физика 104k
9:00 Физика 104k
10:00 Химия 106k
11:20 Биология 115k
12:20 Математика 115k
13:20 Математика 115k
            '''
            bot.send_message(message.chat.id, text)


        elif message.text == '📗Вторник':
            text =  '''
8:00  ---------
9:00    Начальная военная подготовка 205k
10:00   Граждоноведение 108k
11:20   Всеобщая история 201k
12:20   Французский/Корейский язык 116/108A.k
13:20   Французский/Корейский язык 116/108А.k	
            '''
            bot.send_message(message.chat.id, text)

        elif message.text == '📘Среда':
            text =  '''
8:00----------
9:00----------
10:00 География 116k
11:20 Русский язык 113k
12:20 Русский язык 113k
13:20 История Кыргызстана 108k
14:20 Химия 106k
            '''
            bot.send_message(message.chat.id, text)

        elif message.text == '📙Четверг':
            text =  '''
8:00   ----------
9:00   Математика 114k
10:00  Физика 104k
11:20  Французский/Корейский язык 116/108А.k
12:20  Французский/Корейский язык 116/108А.k
13:20  ---------
14:20  Физическая культура 
15:20  Физическая культура	
            '''
            bot.send_message(message.chat.id, text)    

        elif message.text == '📔Пятница':
            text =  '''
8:00 Английский язык 
9:00 Английский язык 
10:00 Начальная военная подготовка 113k
11:20 Эдвайзерский час 107k
12:20 Кыргызский язык 114k
13:20 Кыргызский язык 114k
            '''
            bot.send_message(message.chat.id, text)  

        elif message.text == 'Суботта':
            text =  '''
8:00  ---------
9:00  Математика 202k
10:00  Математика 202k
11:20  Основы критического мышления 108А.k
12:20  Основы критического мышления 108А.k
13:20  Кыргызская литература 108k
14:20  Кыргызская литература 108k
            '''
            bot.send_message(message.chat.id, text)  


        elif message.text == '🖇Список':
             text = '''
    1. Абдиев Арсен 
    2. Алиев Эльдар 
    3. Аскарбекова Аяна 
    4. Борбоев Шамиль 
    5. Байитов Нуртилек 
    6. Багишпеков Тилек 
    7. Бейшеналиев Искендер 
    8. Гуламкадыров Байжигит
    9. Жаныбеков Эльдар 
    10. Жээнбаев Нурсултан 
    11. Исмаилов Омурбек 
    12. Каныбеков Айтегин
    13. Кожобеков Темирлан 
    14. Лим Тимур 
    15. Орозбаева Айдана 
    16. Сабитов Эрдияр 
    17. Сманова Элина 
    18. Талапова Фатима 
    19. Торогулова Назик 
    20. Турарбеков Айтбек

            ''' 
             bot.send_message(message.chat.id, text)
                
# ---------------------------cs1--------------------------------------
        elif message.text == '💸Понедельник':
                text =  '''
8:00---------------------
9:00 химия 106
10:00 физика 104
11:20 физика 104
12:20 кырг. яз 116
13:20 всеобщая история 116
14:20 введение в специальность 
14:20 -------------------
                '''
                bot.send_message(message.chat.id, text) 


        elif message.text == '💵Вторник':
                text =  '''
8:00 кыргызская литература 113
9:00 граждановеденье 113
10:00 биология 113
11:20 математика 113
12:20 математика 113
13:20---------------
14:20 физическая культура 
14:20 физическая культура    
                '''
                bot.send_message(message.chat.id, text) 


        elif message.text == '💴Среда':
                text =  '''
8:00 география 116
9:00 математика 115
10:00 эдвайзерский час 107
11:20 история Кыргызстана 108
12:20 Кыргызский язык 108
13:20 русский язык 113
14:20 -------------
                '''
                bot.send_message(message.chat.id, text) 


        elif message.text == '💶Четверг':
            text =  '''
8:00 Корейский/французский 108а/116
9:00 Корейский/французский 108а/116
10:00 химия 106
11:20 математика 115
12:20 математика 115
13:20 нвп 108
14:20 нвп 108
15:20----------------
            '''
            bot.send_message(message.chat.id, text) 


        elif message.text == '💷Пятница':
            text =  '''
8:00 Английский язык 
9:00 Английский язык 
10:00  Кыргызская литература 108k
11:20  Корейский/французский 108а/116
12:20  Корейский/французский 108а/116
13:20  Русский язык 114
14:20  -----------
            '''
            bot.send_message(message.chat.id, text)

        elif message.text == '💰Суботта':
            text =  '''
8:00  Физика   104k
9:00  Основы критического мышления 108А.k
10:00  Основы критического мышления 108А.k
11:20  -------------
12:20  -------------
13:20  -------------
14:20  -------------
            '''
            bot.send_message(message.chat.id, text)   


# ---------------------------cs5------------------------------------

        elif message.text == '🐶Понедельник':
            text =  '''

8:00 Русский язык 114
9:00 Русский язык 114
10:00 Всеобщая история 116
11:20 Математика 108А
12:20 Физика 104
13:20 Биология 113
14:20 Математика 116
            '''
            bot.send_message(message.chat.id, text)


        elif message.text == '🐱Вторник':
            text =  '''
8:00 Физика 104
9:00 Физика 104
10:00 Кыргызская литература 204
11:20 Кыргызская литература 204
12:20 Французский язык/Корейский                   116/108А
13:20 Французский язык/Корейский 116/108А
            '''
            bot.send_message(message.chat.id, text)


        elif message.text == '🐼Среда':
            text =  '''
8:00 ----------
9:00 Начальная военная подготовка 113
10:00 Граждановедение 114
11:20 Эдвайзерский час 107
12:20 География 116
13:20 Кыргызский язык 114
            '''
            bot.send_message(message.chat.id, text)


        elif message.text == '🐨Четверг':
            text =  '''
8:00 ---------
9:00 Начальная военная подготовка 113
10:00 История Кыргызстана 113
11:20 Французский язык/Корейский 116/108А
12:20 Французский язык/Корейский 116/108А
13:20 Химия 106
14:20 Химия 106
            '''
            bot.send_message(message.chat.id, text)


        elif message.text == '🐹Пятница':
            text =  '''
8:00 Английский язык 
9:00 Английский язык 
10:00 Математика 116
11:20 Кыргызский язык 114
12:20 -----------
13:20 -----------
14:20 Физическая культура
15:20 Физическая культура
            '''
            bot.send_message(message.chat.id, text)


        elif message.text == '🦁Суботта':
            text =  '''
8:00 ------
9:00 ------
10:00 -----
11:20 Математика 202
12:20 Математика 202
13:20 Основы критического мышления 108А
14:20 Основы критического мышления 108А
            '''
            bot.send_message(message.chat.id, text)

        elif message.text == '🔎Список':
             text = '''
   1)Батырканов Атайбек Нурланович
2)Болотканов Нурболот Нурзатович
3)Икрамов Белал Азаматович
4)Исраилов Орозобек Адилетович 
5) Калмырзаев Умар Бактиярович
6)Мамасалиев Динислам Күйшалалиевич 
7)Мамутова Дильназ Аблимитовна
8)Маратов Темирмырза Мелисович
9)Османкулов Актан Акылбекович
10)Туркменов Жамиль Азаматович
11)Умаров Нурмухаммед Султанмуратович 
12)Шайкеева Бегайым Сталбековна 
13) Эркин кызы Эркинай 
14)Нурдинов Байэл Бегалиевич 
15)Биниязова Жибек Марсовна
16)Барханский Роман Кириллович
17)Каримов Нурдөөлөт Бектурканович 
18)Абытжан улуу Максат
19)Мурзабаев Руслан Абдиманапович 
20)Эгембердиев Рустам Омкрбекович

            ''' 
             bot.send_message(message.chat.id, text)


# -------------------------cs2--------------------------------------

        elif message.text == 'Понедельник':
            text =  '''
8:00 ----------
9:00 кыргызский язык 108 каб
10:00 биология
11:20 химия 106
12:20 химия  106
13:20 кыргызский 114
14:20 физика 104
            '''
            bot.send_message(message.chat.id, text)


        elif message.text == 'Вторник':
            text =  '''
8:00 граждановедение
9:00 адабият
10:00 математика
11:20 начальная военная подготовка
12:20 Всеобщая история 
13:20 физика
14:20 физика
            '''
            bot.send_message(message.chat.id, text)

        elif message.text == 'Среда':
            text =  '''
8:00 ----------
9:00 география 
10:00 математика 
11:20 математика 
12:20 история кыргызыстана
13:20 ---------
14:20 ---------
            '''
            bot.send_message(message.chat.id, text)



        elif message.text == 'Четверг':
            text =  '''
8:00 французский/корейский
9:00 французский/корейский 
10:00 математика
11:20 начальная военная подготовка
12:20 адабият
13:20 математика
14:20 ---------
            '''
            bot.send_message(message.chat.id, text)


        elif message.text == 'Пятница':
            text =  '''
8:00 английский
9:00 английский
10:00 -----------
11:20 французский/ корейский 
12:20 французский/корейский 
13:20 русский
14:20 русский
            '''
            bot.send_message(message.chat.id, text)



        elif message.text == '🌚Суботта':
            text =  '''
8:00 эдвайзерсий час
9:00 критическое мышление
10:00 критическое мышление
            '''
            bot.send_message(message.chat.id, text)
# -------------------------------------------------------
# -----------------------------------------------------------------
# ----------------------------------------------------------------
# ---------------------------------------------------------------
# --------------------------------------------------------------
        elif message.text == 'IC👨‍🎓':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('IC-1')
            item2 = types.KeyboardButton('IC-2')
            item3 = types.KeyboardButton('IC-3')
            item4 = types.KeyboardButton('IC-4')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2,item3,item4,back)

            bot.send_message(message.chat.id,'Группы', reply_markup = markup)


        # --------------------------------------------------------------------------------
        elif message.text == 'IC-1':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🚗Понедельник')
            item2 = types.KeyboardButton('🚕Вторник')
            item3 = types.KeyboardButton('🚙Среда')
            item4 = types.KeyboardButton('🏎Четверг')
            item5 = types.KeyboardButton('🚓Пятница')
            item6 = types.KeyboardButton('🚑Суботта')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2,item3,item4,item5,item6, back)

            bot.send_message(message.chat.id,'Выберите день недели', reply_markup = markup)

        elif message.text == 'IC-2':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🏞Понедельник')
            item2 = types.KeyboardButton('🌅Вторник')
            item3 = types.KeyboardButton('🌄Среда')
            item4 = types.KeyboardButton('🌠Четверг')
            item5 = types.KeyboardButton('🌇Пятница')
            item6 = types.KeyboardButton('🏙Суботта')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2,item3,item4,item5,item6, back)

            bot.send_message(message.chat.id,'Выберите день недели', reply_markup = markup)
        
        elif message.text == 'IC-3':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🏬Понедельник')
            item2 = types.KeyboardButton('🏣Вторник')
            item3 = types.KeyboardButton('🏤Среда')
            item4 = types.KeyboardButton('🏥Четверг')
            item5 = types.KeyboardButton('🏦Пятница')
            item6 = types.KeyboardButton('🏨Суботта')
            # item7 = types.KeyboardButton('🖇Список')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2,item3,item4,item5,item6, back)

            bot.send_message(message.chat.id,'Выберите день недели', reply_markup = markup)

        elif message.text == 'IC-4':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🚔Понедельник')
            item2 = types.KeyboardButton('🚍Вторник')
            item3 = types.KeyboardButton('🚘Среда')
            item4 = types.KeyboardButton('🚖Четверг')
            item5 = types.KeyboardButton('🚛Пятница')
            item6 = types.KeyboardButton('🚜Суббота')
            # item7 = types.KeyboardButton('📄Список')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2,item3,item4,item5,item6, back)
            # --------------?

            bot.send_message(message.chat.id,'Выберите день недели', reply_markup = markup)

# --------------------------расписания4-----------------------------------------------------------------

        elif message.text == '🚔Понедельник':
            text =  '''
8:00 self-менеджмент 116
9:00 география 116
10:00 английский 204 
11:20 английский 204
12:20 нвп 204
13:20 ——
14:20 физра 
15:20 физра
            '''
            bot.send_message(message.chat.id, text)
        
        elif message.text == '🚍Вторник':
            text = '''
8:00 self-менеджмент 108а
9:00 корейский 108а
10:00 корейский 108а
11:20 корейский 108а
12:20 биология 114
13:20 математика 114
14:20 русский 113
            '''

            
            bot.send_message(message.chat.id, text)

        elif message.text == '🚘Среда':
            text = '''
8:00 искусство коммуникации 114
9:00 математика 204
10:00 математика 204
11:20 адабият 204
12:20 адабият 204
13:20 граждановедение 108а
                '''         
            bot.send_message(message.chat.id, text)
        elif message.text == '🚖Четверг':
            text = '''
8:00 нвп 108
9:00 физика 205
10:00 математика 205
11:20 математика 205
12:20 эдвайзерский час 
13:20 корейский 108а
14:20 корейский 108а
                '''
            bot.send_message(message.chat.id, text)
        elif message.text == '🚛Пятница':
            text = '''
8:00 физика 104
9:00 корейский 108а
10:00 химия 106
11:20 химия 106
12:20 русский  204
13:20 корейский 206
14:20 корейский 206
                ''' 
            bot.send_message(message.chat.id, text)

            
        elif message.text == '🚜Суббота':
            text = '''
8:00 ------------
9:00 кыргызский 113
10:00 кыргызский 113 
11:20 история Кр 115
12:20 всеобщая 115
13:20 физика 104
14:20 искусство коммуникации 104
                ''' 
            bot.send_message(message.chat.id, text)

       

# --------------------------cs3--------------------------------------
        elif message.text == '🏬Понедельник':
            text =  '''
8:00 английский 115
9:00 английский 115
10:00 начальная военная подготовка 202
11:20 начальная военная подготовка 202
12:20 биология 202
13:20 self-менеджмент 206
            '''
            bot.send_message(message.chat.id, text)


        elif message.text == '🏣Вторник':
            text =  '''
8:00 окошка
9:00 искусство коммуникации 202
10:00 английский 114
11:20 математика 114
12:20 математика 202
13:20 всеобщая история 202
14:20 self-менеджмент 202
            '''
            bot.send_message(message.chat.id, text)

        elif message.text == '🏤Среда':
            text =  '''
8:00 английский 201
9:00 английский 201
10:00 кыргызская литература 202
11:20 математика 
12:20 физика
            '''
            bot.send_message(message.chat.id, text)

        elif message.text == '🏥Четверг':
            text =  '''
8:00 английский 112
9:00 граждановедение 204
10:00 русский язык 204
11:20 русский язык 204
12:20 математика 206
13:20 математика 206	
            '''
            bot.send_message(message.chat.id, text)    

        elif message.text == '🏦Пятница':
            text =  '''
8:00 окошка
9:00 география 104
10:00 физика 104
11:20 физика 104
12:20 химия 106
13:20 химия 106
14:20 кыргызская литература 108
            '''
            bot.send_message(message.chat.id, text)  

        elif message.text == '🏨Суботта':
            text =  '''
8:00 окошка
9:00 искусство коммуникации 114
10:00 история кыргызстана 116
11:20 кыргызстана язык 113
12:20 кыргызстана язык 113
            '''
            bot.send_message(message.chat.id, text)  


# ---------------------------cs1--------------------------------------
        elif message.text == '🚗Понедельник':
                text =  '''
08:00 английский язык  113
09:00 английский язык  113
10:00 русский язык  108
11:20 искусство коммуникации  113
12:20 self-menedgment   113
13:20 химия   106
                '''
                bot.send_message(message.chat.id, text) 


        elif message.text == '🚕Вторник':
                text =  '''
08:00 математика  206
09:00 всеобщая история   206
10:00 математика  206
11:20 self-menedjment  115
12:20 адабият   204
13:20 окно 
14:20 физкультура 
15:20 физкультура
                '''
                bot.send_message(message.chat.id, text) 


        elif message.text == '🚙Среда':
                text =  '''
08:00 кыргызский язык   205
09:00 кыргызский язык   205
10:00 русский язык  205
11:20 химия   106
12:20 математика  202
13:20 математика  202
                '''
                bot.send_message(message.chat.id, text) 

        elif message.text == '🏎Четверг':
            text =  '''
08:00 английский  201
09:00 английский  201
10:00 граждоноведение   201
11:20 адабият   114
12:20 биология   113
            '''
            bot.send_message(message.chat.id, text) 


        elif message.text == '🚓Пятница':
            text =  '''
08:00 НВП   116
09:00 НВП   116
10:00 искусство коммуникации  108а
11:20 география   113
12:20 физика   104
13:20 физика    104
            '''
            bot.send_message(message.chat.id, text)

        elif message.text == '🚑Суботта':
            text =  '''
08:00 английский  201
09:00 английский  201
10:00 физика   104
11:20 математика  201
12:20 искусство КР   201
13:20 эдвайзерский час
14:20  -------------
            '''
            bot.send_message(message.chat.id, text)   



# -------------------------cs2--------------------------------------

        elif message.text == '🏞Понедельник':
                text =  '''
   8:00 Английский язык 201
9:00 Английский язык 201
10:00 Кыргызский язык 114
11:20 Русский язык 201
12:20 Всеобщая история 201
13:20 Физика 104
                '''
                bot.send_message(message.chat.id, text)


        elif message.text == '🌅Вторник':
            text =  '''
08:00 Английский язык 201
09:00 Биология 114
10:00 Искусство коммуникации 202
11:20 Искусство коммуникации 202
12:20 Self менеджмент 115
13:20 Self менеджмент 115
            '''
            bot.send_message(message.chat.id, text)

        elif message.text == '🌄Среда':
            text =  '''
08:00 Русский язык 115
09:00 Химия 106
10:00 Физика 104
11:20 Физика 104
12:20 Начальная военная подготовка 108А
13:20 -
14:20 Физическая культура спорт зал
15:20 Физическая культура спорт зал
            '''
            bot.send_message(message.chat.id, text)



        elif message.text == '🌠Четверг':
            text =  '''
08:00 Математика 115
09:00 Английский язык 202
10:00 Кыргызский язык 116
11:20 Химия 116
12:20 Граждановедение 108
Эдвайзерский час
            '''
            bot.send_message(message.chat.id, text)

            # tem3 = types.Keyboard


        elif message.text == '🌇Пятница':
            text =  '''
08:00 География 108А
09:00 Английский язык 205
10:00 Английский язык 205
11:20 Начальная военная подготовка 205
12:20 Математика 202
13:20 Математика 202
            '''
            bot.send_message(message.chat.id, text)



        elif message.text == '🏙Суботта':
            text =  '''
08:00 История Кыргызстана 113
09:00 Математика 108
10:00 Математика 108
11:20 Кыргызская литература 108
12:20 Кыргызская литература 108
            '''
            bot.send_message(message.chat.id, text)


        



# ------------------------d--------------------------------------

        elif message.text == 'D👨‍🎨':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('D-1')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,back)

            bot.send_message(message.chat.id,'Группы', reply_markup = markup)



# --------------------------------------------------------------------------------
        elif message.text == 'D-1':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🥇Понедельник')
            item2 = types.KeyboardButton('🥈Вторник')
            item3 = types.KeyboardButton('🥉Среда')
            item4 = types.KeyboardButton('🏅Четверг')
            item5 = types.KeyboardButton('🎖Пятница')
            item6 = types.KeyboardButton('🏆Суботта')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2,item3,item4,item5,item6, back)

            bot.send_message(message.chat.id,'Выберите день недели', reply_markup = markup)

        elif message.text == '🥇Понедельник':
                text =  '''
8:00-Биология 108А
9:00-Математика 108А
10:00-Математика 108А
11:20-Английский 108,112,114
12:20-Английский108,112,114
13:20--------
14:20-Физическая культура
15:20-Физическая культура
                '''
                bot.send_message(message.chat.id, text)


        elif message.text == '🥈Вторник':
            text =  '''
8:00-НВП 108
9:00-Математика 108
10:00-Всеобщая история 116
11:20-Химия 106
12:20-Химия 106
13:20-Граждановидение 108
            '''
            bot.send_message(message.chat.id, text)

        elif message.text == '🥉Среда':
            text =  '''
8:00-НВП 113
9:00-Русский язык108
10:00-Кыргызский язык 108А
11:20-Кыргызский язык 108А
12:20-Математика 115
13:20-География 115
            '''
            bot.send_message(message.chat.id, text)



        elif message.text == '🏅Четверг':
            text =  '''
8:00-Физика 104
9:00-Английский язык 112,104,115
10:00-Искусство коммуникации 114
11:20-История Кыргызстана 104
12:20-Эдвайзерский час 107
            '''
            bot.send_message(message.chat.id, text)

            # tem3 = types.Keyboard


        elif message.text == '🎖Пятница':
            text =  '''
8:00-Кыргызская  литература 108
9:00-Кыргызская литература 208
10:00-Цифровая эрудиция 107
11:20-Цифровая эрудиция 107
12:20-Русский язык 113
13:20-Математика 116
            '''
            bot.send_message(message.chat.id, text)



        elif message.text == '🏆Суботта':
            text =  '''
8:00-Введение в специальность 116
9:00-Введение в специальность 116
10:00-Искусство коммуникации 206
11:20-Физика 104
12:20-Физика 104
13:20-Основы критического мышления 108А
14:20-Основы критического мышления 108А
            '''
            bot.send_message(message.chat.id, text)

# --------------------------fm----------------------------------------
        elif message.text == 'FM🕵️‍♂️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('FM-1-22')
            item2 = types.KeyboardButton('FM-2-22')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2, back)

            bot.send_message(message.chat.id,'Группы', reply_markup = markup)

        # --------------------------------------------------------------------------------
        elif message.text == 'FM-1-22':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('♠️Понедельник')
            item2 = types.KeyboardButton('♣️Вторник')
            item3 = types.KeyboardButton('♥️Среда')
            item4 = types.KeyboardButton('♦️Четверг')
            item5 = types.KeyboardButton('🃏Пятница')
            item6 = types.KeyboardButton('🎴Суботта')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2,item3,item4,item5,item6, back)

            bot.send_message(message.chat.id,'Выберите день недели', reply_markup = markup)

        elif message.text == '♠️Понедельник':
                text =  '''
8:00 ----------------
9:00 Искусство коммуникации 205
10:00 Исскуство коммуникации 205
11:20 Иностранный язык 108,114,112
12:20 Иностранный язык 108,114,112
                '''
                bot.send_message(message.chat.id, text)


        elif message.text == '♣️Вторник':
            text =  '''
8:00 Биология 116
9:00 Self менеджмент 115
10:00 Self менеджмент 115
11:20 Физика 104
12:20 Граждановедение 108
13:20 География 113
            '''
            bot.send_message(message.chat.id, text)

        elif message.text == '♥️Среда':
            text =  '''
8:00 Математика 108
9:00 История Кыргызстана 114
10:00 Введение в специальность 201
11:20 Введение в специальность 201
12:20 Химия 106
13:20 Химия 106
            '''
            bot.send_message(message.chat.id, text)



        elif message.text == '♦️Четверг':
            text =  '''
8:00  ---------------
9:00 Разговорный иностранный язык 112,104,115
10:00 Русский язык 206
11:20 Русский язык 206
12:20 Физика 104
13:20 Физика 104 
14:20 Математика 115
            '''
            bot.send_message(message.chat.id, text)

            # tem3 = types.Keyboard


        elif message.text == '🃏Пятница':
            text =  '''
8:00 Математика 115
9:00 Математика 115
10:00 Кыргызский язык 108
11:20 Кыргызский язык 108
12:20 Начальная военная подготовка 108
13:20 Начальная военная подготовка 108A
            '''
            bot.send_message(message.chat.id, text)



        elif message.text == '🎴Суботта':
            text =  '''
8:00 Математика 206
9:00 Цифровая эрудиция 209
10:00 Цифровая эрудиция 209
11:20 Всеобщая история 116
12:20 Кыргызская литература 114
13:20 Кыргызская литература 114
            '''
            bot.send_message(message.chat.id, text)





        elif message.text == 'FM-2-22':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🔈Понедельник')
            item2 = types.KeyboardButton('🔇Вторник')
            item3 = types.KeyboardButton('🔉Среда')
            item4 = types.KeyboardButton('🔊Четверг')
            item5 = types.KeyboardButton('🔔Пятница')
            item6 = types.KeyboardButton('📣Суботта')
            back = types.KeyboardButton('⬅️назад')
            markup.add(item1,item2,item3,item4,item5,item6, back)

            bot.send_message(message.chat.id,'Выберите день недели', reply_markup = markup)

        elif message.text == '🔈Понедельник':
                text =  '''
9:00 Селф менеджмент 206
10:00 Селф менеджмент 206
11:20 иностранный язык 108,112,114
12:20 иностранный язык 108,112,114
13:20 нвп 108 
14:20 русский язык 115
                '''
                bot.send_message(message.chat.id, text)


        elif message.text == '🔇Вторник':
            text =  '''
8:00 искусство коммуникации 114
9:00 математика 116
10:00 физика 104
11:20 география 116
12:20 физика 104
13:20 химия 106
            '''
            bot.send_message(message.chat.id, text)

        elif message.text == '🔉Среда':
            text =  '''
9:00 искусство коммуникации 108а
10:00 история Кыргызстана 108
11:20 граждановедение 114
12:20 введение в специальность 201
13:20 введение в специальность 201
14:20 русский язык 116
            '''
            bot.send_message(message.chat.id, text)



        elif message.text == '🔊Четверг':
            text =  '''
9:00 разговорный ин.яз 112,104,115
10:00 биология 108а
11:20 физика 201
12:20 химия 106
14:20 физ-ра 
15:20 физ-ра
            '''
            bot.send_message(message.chat.id, text)

            # tem3 = types.Keyboard


        elif message.text == '🔔Пятница':
            text =  '''
8:00 цифровая эрудиция 107
9:00 цифровая эрудиция 107
10:00 математика 201
11:20 математика 201
12:20 кырг.яз 201
13:20 кырг.яз 201
14:20 нвп 115
            '''
            bot.send_message(message.chat.id, text)



        elif message.text == '📣Суботта':
            text =  '''
9:00 всеобщая история 206
10:00 адабият 114
11:20 адабият 114
12:20 математика 116
13:20 математика 116
            '''
            bot.send_message(message.chat.id, text)
# --------------------------------------------------------------------
        elif message.text == 'Другое🔍':
            text =  '''	
            Если у вас есть какие-нибудь пожелания пишите админу
            '''
        
            bot.send_message(message.chat.id, text)
            


        # elif message.text == 'Другое🔍':
        #     foto = open('mennn/aijana.jpg', 'rb')
        #     bot.send_photo(message.chat.id, foto)
        #     text = 'Гапаров Байэл'
        #     bot.send_message(message.chat.id, text)

# -----------------------------------------------------------------


        

        elif message.text == 'Новости📌':
            text =  '''	
            Пока что нету новостей)
            '''
            # foto = open('memy/rek.jpg', 'rb')
            # bot.send_photo(message.chat.id, foto)
            bot.send_message(message.chat.id, text)
    
bot.polling(none_stop = True)
@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return '!', 200
@server.route('/')
def webhook():
    bot.remote_webhook()
    bot.set_webhook(url=APP_URL)
    return '!', 200

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT',5000)))