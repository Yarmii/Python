# Практическое занятие №6. «Разработка алгоритма для конкретной задачи»
# Вариант 19
# 1 Дано натуральное число
# k.
# Напечатать
# k-ю цифру последовательности
# 24681012141618202224262830..., содержащую подряд все натуральные четные
# числа.

try:
    k = int(input("vvod :"))

    if k<=0:
        raise ValueError("<0")
    
    sequence =""
    num = 2

    while len(sequence) <k:
        sequence += str(num)
        num =2

    result =sequence[k-1]
    print(f"{k}-я цфровая в последовательности : {result}")

except ValueError as e:
    print("ошбка")
except Exception as e:
    print("ошбка")