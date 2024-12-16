import utils


def main():
    dealership1_cars_number = 10
    dealership2_cars_number = 30

    total_cars_in_dealership = dealership1_cars_number + dealership2_cars_number


    print(utils.has_premission_drive_car(1980))
    print(utils.has_premission_drive_car(1990))
    print(utils.has_premission_drive_car(2007))

    strings = utils.create_joined_string(data_list=[7654345, 'hjuujjj'], divider=', ')
    strings = utils.create_joined_string(divider='==', data_list=['list 2', 'hhhhhj', 234567, 7890])
    strings = utils.create_joined_string(data_list=['list 2', 'hhhhhj', 234567, 7890], divider='=+=')
    print(strings)


    total_cars = utils.get_cars_in_dealership(dealership1_cars_number, dealership2_cars_number)
    print(total_cars)


    cars_number_from_mobile = [111, 2523]
    total_cars_mobile = utils.get_cars_in_dealership(cars_number_from_mobile[0], cars_number_from_mobile[1])
    print(total_cars_mobile)

    print(1111, 22222, 3333333, sep='+++', end='0')
    print(444444, 55555555, 66666, sep='===')
    print(777777777, 55555555, 66666)

    print(utils.get_multiplied_string('a'))
    print(utils.get_multiplied_string('b'))
    print(utils.get_multiplied_string('c'))
    print(utils.get_multiplied_string('d'))

main()