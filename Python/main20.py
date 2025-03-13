import os

class BookDatabase:
    def __init__(self, filename):
        self.filename = filename

    def add_record(self, title, author, year):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f"{title};{author};{year}\n")

    def delete_record(self, criterion, value):
        records = self.read_records()
        filtered_records = [record for record in records if not self.matches_criterion(record, criterion, value)]
        self.write_records(filtered_records)

    def sort_records(self, sort_index):
        records = self.read_records()
        records.sort(key=lambda x: x[sort_index])  # Сортируем по индексу поля
        return records

    def write_sorted_records(self, sorted_records, output_filename):
        with open(output_filename, 'w', encoding='utf-8') as file:
            for record in sorted_records:
                file.write(f"{';'.join(record)}\n")

    def select_records(self, criterion, value, output_filename):
        records = self.read_records()
        filtered_records = [record for record in records if self.matches_criterion(record, criterion, value)]
        self.write_sorted_records(filtered_records, output_filename)

    def add_sorted_record(self, new_record, sort_index):
        records = self.read_records()
        records.append(new_record)
        records.sort(key=lambda x: x[sort_index])
        self.write_records(records)

    def merge_databases(self, other_file):
        records = self.read_records()
        other_records = BookDatabase(other_file).read_records()
        records.extend(other_records)
        records.sort(key=lambda x: x[0])  # предположим, что сортируем по названию
        self.write_records(records)

    def read_records(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r', encoding='utf-8') as file:
            return [line.strip().split(';') for line in file.readlines()]

    def write_records(self, records):
        with open(self.filename, 'w', encoding='utf-8') as file:
            for record in records:
                file.write(f"{';'.join(record)}\n")

    @staticmethod
    def matches_criterion(record, criterion, value):
        if criterion == 'title':
            return record[0] == value
        elif criterion == 'author':
            return record[1] == value
        elif criterion == 'year':
            return record[2] == value
        return False

# Пример использования
if __name__ == "__main__":
    db = BookDatabase('books.txt')

    # Добавляем записи
    db.add_record("Гарри Поттер и философский камень", "Дж.К. Роулинг", "1997")
    db.add_record("Война и мир", "Лев Толстой", "1869")
    
    # Удаляем запись
    db.delete_record('author', 'Дж.К. Роулинг')
    
    # Сортируем записи
    sorted_records = db.sort_records(sort_index=0)  # Сортировка по названию
    db.write_sorted_records(sorted_records, 'sorted_books.txt')

    # Выбираем записи по критериям
    db.select_records('year', '1869', 'tolstoy_books.txt')

    # Добавляем запись в отсортированную базу
    db.add_sorted_record(["1984", "Джордж Оруэлл", "1949"], sort_index=0)

    # Сливаем две базы данных
    db.merge_databases('more_books.txt')