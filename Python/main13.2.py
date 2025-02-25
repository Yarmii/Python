# 5 Дан файл Tovar, содержащий сведения об экспортируемых
# товарах
# с
# указанием
# наименований
# импортеров и объемов поставляемых партий в штуках.
# Составить список стран, в которые экспортируется заданный
# товар, и общий объем его экспорта.
# Открываем файл для чтения
with open('Tovar.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Запрашиваем у пользователя название товара
target_product = input("Введите название товара: ")

# Создаем словарь для хранения информации по странам
countries = {}

# Обрабатываем каждую строку файла
for line in lines:
    # Разделяем строку на части
    product, country, quantity = line.strip().split(';')
    
    # Если строка относится к заданному товару
    if product == target_product:
        # Преобразуем количество в целое число
        quantity = int(quantity)
        
        # Если страна уже есть в словаре, добавляем количество
        if country in countries:
            countries[country] += quantity
        # Иначе создаем новую запись
        else:
            countries[country] = quantity

# Выводим результат
if countries:
    print(f"Страны, в которые экспортируется товар '{target_product}':")
    for country, total_quantity in countries.items():
        print(f"{country}: {total_quantity} штук")
    total_export = sum(countries.values())
    print(f"Общий объем экспорта: {total_export} штук")
else:
    print(f"Товар '{target_product}' не найден в файле.")