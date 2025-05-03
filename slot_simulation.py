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

# Основний цикл
for i in range(spins):
    symbol1 = np.random.choice(reel1)
    symbol2 = np.random.choice(reel2)
    symbol3 = np.random.choice(reel3)

    combination = (symbol1, symbol2, symbol3)

    win = 0
    # Перевірка на точну трійку
    if combination in payouts:
        win = payouts[combination]
    # Перевірка на перші 2 символи (парні виграші)
    elif combination[:2] in payouts:
        win = payouts[combination[:2]]

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
