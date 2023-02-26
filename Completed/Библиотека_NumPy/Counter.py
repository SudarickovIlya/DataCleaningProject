from collections import Counter

print(1)
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

print(2)
print(counter_moscow + counter_spb)
print()

print(3)
counter_moscow.subtract(counter_spb)
print(counter_moscow)
print()

print(4)
print(*counter_moscow.elements())
print()

print(5)
print(dict(counter_moscow))
print()

print(6)
print(counter_moscow.most_common())

