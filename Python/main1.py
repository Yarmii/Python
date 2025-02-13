
x = float(input("Введите значение x: "))

form1 = abs(x**2 - x**3)

denominator = x**3 - 15 * x
if denominator == 0:
    result = "Определено не для x = 0 или x = 15"
else:
    fraction_part = 7 * x / denominator
    result = form1 - fraction_part

print(f"Результат f: {result}")