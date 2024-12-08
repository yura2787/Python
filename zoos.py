import discoun
from pywebio.input import input as pw_input, NUMBER
from pywebio.output import put_text
from discoun import discount_6_12, discount_13_17, discount_61_100, price

age = pw_input(label='Введіть свій вік', type=NUMBER)

if age < 6:
    price = price * 0
elif age >= 6 and age <= 12:
    price = price / 100 * discount_6_12 - price
elif age >= 13 and age <= 17:
    price = price / 100 * discount_13_17 - price
elif age >= 18 and age <= 60:
    price = price
elif age > 61:
    price = price / 100 * discount_61_100 - price

put_text(f'Вхід у зоопарк коштує {price} грн')
