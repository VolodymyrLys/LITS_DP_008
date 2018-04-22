import time
def good_mor():
    """Чи будемо снідати"""
    print('='*80)
    print('Задзовнив будильник, ви прокинулись, будете снідати?\n1 - Так\n2 - Ні')
    while True:
        choose = input()
        if choose == '1':
            #print('1')
            eating()
            return
        elif choose == '2':
            print('Будете голодні, тіпа дієта')
            return
        else:
           print('Зробіть вибір, натиснувши 1 або 2')
    

def eating():
    """Вибір їжі"""
    print('='*80)
    print('Виберіть сніданок:\n1 - кава\n2 - чай\n3 - щось серйозніше')
    while True:
        choose = input()
        if choose =='1':
            print('Ви випили каву')
            return
        elif choose =='2':
            print('Ви випили чай')
            return
        elif choose =='3':
            frig()
            return
        else:
            print('Зробіть вибір, натиснувши 1, 2 або 3')



def frig():
    """Вибір їжі з холодильника"""
    print('='*80)
    print('Відкрили холодильник, а там піца та солянка\n1 - піца\n2 - солянка')
    while True:
        choose=input()
        if choose=='1':
            print('Не найркащий вибір на ранок, але краще ніж порожній шлунок')
            return
        elif choose=='2':
            print('О солянка, з ранку робить диво, смачного')
            return
        else:
            print('Зробіть вибір, натиснувши 1 або 2')

def cln_teeth():
    """ Вибір чищення зубів"""
    print('='*80)
    print('Зуби чистити будемо?\n1 - Так\n2 - Ні')
    while True:
        choose = input()
        if choose == '1':
            print('Почистили зуби і на роботу')
            return
        elif choose == '2':
            print('Та ну його..., ще пасту тратити на такі дрібниці')
            return
        else:
           print('Зробіть вибір, натиснувши 1 або 2')
    
def car_or_bus():
    """Вибір автомобіля чи автобуса"""
    print('='*80)
    print("""На дворі сніг та мороз.
На роботу
1 - автомобілем
2 - скотовозкою""")
    while True:
        choose = input()
        if choose=='1':
            cln_car()
            return
        elif choose=='2':
            print('Бог в поміч..')
            return
        else:
            print('Зробіть вибір, натиснувши 1 або 2')
    

def cln_car():
    """Вибір очистки авто"""
    print('='*80)
    print('Треба чистити машину від снігу')
    print("""Будете чистити чи сама розмерзнеться в корку на світлофорі?
1 - Так
2 - Ні""")
    while True:
        choose = input()
        if choose=='1':
            print('Машина чиста і прогріта, поїхали!!!')
            return
        elif choose=='2':
            print('Розмерзнеться, не дизель ж..')
            return
        else:
            print('Зробіть вибір, натиснувши 1 або 2')

def auto_blyaha():
    """дії щодо відробляхи"""
    print('='*80)
    print('Якесь відро з гайками на БЛЯхах підрізає і димить дизелем перед вами')
    print("""Що будемо робити?
1 - Наказати дибіла
2 - Чи його і так життя наказало?""")
    while True:
        choose=input()
        if choose=='1':
            punshing()
            return
        elif choose=='2':
            print('Тримаємо дистанцію \n подалі від "відра"\n')
            return
        else:
            print('Зробіть вибір, натиснувши 1 або 2')


def punshing():
    print('='*80)
    print("""Як будемо наказувати?
1 - Тупо попікаєм
2 - Обеженем і дамо по гальмах
3 - Їдемо спокійно далі""")
    while True:
       choose = input()
       if choose=='1':
           print('Бидло навіть не розуміє кому сигналять')
           return
       elif choose=='2':
           print('Чути як шини візжать, сигналить. Дивно, що тормоза є у відрі з гайками')
           return
       elif choose=='3':
           chg_road_line()
           return
       else:
           print('Зробіть вибір, натиснувши 1, 2 або 3')

def chg_road_line():
    """зміна смуги руху"""
    print('='*80)
    print("""Змінемо смугу руху від відра подалі?
1 - Так
2 - Ні""")
    while True:
        choose=input()
        if choose=='1':
            print('Обганяємо, дивимось іржаве відро та їдемо далі')
            return
        elif choose=='2':
            print('Тримаємо дистанцію "\n подалі від відра"\n')
            return
        else:
            print('Зробіть вибір, натиснувши 1 або 2')



def car_brk():
    """ у бляхи відлітає колесо"""
    print('='*80)
    print('Ви їдете і помічаєте, що у євроВІДРА на польських бляхах відривається колесо')
    time.sleep(0.5)
    print("""Ваша дія?
1 - Зняти цей ржач на телефон
2 - Зупинитись і допомогти
3 - Зупинитись і дати в морду уроду""")
    while True:
        choose=input()
        if choose=='1':
            print('Оце так ржач, буде що у youtube залити')
            return
        elif choose=='2':
            print('За кермом лице не зіпсуте інтелектом, без ушкоджень')
            print('')
            print('Що на нього дивитись? Треба на роботу спішити')
            return
        elif choose=='3':
            wht_do()
            return
        else:
            print('Зробіть вибір, натиснувши 1, 2 або 3')

def wht_do():
    """дії з бляхером"""
    print('='*80)
    print("""Ви підійшли до БЛЯхи з гайками, за кермом лице не зіпсуте інтелектом.
без ушкоджень""")
    time.sleep(0.5)
    print("""Заїхати бляхеру по пиці?
1 - Так
2 - Ні""")
    while True:
        choose=input()
        if choose=='1':
            print('Бац, але дибіл і так не зрозумів за що')
            return
        elif choose=='2':
            print('Йому і так в житті важко')
            return
        else:
            print('Зробіть вибір, натиснувши 1 або 2')

"""Main code"""
good_mor()
time.sleep(1)
cln_teeth()
time.sleep(1)
car_or_bus()
time.sleep(1)
print('Так добре, тепло їдеться...')
time.sleep(3)
auto_blyaha()
time.sleep(1)
car_brk()
print('Ви приїхали на роботу')