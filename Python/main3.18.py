# Создаём списки для хранения баллов каждого участника
participants = ["Иванов", "Петров", "Сидоров"]
scores = []

for participant in participants:
    print(f"Введите баллы для {participant}:")
    m = int(input("Введите m: "))
    n = int(input("Введите n: "))
    p = int(input("Введите p: "))
    total = m + n + p
    scores.append(total)  

winner_score = max(scores)

print(f"Победитель набрал {winner_score} баллов.")