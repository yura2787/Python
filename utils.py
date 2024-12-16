import consatns


def get_cars_in_dealership(dealership1_cars: int, dealership2_cars: int) -> int:
    total_cars = dealership1_cars + dealership2_cars
    return total_cars



def create_joined_string(data_list: list, divider: str = ', ') -> str:
    result = divider.join(map(str, data_list))
    return result



def has_premission_drive_car(birth_year: int) -> bool:
    age = consatns.CURRENT_YEAR - birth_year
    has_premission = age >= consatns.MIN_DRIVE_AGE
    return has_premission



def get_multiplied_string(letter:  str, multiplicator: int = 5) -> str:
    result = letter * multiplicator
    return result


def get_list_with_numbers() -> list[int | float]:
    result = [111111, 23.65]
    return result





# def add_two_numbers(number_1, number_2):
#     result = number_1 + number_2
