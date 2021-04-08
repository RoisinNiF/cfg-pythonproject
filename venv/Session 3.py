burger_price = input('What price is the burger? ')
within_budget = float(burger_price) <= 10.00
vegetarian= input('Does the restaurant have a veggie option? y/n ')
veggie_option = vegetarian == 'y'
suitable_restaurant = within_budget and vegetarian
if suitable_restaurant:
    print('This restaurant is a good choice')
if not suitable_restaurant:
    print('Probably not a good idea')


