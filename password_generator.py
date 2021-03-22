from random import *

def generate_password(len_passwd, chars):
    
    return sample(chars, len_passwd)

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

quan_passwd = int(input('Введите количество генерируемых паролей: \n'))
len_passwd = int(input('Введите длинну желаемого пароля: \n'))

num_passwd = input('Включать ли цифры "0123456789"? (да/нет)').lower()
upp_str_passwd = input('Включать ли прописные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"? (да/нет)').lower()
low_str_passwd = input('Включать ли прописные буквы "abcdefghijklmnopqrstuvwxyz"? (да/нет)').lower()
char_passwd = input('Включать ли символы "!#$%&*+-=?@^_"? (да/нет)').lower()
except_passwd = input('исключать ли неоднозначные символы "il1Lo0O"? (да/нет)').lower()

if num_passwd == 'да':
    chars += digits
if upp_str_passwd == 'да':
    chars += uppercase_letters
if low_str_passwd == 'да':
    chars += lowercase_letters
if char_passwd == 'да':
    chars += punctuation 
if except_passwd == 'да':
    for i in chars:
        if i in 'il1Lo0O':
            chars = chars.replace(i, '')
for _ in range(quan_passwd):
    print(*generate_password(len_passwd, chars), sep='')
input('Нажмите Enter для завершения программы: ')