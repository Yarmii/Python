import math
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
numerator1 = 1 + math.sin(x + y)**2
denominator1 = 2 + x
term1 = numerator1 / denominator1
numerator2 = 2 * x
denominator2 = 1 + x**2 * y**2
if denominator2 == 0:
    result = "Определено не для значений, при которых 1 + x^2 * y^2 = 0"
else:
    term2 = numerator2 / denominator2
    result = term1 + term2

print(f"Результат f(x, y): {result}")