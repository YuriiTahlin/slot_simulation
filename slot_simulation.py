import numpy as np

# Три барабани (по 10 символів кожен)
reel1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
reel2 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
reel3 = [3, 1, 5, 2, 3, 2, 4, 1, 3, 2]

# Таблиця виплат
payouts = {
    (1, 1, 1): 50,
    (1, 1): 5,
    (2, 2, 2): 20,
    (2, 2): 3,
    (3, 3, 3): 5
}

# Параметри
spins = 500000
bet = 1

# Статистика
total_win = 0
win_count = 0
win_values = []

# Статистика виграшів за типами
win_types = {
    "(1, 1, 1)": 0,
    "(1, 1)": 0,
    "(2, 2, 2)": 0,
    "(2, 2)": 0,
    "(3, 3, 3)": 0
}

# Основний цикл
for i in range(spins):
    symbol1 = np.random.choice(reel1)
    symbol2 = np.random.choice(reel2)
    symbol3 = np.random.choice(reel3)

    # Перетворюємо в стандартні Python типи
    combination = (int(symbol1), int(symbol2), int(symbol3))  # Ось тут виправлено

    win = 0
    # Перевірка на точну трійку
    if combination in payouts:
        win = payouts[combination]
        win_types[str(combination)] += 1
    # Перевірка на перші 2 символи (парні виграші)
    elif combination[:2] in payouts:
        win = payouts[combination[:2]]
        win_types[str(combination[:2])] += 1

    if win > 0:
        win_count += 1
        total_win += win

    win_values.append(win)

# Підрахунок
rtp = total_win / (spins * bet)
hit_rate = win_count / spins
volatility = np.std(win_values)

# Результати
print(f"Кількість обертів: {spins}")
print(f"Загальний виграш: {total_win} грн")
print(f"RTP: {rtp:.4f}")
print(f"Частота виграшів: {hit_rate:.4f}")
print(f"Волатильність: {volatility:.2f}")

# Виведення статистики виграшів за типами
print("\nСтатистика виграшів за типами:")
for win_type, count in win_types.items():
    print(f"Комбінація {win_type}: {count} разів")
