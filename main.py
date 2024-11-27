import prices
import phrases
from prices import yogurt, pancakes, omelette, ice_cream, cake

print("Вітаємо вас в нашому закладі")
name = input('Як вас звати?').title()
print(phrases.phrases)

pancakes1 = input(f'{name} введіть кількість млинців >> ')
pancakes_quantity = int(pancakes1)
pancakes_price = prices.pancakes
total_pancakes = pancakes_quantity * pancakes_price

yogurt1 = input(f'{name} введіть кількість йогуртів >> ')
yogurt_quantity = int(yogurt1)
yogurt_price = prices.yogurt
total_yogurt = yogurt_quantity * yogurt_price

omelette1 = input(f'{name} введіть кількість омлетів >> ')
omelette_quantity = int(omelette1)
omelette_price = prices.omelette
total_omelette = omelette_quantity * omelette_price

ice_cream1 = input(f'{name} введіть кількість морозива >> ')
ice_cream_quantity = int(ice_cream1)
ice_cream_price = prices.ice_cream
total_ice_cream = ice_cream_quantity * ice_cream_price

cake1 = input(f'{name} введіть кількість тортів >> ')
cake_quantity = int(cake1)
cake_price = prices.cake
total_cake = cake_quantity * cake_price

total = total_pancakes + total_yogurt + total_omelette + total_ice_cream + total_cake
print(f"{name} сьогодні у нас в ресторані супер акція - всім клієнтам знижка 15%")
discount = total * 0.15
overall_result = total - discount

print('*' * 50)
print('RECEIPT')
print('*' * 50)
print(f"Млинці {pancakes_quantity} кількість порцій * ціна порції {pancakes} грн = {total_pancakes} ")
print(f"Йогурт {yogurt_quantity} кількість порцій * ціна порції {yogurt} грн = {total_yogurt} ")
print(f"Омлет {omelette_quantity} кількість порцій * ціна порції {omelette} грн = {total_omelette} ")
print(f"Морозиво {ice_cream_quantity} кількість порцій * ціна порції {ice_cream} грн = {total_ice_cream} ")
print(f"Торт {cake_quantity} кількість порцій * ціна порції {cake} грн = {total_cake} ")
print('*' * 50)
print(f'{name} Загальна сума для вашого замовлення = {overall_result}')
print('=' * 50)
