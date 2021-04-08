import random

first_names = ['Róisín', 'Ciara', 'Amy', 'Aoife']
last_names = ['Murphy', 'Finan', 'Monahan', 'Whelan']

chosen_name = random.choice(first_names) + ' ' + random.choice(last_names)
print(chosen_name)
