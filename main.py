lenx = 10                   #Ширина
leny = 10                   #Висота
lensnake = 2                #Довжина змійки
snakex = [lenx//2]*lensnake #Масив який буде зберігати кординати по іксам сигментів змійки (деволтно змійка в середині)
snakey = [leny//2]*lensnake #Масив який буде зберігати кординати по ігрикм сигментів змійки (деволтно змійка в середині)


def preferens():            #Функція для налаштування параметпів
    global lenx,leny,lensnake,snakex,snakey #обявлення того що ці змінні в функції будуть змінюватись глобально
    print('Чи потрібно вам надати нові значення для гри? \nСтандартні значення x=',lenx,' y=',leny,'snake = ',lensnake,'\n(yes/no)\n') #інтерфейс який запитує про необхідність щось змінювати
    flag = input()          #локальна змінна яка зберігає відповідь
    while True:             #Цикл який не завершиться допоки не отримає значення
        if flag == 'yes':   #Перевірка відповіді(якщо відповідь так то:)
            lenx = int(input('x\n')) #запитання яку поставити ширину
            leny = int(input('y\n')) #запитання яку поставити висоту
            lensnake = int(input('snake\n')) #запитання яку поставити довжину змійки
            snakex = [lenx//2]*lensnake #перестворення кординат іксів
            snakey = [leny//2]*lensnake #перестворення кординат ігриків
            break           #Вихід з циклу
        elif flag == 'no':  #Перевірка відповіді(якщо відповідь ні то:)
            print('ok')     #Написати ок
            break           #Вихід з циклу
        else:               #Інакше(якщо відповідь незадовольняється)
            flag = input('Що?\n') #Перезапитати відповідь


preferens()                 #Виклик функції налаштування
