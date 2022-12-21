from collections import OrderedDict

print(1)
data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
ordered_client_ages = OrderedDict(data)
print(ordered_client_ages)
print()

print(2)
ordered_client_ages['Ilia'] = 23
print(ordered_client_ages)
print()

print(3)
ordered_client_ages = OrderedDict(sorted(data, key=lambda x: x[1], reverse=True))
ordered_client_ages['Sonya'] = 24
del ordered_client_ages['Sonya']
print(ordered_client_ages)
print()

print(4)
from collections import defaultdict
ratings = [('Old York', 3.3), ('New Age', 4.6), ('Old Gold', 3.3), ('General Foods', 4.8),
           ('Belissimo', 4.5), ('CakeAndCoffee', 4.2), ('CakeOClock', 4.2), ('CakeTime', 4.1),
           ('WokToWork', 4.9), ('WokAndRice', 4.9), ('Old Wine Cellar', 3.3), ('Nice Cakes', 3.9)]

cafe=defaultdict(float)
for name, score in ratings:
    cafe[name]=score
    
cafes = OrderedDict(sorted(ratings, key=lambda x: (-x[1], x[0])))
# Обратная сортировка по рейтингу, прямая по названию (алфавитная)
print(cafes)