
def chipher(text, step, direction):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    result = ''
    for i in range(len(text)):
        if direction == '1':
            if text[i] in eng_upper_alphabet:
                n = ord(text[i]) + step
                if n > 90:
                    n = 64 + (n - 90)
                result += chr(n)
            elif text[i] in eng_lower_alphabet:
                n = ord(text[i]) + step
                if n > 122:
                    n = 96 + (n - 122)
                result += chr(n)
            elif text[i] in rus_upper_alphabet:
                n = ord(text[i]) + step
                if n > 1071:
                    n = 1039 + (n - 1071)
                result += chr(n)
            elif text[i] in rus_lower_alphabet:
                n = ord(text[i]) + step
                if n > 1103:
                    n = 1071 + (n - 1103)
                result += chr(n)
            else:
                result += text[i]
        elif direction == '2':
            if text[i] in eng_upper_alphabet:
                n = ord(text[i]) - step
                if n < 65:
                    n = 90 - (64 - n)
                result += chr(n)
            elif text[i] in eng_lower_alphabet:
                n = ord(text[i]) - step
                if n < 97:
                    n = 122 - (96 - n)
                result += chr(n)
            elif text[i] in rus_upper_alphabet:
                n = ord(text[i]) - step
                if n < 1040:
                    n = 1071 - (1039 - n)
                result += chr(n)
            elif text[i] in rus_lower_alphabet:
                n = ord(text[i]) - step
                if n < 1072:
                    n = 1103 - (1071 - n)
                result += chr(n)
            else:
                result += text[i]
    return result

direction = input('Введите направление: \n(1 - шифрование, 2 - дешифрование: )\n')
step = int(input('Введите шаг сдвига: \n (от 1 до n) \n'))
language = input('Введите язык шифра: \n(1 - русский, 2 - английский) \n')
text = input('Введите текст для шифвровки или дешифровки: \n')

print(chipher(text, step, direction))

# перебор всех возможных комбинаций зашифрованных методом Цезаря
# out = []
# for i in range(2, 26):
#     out += f'{i}:' + chipher(text, i, direction) + '\n'
# print(*out, sep="")