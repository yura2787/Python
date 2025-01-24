from typing import Callable


def master(func: Callable) -> Callable:
    def subordinate(*args, **kwargs):
        result = func(*args, **kwargs)  # must be here!!!!!!!!!!!!!!!

        # -----------------------------------------
        # after execution
        if type(result) == int:
            number_to_increase = 10
            return result + number_to_increase

        return result

    return subordinate  # no round brackets !!!!!!!!!!!!!!


@master
def foo(num: int) -> int:
    return num


res = foo(10)
print(res)
