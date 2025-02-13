try:
    n, k, m = map(int, input("Введите через пробел: ").split())
    #даёт условие 
    if m < 0 or m > 9:
        raise ValueError("m должна быть одной цифрой")
    
    result = n ** k
    #ищет число 
    result_str = str(result)
    
    if str(m) in result_str:
        print("Да, цифра", m, "присутствует в числе", result)
    else:
        print("Нет, цифра", m, "отсутствует в числе", result)
#ошибки
except ValueError as e:
    print("Ошибка ввода:", e)
