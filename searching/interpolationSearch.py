def interpolationSearch(lst, elem, visual=False):
    """
    Similar to binary search, search for an element in a sorted list, 
    but assume that the values are generally linear. 
    Use the line formed by the bounds of a range to guess a new index.

    :param lst:    List, string, or other sorted sequential list 
                   with __getitem__, __len__, and numeric items
    :param elem:   Element to search for
    :param visual: Set to true to output visual
    :return:       Index of the element in the list, -1 if not in list
    """
    if not len(lst):
        return -1

    low = 0
    high = len(lst) - 1

    while low <= high:
        
        # The line between low and elem must have the same slope as
        # the line between low and high so:
        # (elem - lst[low]) / (i - low) = (lst[high] - lst[low]) / (high - low)
        # So the value of elem is most likely to be at:
        i = int(low + (elem - lst[low]) * (high - low) / (lst[high] - lst[low]))

        if i < low or i > high:
            return -1

        if visual:
            print(f"L[{i}] = {lst[i]}")

        if lst[i] == elem:
            if visual:
                print("Found at index", i)
            return i
        elif elem < lst[i]:
            high = i - 1
        else:
            low = i + 1
    return -1