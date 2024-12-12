from pywebio.input import input as pw_input, NUMBER
from pywebio.output import put_text

price = 0

age = pw_input(label='Введіть свій вік', type=NUMBER)
if age < 6:
    price = 0
elif age >= 6 and age <= 12:
    price = 50
elif age >= 13 and age <= 17:
    price = 75
elif age >= 18 and age <= 60:
    price = 100
elif age > 61:
    price = 70

put_text(f'Вхід у зоопарк коштує {price} грн.')
