

# Надо доделать в полноценную программу.



# num = int(input('Введите число: \n'))
# num_sys = int(input('Введите на какую систему счисления хотите перевести число (2, 8):  \n'))
# result = []
# while num != 0:
#     result.append(num % num_sys)
#     num = num // num_sys

# print(*result[::-1], sep='')



num_sys_from = int(input('Из какой системы счисления вы хотите перевести число?: (2, 4, 8, 10, 16) \n'))
num_sys_in = int(input('В какую систему счисления вы хотите перевести число?: (2, 4, 8, 10, 16) \n'))
if num_sys_from == 16:
    num = input('Введите число: \n')
else:
    num = int(input('Введите число: \n'))
# num_sys = int(input('Введите на какую систему счисления хотите перевести число (2, 8, 10, 16):  \n'))

# Перевод из 10 в любую другую
def from_10(num, num_sys):
    result = []
    while num != 0:
        if num % num_sys > 9:
            result.append(chr((num % num_sys) + 55))
        else:
            result.append(num % num_sys)
        num = num // num_sys
    result = result[::-1]
    result = [str(i) for i in result]
    return ''.join(result)

# Перевод из двоичной системы в 
def from_2(num, num_sys):
    res = 0
    num = str(num)[::-1]
    for i in range(len(num)):
        res += int(num[i]) * num_sys ** i
    return res

# Перевод из 16 системы счисления
def from_16(num, num_sys):
    num = num[::-1]
    res = 0
    for i in range(len(num)):
        if num[i] in 'ABCDEF':
            res += (int(ord(num[i])) - 55) * num_sys ** i
        else:
            res += int(num[i]) * num_sys ** i
    return res


if num_sys_from == 10:
    print(from_10(num, num_sys_in))
elif num_sys_from == 2:
    print(from_2(num, num_sys_from))
elif num_sys_from == 16:
    print(from_16(num, num_sys_from))

# def nums():
#     a = ['1', '4', '7']
#     return (''.join(a))
# print(nums())

