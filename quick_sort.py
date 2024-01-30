def quick_sort(array: list[int | float], low: int, high: int) -> None:
    if low >= high:
        return
    left, right = low, high
    pivot = array[(low + high) // 2]
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left, right = left + 1, right - 1
    quick_sort(array, low, right)
    quick_sort(array, left, high)


if __name__=='__main__':
    test_list_1 = [2, 4, 1, 5]
    test_list_2 = [-10, -20, 0, 4]
    test_list_3 = [1, 2, 3, 4]
    test_list_4 = [1, 1, 1, 1]
    test_list_5 = []

    quick_sort(test_list_1, low=0, high=len(test_list_1) - 1)
    quick_sort(test_list_2, low=0, high=len(test_list_2) - 1)
    quick_sort(test_list_3, low=0, high=len(test_list_3) - 1)
    quick_sort(test_list_4, low=0, high=len(test_list_4) - 1)
    quick_sort(test_list_5, low=0, high=len(test_list_5) - 1)

    assert test_list_1 == [1, 2, 4, 5]
    assert test_list_2 == [-20, -10, 0, 4]
    assert test_list_3 == [1, 2, 3, 4]
    assert test_list_4 == [1, 1, 1, 1]
    assert test_list_5 == []
