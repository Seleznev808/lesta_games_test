import timeit


def is_even(number: int) -> bool:
    return number & 1 == 0


def isEven(value: int) -> bool:
    return value % 2 == 0


if __name__=='__main__':
    assert is_even(2) == True
    assert is_even(1) == False
    assert is_even(0) == True
    assert is_even(-1) == False
    assert is_even(-2) == True

    value = 10 ** 1000 + 1
    number_of_measurements = 10 ** 6

    print(timeit.timeit(f'is_even({value})', number=number_of_measurements, setup='from __main__ import is_even'))
    print(timeit.timeit(f'isEven({value})', number=number_of_measurements, setup='from __main__ import isEven'))
