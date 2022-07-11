import sys

bitmap = '''
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................'''

print('Введите сообщение которое будет выведено в стили BitMap')
message = input('> ')
if message == '' or message == ' ':
    sys.exit()

# Проходим в цикле по всем строкам битовой карты

for line in bitmap.splitlines():
    # Проходим по всем символам строки
    for i, bit in enumerate(line):
        # Выводим пустое пространство согласно битовой карте
        if bit == ' ':
            print(' ', end='')
        else:
            print(message[i % len(message)], end='')
    print()