import string

def convert_n_to_m(x, n, m):
    digits = string.digits+string.ascii_uppercase #0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(digits)
    if (not isinstance(x, (str, int))):#перевірка чи х є класом str або int, тобто на дріб
        return False
    if (m > 36):
        return False
    if (n < 1):
        return False
    try:
        num = int(str(x), n)  # пробуємо перевести x в 10 систему через інт, та проводимо провірку чи число х є в системі числення з основою n
    except ValueError:
        return False  # Повертаю помилку, що число х має більшу основу за n
    try:
        if (m == 1):  # Провіряю, якщо перевести треба в систему "1" і видаю результат, якщо можливо, ні фалс
            return '0' * num
        else:  # Якщо число переводиться, усі умови правильні, то починаю конвертацію
            result = ''  # Пустий рядок
            while (num != 0):           #
                #print('num = ', num)
                digit = num % m         #ділю десткове число на основу м, залишок, буде цифра в системі м
                #print('digit =', digit, 'equalent to ', digits[digit])
                result += digits[digit] #беру число по індеску та записую перше число у строку
                num = num // m          #цілочисельне ділення, для того,щоб почати і настпній ітерації циклу, шукати наступний розряд
            return result[::-1]         #реверсую результат

    except ValueError:
        return False
    else:
        return result

# print(convert_n_to_m([123], 4, 3))
# print(convert_n_to_m("0123", 5, 6))
# print(convert_n_to_m("123", 3, 5))
# print(convert_n_to_m(123, 4, 1))
# print(convert_n_to_m(-123.0, 11, 16))
print(convert_n_to_m("A1Z", 36, 16))
#print(convert_n_to_m(4, 10, 5))