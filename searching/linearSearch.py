def linearSearch(lst, elem, visual=False):
    """
    :param lst:    List, string, or other sequential list 
                   with __getitem__ and __len__
    :param elem:   Element to search for
    :param visual: Set to true to output visual
    :return:       Index of the element in the list, -1 if not in list
    """
    for i in range(len(lst)):
        if visual: 
            print(lst[i], end="")

        if lst[i] == elem:
            if visual:
                print("\nFound at index", i)
            return i
        elif visual and i != len(lst) - 1:
            print(", ", end="")
    return -1