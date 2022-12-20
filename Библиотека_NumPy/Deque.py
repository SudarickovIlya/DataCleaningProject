from collections import deque

dq = deque()
print(dq)
print()

clients = deque()
clients.append('Ivanov')
clients.append('Petrov')
clients.append('Smirnov')
clients.append('Tikhonova')
print(clients)
print()

print(clients[2])
print()

first_client = clients.popleft()
second_client = clients.popleft()
print('First client:', first_client)
print('Second client:', second_client)
print('Other clients:', clients)
print()

clients.appendleft('VIP')
print(clients)
print()

tired_client = clients.pop()
print(tired_client, 'left the queu')
print(clients)
print()

del clients[0]
print(clients)
print()

shop = deque([1, 2, 3, 4, 5])
print(shop)
print()

shop.extend([11, 12, 13, 14, 15, 16, 17])
shop.extendleft([11, 12, 13, 14, 15, 16, 17])
print(shop)
print()

limited = deque([4, 6, 7, 12, 15, 26, 31], maxlen=4)
limited.extend([56, 69])
print(limited.append(125))
print(limited)
print()

temps = [20.6, 19.4, 19.0, 19.0, 22.1,
        22.5, 22.8, 24.1, 25.6, 27.0,
        27.0, 25.6, 26.8, 27.3, 22.5,
        25.4, 24.4, 23.7, 23.6, 22.6,
        20.4, 17.9, 17.3, 17.3, 18.1,
        20.1, 22.2, 19.8, 21.3, 21.3,
        21.9]
days = deque(maxlen=7)

for temp in temps:
    # Добавляем температуру в очередь
    days.append(temp)
    # Если длина очереди оказалась равной максимальной длине очереди (7),
    # печатаем среднюю температуру за последние 7 дней
    if len(days) == days.maxlen:
        print(round(sum(days) / len(days), 2), end='; ')
# Напечатаем пустую строку, чтобы завершить действие параметра
# end. Иначе следующая строка окажется напечатанной на предыдущей
print()
print()

dq = deque([1,2,3,4,5])
dq.reverse()
print(dq)

dq = deque([1,2,3,4,5])
dq.rotate(2)
print(dq)
dq.rotate(-3)
print(dq)
print()

dq = [1,2,4,2,3,1,5,4,4,4,4,4,3]
print(dq.index(5))


