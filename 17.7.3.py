per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = float(input("Введите сумму, которую планируете положить под проценты: "))

deposit = []

for bank, percent in per_cent.items():
    deposit.append(int(money * percent / 100))

print("Накопленная сумма за год вклада в каждом из банков:", deposit)

max_deposit = max(deposit)

print("Максимальная сумма, которую вы можете заработать —", max_deposit)