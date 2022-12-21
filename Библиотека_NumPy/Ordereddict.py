from collections import OrderedDict

data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
ordered_client_ages = OrderedDict(data)
print(ordered_client_ages)
print()

ordered_client_ages['Ilia'] = 23
print(ordered_client_ages)
print()

ordered_client_ages = OrderedDict(sorted(data, key=lambda x: x[1], reverse=True))
ordered_client_ages['Sonya'] = 24
del ordered_client_ages['Sonya']
print(ordered_client_ages)
print()