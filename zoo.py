import discount
from pywebio.input import input as pw_input, NUMBER
from pywebio.output import put_text
from discount import discount1, discount2, discount3

price = 100
age = pw_input(label='Введіть свій вік', type=NUMBER)

if age < 6:
    price = price * 0
elif age >= 6 and age <= 12:
    price = price / 100 * discount1 - price
elif age >= 13 and age <= 17:
    price = price / 100 * discount2 - price
elif age >= 18 and age <= 60:
    price = price
elif age > 61:
    price = price / 100 * discount3 - price

put_text(f'Вхід у зоопарк коштує {price} грн')
