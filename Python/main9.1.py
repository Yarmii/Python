#Практическое занятие №9. «Обработка одномерных массивов» Вариант 16 1 
numbers = []
count = int(input("Сколько должно выполнится :"))
for i in range(count):
    while True:
        try:
            number = int(input(f"Ввод {i+1}: "))
            numbers.append(number)
            break  # выход из цикла, если ввод корректен
        except ValueError:
            print("Ошибка! Введите целое число.")
result = sum(numbers)
print("Сумма:", result)








