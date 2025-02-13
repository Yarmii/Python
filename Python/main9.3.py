#Практическое занятие №9. «Обработка одномерных массивов» Вариант 16 3
def find_pairs(arr, m):
    seen = set() ; pairs = []
    for num in arr: 
        target = m - num  
        if target in seen:  
            pairs.append((target, num))  
        seen.add(num)  
    return pairs
try:
    arr_input = input("Введите массив чисел через пробел: ")
    mas = arr_input.split()
    for i in mas:
        mas[mas.index(i)] = int(i)
    arr = list(mas)  
    m = int(input("Введите m: ")) 
except ValueError:
    print("Ошибка: введены некорректные данные. Убедитесь, что вы вводите числа.")
else:
    result = find_pairs(arr, m)
    if result:
        print(f"Найденные пары: {result}")
    else:
        print("Пары не найдены.")
