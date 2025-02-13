
number = float(input("Введите положительное вещественное число: "))


fractional_part = str(number).split('.')[1] 

result = '0' in fractional_part[:3]  


print(result)  