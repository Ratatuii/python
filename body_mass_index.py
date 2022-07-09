"""Программа, которая вычисляет индекс массы тела в зависимости от роста, веса и возраста, а затем выдает результат в
соответствии с рекомендациями Всемирной Организации Здравоохранения. """

age = int(input('Введите возраст (Например 18): '))
height = float(input('Введите рост (Например 1.75): '))
weight = float(input('Введите вес (Например 76.5): '))

if 10 > age or age > 100 or height <= 0 or height > 3 or weight <= 0 or weight > 150:
    print("Ошибочные входные данные")
else:
    bmi = weight / height ** 2  
    bmi = round(bmi, 2)
    if age >= 45:
        if bmi < 22:
            description = "недостаточной массой тела."            
        elif 22 < bmi <= 26.99:
            description = "нормальной массой тела."            
        elif 27 < bmi <= 31.99:
            description = "избыточной массой тела."  
        else:          
            description = "ожирением."
    else:
        if bmi < 18.5:
            description = "недостаточной массой тела."            
        elif bmi < 25:
            description = "нормальной массой тела."            
        elif bmi < 30:
            description = "избыточной массой тела."  
        else:          
            description = "ожирением."
    print("bmi =", bmi, "Вы относитесь к группе людей с", description)
