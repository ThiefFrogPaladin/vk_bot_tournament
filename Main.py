import random
import csv
import datetime,schedule,threading,time

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# --
from commander.commander import Commander
from vk_bot import VkBot
# --


def write_msg(user_id, message):
    try:
        vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})
    except BaseException:
        vk.method('messages.send', {'user_id': user_id, 'message': 'ошибка', 'random_id': random.randint(0, 2048)})


# API-ключ созданный ранее
#token = "vk1.a.IRFlkf4jR6hCwUIN9WEGyDvsrILcWRGGkjdw54DIwnjQ4dT74hVzrW_KBgnkh9ch627e3XgKVcHOApGgFllKb-dGrzdFr0lifhlX4F9tJjzU8rhK5NL1kbc90-LLt1NWq8Q5dngCwjU-FSQRCNzJa8D8esWK9bswYPplnNtHfaM_iOhpVT84n-qf3JE65F4peRB4LLXRRAfpW_MihYFHXA"
token="vk1.a.AROswEGnXC7DdMkaPuZoQS32HAOF-ho6ooL3VuHo3zlN5F_06pcs7IgdtYwVSEK0QXUBLLBv8RHeARStPOGAvTTOSPXpxb4NQv-oFN6ih0QmEtOKG_prQTVpueMM4qB44IbGHDtQVmMrdSxLKVVaBlvDntv3m_Fb5JcfoOaIvUk37A_PDBV7ecML0OFDR52rlrbFsceRPeLhPLkPvKiYyw"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

commander = Commander()
print("Server started")

spis=1
def check_time():

    with open('participants.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for_correction = datetime.datetime.now().replace(microsecond=0)
        '''
        if for_correction.second < 10:
            for_correction = for_correction.replace(second=10)
        elif for_correction.second < 20:
            for_correction = for_correction.replace(second=20)
        elif for_correction.second < 30:
            for_correction = for_correction.replace(second=30)
        elif for_correction.second < 40:
            for_correction = for_correction.replace(second=40)
        elif for_correction.second < 50:
            for_correction = for_correction.replace(second=50)
        else:
            for_correction = for_correction.replace(second=0)
            for_correction += datetime.timedelta(minutes=1)
        
        if for_correction.second < 20:
            for_correction = for_correction.replace(second=0)
        elif for_correction.second < 40:
            for_correction = for_correction.replace(second=20)
        else:
            for_correction = for_correction.replace(second=40)
        '''
        number = (for_correction.second // 10) * 10
        for_correction = for_correction.replace(second=number)
        for_correction = str(for_correction)
        field = ['id', 'index_numb', 'starttime', 'round1end', 'rest1end', 'round2end', 'rest2end',
                 'round3end', 'rest3end', 'round4end', 'rest4end', 'round5end', 'rest5end', 'round6end', 'rest6end']
        numb = 13

        for row in reader:
            flag = False
            n = 2
            while n <= numb and not flag:

                if for_correction == row[field[n]]:
                    flag = True
                n += 1
            n -= 1
            if flag:
                print(f'New message from {field[0]}', end='')

                bot = VkBot(field[0])
                write_msg(int(row['id']), bot.new_message('РАУНД ' + str(n)+' '+str(row['index_numb'])))

def thr():
   while True:
      schedule.run_pending()


schedule.every(10).seconds.do(check_time)
threading.Thread(target=thr).start()

while True:
    #schedule.run_pending()
    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW:



            if event.to_me:
                '''if event.text=="автоотпр":
                    with open('participants.csv', newline='') as csvfile:
                        reader = csv.DictReader(csvfile)

                        for_correction=datetime.datetime.now().replace(microsecond=0)
                        if for_correction.second < 20:
                            for_correction = for_correction.replace(second=0)
                        elif for_correction.second < 40:
                            for_correction = for_correction.replace(second=20)
                        else:
                            for_correction = for_correction.replace(second=40)
                        for_correction=str(for_correction)
                        field=['id', 'index_numb', 'starttime', 'round1end', 'rest1end', 'round2end', 'rest2end',
                                  'round3end', 'rest3end', 'round4end', 'rest4end', 'round5end', 'rest5end', 'round6end','rest6end']
                        numb = 14

                        for row in reader:
                            flag=False
                            n=2
                            while n<=numb and not flag:
                                print(for_correction,row[field[n]])
                                if for_correction==row[field[n]]:
                                    flag=True
                                n+=1
                            n-=1
                            if flag:
                                print(f'New message from {field[0]}', end='')

                                bot = VkBot(field[0])
                                write_msg(int(row['id']), bot.new_message('РАУНД '+str(n)))
                    




                else:
                '''
                print(f'New message from {event.user_id}', end='')

                bot = VkBot(event.user_id)


                write_msg(event.user_id, bot.new_message(event.text))

                print('Text: ', event.text)
                print("-------------------")

