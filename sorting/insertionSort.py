def insertionSort(lst, visual=False):
    """
    :param lst:    List with comparable items
    :param visual: Set to true to output visual
    :return:       The list sorted in ascending order
                   Note: The original list object passed as an argument is also
                   altered, so you don't have to use the return value
    """
    if visual:
        print(lst)
    for i in range(1, len(lst)):
        insert_val = lst[i]
        position = i - 1

        while position >= 0 and insert_val < lst[position]:
            # Shift the items to the right
            lst[position + 1] = lst[position]
            position -= 1

            if visual:
                print(lst)
        lst[position + 1] =  insert_val

        if visual:
            print(lst)
    return lst