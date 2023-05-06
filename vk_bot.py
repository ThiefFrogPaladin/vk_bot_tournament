import bs4 as bs4
import requests
import datetime
import csv


class VkBot:

    def __init__(self, user_id):
        print("\nСоздан объект бота!")

        #self._starttime=datetime.datetime.now()
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        self._fieldnames = ['id', 'index_numb', 'starttime', 'round1end', 'rest1end', 'round2end', 'rest2end',
                              'round3end', 'rest3end', 'round4end', 'rest4end', 'round5end', 'rest5end', 'round6end','rest6end']
        self._enemy="ГОНКАПЕЧЕНЬЯ"
        self._solution=["молок",'','','','','']
        self._cur_part=0
        self._quest=['Где вы будете плыть быстрее — в воде или молоке?',
                     'Продолжите последовательность\n\n1, 9, 50, 11, 70',
                     'Найдите на сайте вк информацию для роботов. Имя класса:tr-popup__menu',
                     'Ты молодец. Уже работал с кодом и хорошо движешься по карьерной лесттнице. Но наша работа продолжается. Ты взломал переписку своего руководителя, и в ней он говорит ключевую информацию,но она, увы, зашифрована. Попробуй разгадать, что тут написано \n>=BA@9]~}|{zyxwvutsrqponmlkjihgfedcba`_^]\[ZYXWVUTSRQPONMLKJIeGcba`_^]\[ZSw:\n9OTMRQPONMFj-,+*)(DCBA:?>=<;4X876/.R2r*No-&J7',
                     'спектограмма',
                     'Вчера в команде разработки Саша Виженер отправил сообщение: \n"тз ноэадие,генё ухслтам срёлсдь ббя. пэйзясйхн зеюуна,ды хчььъп паэороь гымоуе,ктсфа эёшсэ эцэ"']
        self._rest=['На собеседованиях могут задавать головоломки в формате сообщения для человека, чтобы проверить кандидата на способность к абстрактному мышлению, логическому анализу и решению проблем. Такие задачи могут также показать, насколько кандидат способен организовывать свои мысли и выражать их ясно и лаконично. Кроме того, такие головоломки могут помочь оценить креативность и умение кандидата мыслить нестандартно и находить необычные решения. Эти навыки могут быть важными в работе, особенно в сферах, связанных с научными исследованиями, разработкой программного обеспечения и решением сложных задач.'+'https://vk.com/@psyfb2-naiti-umnogo-kak-proverit-logicheskoe-myshlenie-i-tvorcheski',
                    'Хорошо,ты изучил и подготовился к разным заданиям перед собеседованиям. Но ведь HR как это часто бывает,может отказать тебе. Мы предлагаем сейчас расслабиться почитать статью "Почему даже хорошие HR-ы никогда не объяснят вам причину отказа"\nhttps://vc.ru/flood/40466-pochemu-dazhe-horoshie-hr-y-nikogda-ne-obyasnyat-vam-prichinu-otkaza',
                    'Я думаю, тебе интересно узнать, насколько сложно вливаться в новый коллектив на работе. Честно говоря, это зависит от многих факторов, включая размер компании, культуру и отношения между коллегами.\n\nЕсли компания небольшая, то, скорее всего, тебе будет проще вливаться в коллектив. Обычно такие компании более дружелюбные, и коллеги легче находят общий язык. Если же компания крупная, то может понадобиться больше времени, чтобы наладить отношения со всеми коллегами.\n\nКультура компании также может повлиять на процесс вливания. Если компания очень формальная, то может быть сложнее найти общий язык с коллегами. В таком случае, стоит стараться проявлять инициативу и проявлять интерес к работе и коллегам.\n\nВ целом, вливаться в новый коллектив на работе может быть сложно, но это возможно. Главное – быть открытым, уважительным и проявлять инициативу.\nhttps://vk.com/@phosagro_career-kak-vlitsya-v-novyi-kollektiv',
                    'Если тебе нужно внедриться в коллектив и получить уважение своих коллег, то эффективные переговоры могут стать твоим лучшим помощником.\n\nВот несколько советов, которые помогут тебе добиться успеха в переговорах:\n\n1. Подготовься. Изучи тему переговоров, определи свои цели и рассмотрите возможные варианты развития событий.\n\n2. Слушай внимательно. Придай больше внимания тому, что говорят твои коллеги, и попробуй понять их точку зрения.\n\n3. Будь уверенным. Постарайся быть уверенным в себе и своих действиях. Это поможет тебе добиваться своих целей.\n\n4. Используй эмпатию. Попробуй поставить себя на место своих коллег и понять их чувства и мотивы.\n\n5. Будь готов к компромиссу. Иногда приходится идти на уступки, чтобы добиться общей цели.\nИ вот полезная статейка https://vk.com/@marketing_s-vedem-peregovory-pravilno',
                    'Кража данных может происходить из-за слабых паролей.В 21 веке информация — главная ценность, и ее надо уметь защищать.Правда компаниям такое нельзя использовать,в их структуре стоит многоуровневая защита данных.Но мы же не являемся компанией и нам самим бы не мешало защитить свои данные.\n\nКакие пароли ненадежные и как сделать их надёжными? Добавьте себе, чтобы не забыть: vk.cc/cn9PC1',
                    'Поздравляю с прохождением IT турнира! Вы проявили высокую компетенцию и профессионализм в сфере информационных технологий. Мы уверены, что такие успехи принесут вам новые возможности и достижения в карьере.\n\nХотим предложить вам несколько полезных материалов, которые помогут вам продолжить развиваться в IT-сфере:\n\n1. Книга "Clean Code" Роберта Мартина. Эта книга поможет вам стать лучшим программистом и научит вас писать чистый и понятный код.\n\n2. Курс "Алгоритмы и структуры данных" на платформе Coursera. Этот курс поможет вам улучшить свои навыки в разработке алгоритмов и структур данных.\n\n3. Сайт HackerRank. Этот сайт предлагает множество задач и вызовов для программистов, которые помогут вам улучшить свои навыки в различных областях программирования.\n\nНадеюсь, эти материалы будут полезны для вашего дальнейшего развития в IT-сфере. Желаем вам успехов и новых достижений!'
                    ]

        self._COMMANDS = ["ПРИВЕТ","НАЧАТЬ",'ПРАВИЛА','ПРИСТУПИТЬ',"РАУНД","РЕШЕНИЕ","ПРОТИВНИК","ВРЕМЯ", "ПОКА","ОТДЫХ"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")

        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

        return user_name.split()[0]

    def create_user(self):
        participant_exist=False
        num=0
        with open('participants.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                num+=1
                if self._USER_ID==int(row['id']):
                    participant_exist=True
        if not participant_exist:
            #self.increase_particip_numb()
            with open('participants.csv', 'a', newline='') as csvfile:
                fieldnames = self._fieldnames
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                nowi=datetime.datetime.now().replace(microsecond=0)
                if nowi.second<20:
                    nowi=nowi.replace(second=20)
                elif nowi.second<40:
                    nowi = nowi.replace(second=40)
                else:
                    nowi = nowi.replace(second=0)
                    nowi+=datetime.timedelta(minutes=1)
                spis=[]
                spis.append(nowi)
                delta=1
                for i in range(12):
                    nowi += datetime.timedelta(minutes=delta)
                    spis.append(nowi)
                writer.writerow({fieldnames[0]: self._USER_ID, fieldnames[1]:num+1, fieldnames[2]: spis[0], fieldnames[3]: spis[1], fieldnames[4]: spis[2], fieldnames[5]: spis[3], fieldnames[6]: spis[4], fieldnames[7]: spis[5], fieldnames[8]: spis[6], fieldnames[9]: spis[7],
                                 fieldnames[10]: spis[8], fieldnames[11]: spis[9], fieldnames[12]: spis[10], fieldnames[13]: spis[11],fieldnames[14]: spis[12]})
        return participant_exist



    def new_message(self, message):
        split_message=message.split()
        # Привет
        if message.upper() == self._COMMANDS[0]:
            return f"Привет-привет, {self._USERNAME}!"
        elif message.upper() == self._COMMANDS[1]:
            self._starttime = datetime.datetime.now().replace(microsecond=0)
            return "Привет, коллега, я буду твоим связным, мостиком для твоей работы, чтобы компания не рассекретила твою личность. Ты немного опоздал, так что пора приступать к делу.\nЕсли хочешь, чтобы я напомнил тебе правила нашей работы, то напиши ПРАВИЛА\nЕсли хочешь начать отсчёт, то напиши ПРИСТУПИТЬ"
        elif message.upper() == self._COMMANDS[2]:
            return "Ты хакер, который хочет пролезть глубоко в компанию, чтобы украсть её данные. Помимо тебя тем же самым занимается ещё множество нарушителей" \
                   "Ты должен решать задания компании, чтобы двигаться вглубь неё. Кроме этого тебе необходимо расшифровывать кодовые слова противников, чтобы осведомитель с ним разобрался\n\n" \
                   "Если ты не решаешь задание компании, то они теряют к тебе доверие, если твой противник расшифрует твоё сообщение, то компания тоже теряет к тебе доверие\n" \
                   "Если ты успеешь решить задание раньше, чем твой противник разгадает твою фразу, то твой цифровой след потеряется, и он не сможет тебе повредить.\n\nНа каждый раунд выделяется суммарно 10 минут, которые чередуются с 10 минутами отдыха\nВсего будет 6 раундов, как только ты попросишь задания, отсчёт пойдёт\n Дерзай!"
        elif message.upper() == self._COMMANDS[3]:
            flag=self.create_user()
            if flag:
                return 'Увы, порой невозможно начать всё сначала'
            else:
                return 'Начнётся же действо!'
        elif (split_message[0]).upper() == self._COMMANDS[4]:
            round=int(split_message[1])
            if round%2==0:
                return self._quest[round//2-1] + "\nНе забудь разобраться с конкурентом, он сделает всё, чтобы ты пролетел. Он оставил в сети кусок своих данных *ёсрнгтзъзряв*, декодируй его для меня\n" \
                                "напиши РЕШЕНИЕ *твой ответ без звёздочек* для ответа на задание.\nНапиши ПРОТИВНИК *расшифрованное сообщение противника без звёздочек*, чтобы я с ним разобрался"
            else:
                return self._rest[round//2-1]
            '''
            cur_part=0
            with open('participants.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                flag=True
                for row in reader:
                    if self._USER_ID == int(row['id']):
                        index=2
                        flag=True
                        nowi=str(datetime.datetime.now().replace(microsecond=0))
                        while index<14 and flag:
                            if nowi<row[self._fieldnames[index]]:
                                flag=False
                            index+=1
                        cur_part=index-2
            if cur_part%2==1 and not flag:
                return self._quest[cur_part]+"\nНе забудь разобраться с конкурентом, он сделает всё, чтобы ты пролетел. Он оставил в сети кусок своих данных *ёсрнгтзъзряв*, декодируй его для меня\n" \
                    "напиши РЕШЕНИЕ *твой ответ без звёздочек* для ответа на задание.\nНапиши ПРОТИВНИК *расшифрованное сообщение противника без звёздочек*, чтобы я с ним разобрался"
            else:
                return 'сейчас нет никаких заданий, отдыхай и учись хакерить)'
            '''
        elif (split_message[0]).upper() == self._COMMANDS[5]:
            with open('answers.csv', 'a', newline='') as csvfile:
                fieldnames = ['id','answer']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'id': self._USER_ID, 'answer': " ".join(split_message[1:])})
            return 'ты неплохо выдержал испытание, пока можешь заняться чем-то другим'
            '''
            if " ".join(split_message[1:]) == self._solution:
                return "HR в восторге! Ещё один тест, и ты на работе."
            else:
                return "Я думаю, HR не устроил твой ответ, они сомневаются в твоей надёжности..."
            '''
        elif (split_message[0]).upper() == self._COMMANDS[6]:
            with open('enemies.csv', 'a', newline='') as csvfile:
                fieldnames = ['id','answer']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'id': self._USER_ID, 'answer': " ".join(split_message[1:])})
            return 'О, с ними разберутся, пока можешь заняться чем-то другим'
            '''
            print(" ".join(split_message[1:]))
            if " ".join(split_message[1:]).upper()==self._enemy:
                return "У него будут большие неприятности, я обещаю."
            else:
                return "Я думаю, ты ошибся."
            '''
        elif message.upper() == self._COMMANDS[7]:
            nowi = ''
            flag=True
            nowi = datetime.datetime.now().replace(microsecond=0)
            used_nowi=str(nowi)
            zap=''
            with open('participants.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if self._USER_ID == int(row['id']):
                        index=2
                        flag=True

                        while index<14 and flag:
                            if used_nowi<row[self._fieldnames[index]]:
                                flag=False
                            index+=1
                        cur_part=index-2
                        zap=row[self._fieldnames[index-1]]
            if flag:
                return 'Всё кончилось, празднуй!'
            if not flag:
                remain_time = datetime.datetime.strptime(zap, "%Y-%m-%d %H:%M:%S") - nowi
                if cur_part%2==1:
                    return f"до конца раунда {cur_part//2+1} осталось {remain_time.seconds//60}:{str(remain_time.seconds % 60).zfill(2)}"
                else:
                    return f"до конца отдыха {cur_part//2} осталось {remain_time.seconds//60}:{str(remain_time.seconds % 60).zfill(2)}"


        else:
            return "Не понимаю о чем ты..."


    @staticmethod
    def _clean_all_tag_from_str(string_line):

        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """

        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result


