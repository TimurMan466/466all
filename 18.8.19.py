num_tickets = int(input("Сколько билетов вы хотите купить? "))
total_cost = 0
underage_count = 0
for i in range(num_tickets):
    age = int(input("Введите возраст посетителя №{}: ".format(i+1)))
    if age < 18:
        underage_count += 1
    elif age < 25:
        total_cost += 990
    else:
        total_cost += 1390
if num_tickets > 3:
    total_cost *= 0.9
total_cost -= underage_count * 1390
if total_cost < 0:
    print(0)
else:
    print("Общая стоимость билетов: {} рублей".format(total_cost))