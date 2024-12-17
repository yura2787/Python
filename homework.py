import constans
from constans import list_repetition, PEN, BUDGET


def calculates_the_amount(prices: list[float]) -> float:
    total_price = 0
    for possion in prices:
        total_price = total_price + possion
    return total_price


def returning_element(items: list[str]) -> list[str]:
    repetition_list = []
    for item in items:
        if item not in repetition_list:
            repetition_list.append(item)
    return repetition_list


def checks_the_budget(budget: float, price: float) -> bool:
    has_permission = budget >= price
    return has_permission
