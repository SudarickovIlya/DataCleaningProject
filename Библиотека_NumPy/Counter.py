from collections import Counter


cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
c=Counter()
for car in cars:
    c[car]+=10
print(c)
print()
cars_moscow = ['black', 'black', 'white', 'black', 'black', 'white', 'yellow', 'yellow', 'yellow']
cars_spb = ['red', 'black', 'black', 'white', 'white', 'yellow', 'yellow', 'red', 'white']

counter_moscow = Counter(cars_moscow)
counter_spb = Counter(cars_spb)
print(counter_moscow)
print(counter_spb)
print()

print(counter_moscow + counter_spb)
print()

counter_moscow.subtract(counter_spb)
print(counter_moscow)
print()

print(*counter_moscow.elements())
print()

print(dict(counter_moscow))
print()

print(counter_moscow.most_common())

