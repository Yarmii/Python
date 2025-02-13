
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

in_circle = (x**2 + y**2 <= 5**2)

in_square = (0 <= x <= 5) and (0 <= y <= 5)

result = in_circle or in_square

print(result)  