while True:
    choose = input('Задзовнив будильник, ви прокинулись, будете снідати? Так(y), Ні(n)')
    if choose == 'y' or choose == 'Y':
        while True:
            choose = input('К(с)ава, ч(t)ай, щось с(о)ерйозніше:')
            if choose == 'c' or choose == 'C':
                print('Ви випили каву')
                break
            elif choose == 't' or choose == 'T':
                print('Ви випили чай')
                break
            elif choose == 'o' or choose == 'O':
                while True:
                    print('Відкрили холодильник, а там піца та солянка')
                    choose = input('Що будемо їсти: П(р)іца чи с(s)олянка:')
                    if choose == 'p' or choose == 'P':
                        print('Не найркащий вибір на ранок, але краще ніж порожній шлунок')
                        break
                    elif choose == 's' or choose == 'S':
                        print('О солянка, з ранку робить диво, смачного')
                        break
                    else:
                        print('Зробіть вибір, натиснувши р або s')
            else:
                print('Не правильний ввід, введіть c або t або o')
        break
    elif choose == 'n' or choose == 'N':
        print('Значить дієта, будемо голодні')
        break
    else:
        print('Не правильний ввід, введіть y або n')
#print ('Кінець великого вибору, частина 2.....')

while True:
    choose = input('Зуби чистемо? Так(y), Ні(n):')
    if choose == 'y' or choose == 'Y':
        print('Почистили зуби і на роботу')
        break
    elif choose == 'n' or choose == 'N':
        print('Та ну його..., ще пасту тратити на такі дрібниці')
        break
    else:
        print('Не правильний ввід, введіть y або n')
#print('кінець частини 2')
while True:
    choose = input('На дворі сніг та мороз. На роботу (а)втомобілем чи (с)котовозка?:')
    if choose =='a' or choose == 'A':
        print ('Треба чистити машину від снігу')
        while True:
            choose = input ('Будете чистити чи сама розмерзнеться в корку на світлофорі? Так(y), Ні(n):')
            if choose == 'y' or choose == 'Y':
                print ('Машина чиста і прогріта, поїхали!!!')
                break
            elif choose == 'n' or choose =='N':
                print ('Розмерзнеться, не дизель ж..')
                break
            else:
                print('Не правильний ввід, введіть y або n')
        input('Так добре, тепло їдеться, введіть що-небудь...')
        print('Якесь відро з гайками на БЛЯхах підрізає і димить дизелем перед вами')
        while True:
            choose = input('Що будемо робити? Наказати дибіла(y), чи його і так життя наказало (n)?')
            if choose == 'y' or choose == 'Y':
                print('Як будемо наказувати?')
                print('а) Тупо попікаєм')
                print('b) Обеженем і дамо по гальмах')
                print('c) Їдемо спокійно далі')
                while True:
                    choose = input()
                    if choose == 'a' or choose =='A':
                        print('Бидло навіть не розуміє кому сигналять')
                        break
                    elif choose == 'b' or choose == 'B':
                        print('Чути як шини візжать, сигналить. Дивно, що тормоза є у відрі з гайками')
                        break
                    elif choose =='c' or choose =='C':
                        while True:
                            choose = input('Змінемо смугу руху від відра подалі?  Так(y), Ні(n):')
                            if choose == 'y' or choose =='Y':
                                print('Обганяємо, дивимось іржаве відро та їдемо далі')
                                break
                            elif choose == 'n' or choose =='N':
                                print('Тримаємо дистанцію "\n подалі від відра"\n')
                                break
                            else:
                                print('Не правильний ввід, введіть y або n')
                        break
                    else:
                        print('Не правильний ввід, введіть ')
                        print('а) Тупо попікаєм')
                        print('b) Обеженем і дамо по гальмах')
                        print('c) Їдемо спокійно далі')
                
                break

            elif choose =='n' or choose =='N':
                print('Тримаємо дистанцію "\n подалі від відра"\n')
                break
            else:
                print('Не правильний ввід, введіть y або n')
        break

    elif choose == 'c' or choose == 'C':
        print ('Бог в поміч..')

        break
    else:
        print('Не правильний ввід, введіть a або c')
#print('Кінець частини три')
print('='*len('Ви їдете і помічаєте, що у євроВІДРА на польських бляхах відривається колесо'))
print('Ви їдете і помічаєте, що у євроВІДРА на польських бляхах відривається колесо')
while True:
    print('Ваша дія?')
    print('а) Зняти цей ржач на телефон')
    print('b) Зупинитись і допомогти')
    print('c) Зупинитись і дати в морду уроду')
    choose = input()
    if choose == 'a' or choose == 'A':
        print('Оце так ржач, буде що у youtube залити')
        break
    elif choose=='b' or choose=='B':
        print('За кермом лице не зіпсуте інтелектом, без ушкоджень')
        print('')
        print('Що на нього дивитись? Треба на роботу спішити')
        break
    elif choose =='c' or choose=='C':
        print('Ви підійшли до БЛЯхи з гайками, за кермом лице не зіпсуте інтелектом, без ушкоджень')
        while True:
            choose=input('Заїхати бляхеру по пиці? Так(y), Ні(n):')
            if choose=='y' or choose=='Y':
                print('Бац, але дибіл і так не зрозумів за що')
                break
            elif choose=='n' or choose=='N':
                print('Йому і так в житті важко')
                break
            else:
                print('Не правильний ввід, введіть y або n')
        break
    else:
        print('Не правильний ввід, введіть ')
        print('Ваша дія?')
        print('а) Зняти цей ржач на телефон')
        print('b) Зупинитись і допомогти')
        print('c) Зупинитись і дати в морду уроду')

print('='*len('Ви приїхали на роботу'))
print('Ви приїхали на роботу')
