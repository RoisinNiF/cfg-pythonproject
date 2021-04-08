meal_price = float(input('How much did the meal cost? '))
discount_choice = input('Do you have a discount? y/n ')

discount_applicable = discount_choice == 'y'

discount_crit_passed= discount_applicable and meal_price >= 20

if discount_crit_passed:
    print('Discount applied')
    print('New price = {}'.format(meal_price*0.9))

else:
    print('No discount')