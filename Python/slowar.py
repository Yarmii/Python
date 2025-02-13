# В Python словарь (dictionary) — это изменяемая коллекция, которая хранит данные в виде пар "ключ-значение". Ключи в словаре должны быть неизменяемыми типами данных (например, строки, числа, кортежи), а значения могут быть любыми типами данных, включая изменяемые (например, списки, другие словари и т.д.).

# Создание словаря
countries = {"Belarus": "Minsk", "Russia": "Moscow", "Germany": "Berlin"}

# Доступ к значению
print(countries["Belarus"])  # Minsk

# Добавление нового элемента
countries["France"] = "Paris"

# Изменение существующего элемента
countries["Belarus"] = "Brest"

# Удаление элемента
del countries["Russia"]

# Итерация по ключам и значениям
for key, value in countries.items():
    print(f"{key}: {value}")

# Очистка словаря
countries.clear()