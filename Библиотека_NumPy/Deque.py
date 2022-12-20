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




