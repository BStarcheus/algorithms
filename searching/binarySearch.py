def binarySearchRecursive(lst, elem, low, high, visual=False):
    """
    :param lst:    List, string, or other sorted sequential list 
                   with __getitem__, __len__, and numeric items
    :param elem:   Element to search for
    :param low:    Lower index of search range
    :param high:   Upper index of search range
    :param visual: Set to true to output visual
    :return:       Index of the element in the list, -1 if not in list
    """
    if high < low or not len(lst):
        return -1
        
    mid = (low + high) // 2
    if visual:
        print(f"L[{mid}] = {lst[mid]}")

    if lst[mid] == elem:
        if visual:
            print("Found at index", mid)
        return mid
    elif elem < lst[mid]:
        return binarySearchRecursive(lst, elem, low, mid-1, visual=visual)
    else:
        return binarySearchRecursive(lst, elem, mid+1, high, visual=visual)

def binarySearchIterative(lst, elem, visual=False):
    """
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
        mid = (low + high) // 2
        if visual:
            print(f"L[{mid}] = {lst[mid]}")

        if lst[mid] == elem:
            if visual:
                print("Found at index", mid)
            return mid
        elif elem < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1