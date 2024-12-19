import utils_lesson_13



def test_is_even_postive():
    number = 6
    expected_result = True
    actual_result = utils_lesson_13.is_even(number)
    assert actual_result == expected_result



def test_is_even_negative():
    number = 5
    expected_result = False
    actual_result = utils_lesson_13.is_even(number)
    assert actual_result == expected_result

# def test_get_list_of_string():
#     items = [22, 'apple']
#     expected_result = ['apple']
#     actual_resulr = utils_lesson_13.get_list(items)
#     assert actual_resulr



# def test_is_multiply_number():
#     number = 5
#     expected_result = 50
#     actual_result = utils_lesson_13.multiply_ten(number)
#     assert actual_result == expected_result
#
# def test_is_multiply_number_negative():
#     number = -2.5
#     expected_result = 25
#     actual_result = utils_lesson_13.multiply_ten(number)
#     assert actual_result == expected_result


def test_filter_strings_with_n():
        list_strings = ['apple', 'n', 'N']
        expected_result = ['n', 'N']
        actual_result = utils_lesson_13.filter_strings_with_n(list_strings)
        assert actual_result == expected_result

