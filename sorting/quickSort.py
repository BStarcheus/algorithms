def quickSort(lst, low, high, visual=False):
    """
    :param lst:    List with comparable items
    :param visual: Set to true to output visual
    :return:       The list sorted in ascending order
                   Note: The original list object passed as an argument is also
                   altered, so you don't have to use the return value
    """
    if high > low:
        pivot = _partition(lst, low, high, visual=visual)
        quickSort(lst, low, pivot - 1, visual=visual)
        quickSort(lst, pivot + 1, high, visual=visual)
    return lst


def _partition(lst, low, high, visual=False):
    """
    :param lst:    List with comparable items
    :param low:    Lower index of sublist
    :param high:   Upper index of sublist
    :param visual: Set to true to output visual
    :return:       Index of pivot value
    """
    left_position = low + 1
    right_position = high
    pivot = low
    pivot_val = lst[pivot] # Pick the first element as the pivot

    if visual:
        print("Low:", low, "High:", high, "Pivot Val:", pivot_val)
        print(lst)

    while left_position < right_position:

        # Find a value that is greater than pivot
        while left_position <= high and lst[left_position] < pivot_val:
            left_position += 1

        # Find a value that is less than pivot
        while right_position > low and lst[right_position] > pivot_val:
            right_position -= 1

        # Swap the two values
        if left_position < right_position:
            lst[left_position], lst[right_position] = lst[right_position], lst[left_position]

            if visual:
                print("Swap", lst[right_position], "and", lst[left_position])
                print(lst)

    if lst[right_position] <= pivot_val:
        # Place pivot in its correct position
        pivot = right_position
        lst[low] = lst[pivot]
        lst[pivot] = pivot_val

        if visual:
            print("Swap pivot and", lst[low])
    if visual:
        print(lst)

    return pivot