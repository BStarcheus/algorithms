def mergeSort(lst, low, high, visual=False):
    """
    :param lst:    List with comparable items
    :param low:    Lower index of sublist
    :param high:   Upper index of sublist
    :param visual: Set to true to output visual
    :return:       The list sorted in ascending order
                   Note: The original list object passed as an argument is also
                   altered, so you don't have to use the return value
    """

    def merge(low, mid, high):
        """
        Helper function to sort the elements while merging sublists.
        :param low:    Lower index of sublist
        :param mid:    Midpoint index of sublist
        :param high:   Upper index of sublist
        """
        left_position = low
        right_position = mid + 1
        counter = low
        temp = list(lst)

        while left_position <= mid or right_position <= high:
            # Find the next smallest element
            
            # If left < right, or
            # all of right sublist is used, keep pulling from left
            if (right_position > high
                or (left_position <= mid 
                    and temp[left_position] <= temp[right_position]) ):
                lst[counter] = temp[left_position]
                left_position += 1
            # If right < left, or
            # all of left sublist is used, keep pulling from right
            else:
                lst[counter] = temp[right_position]
                right_position += 1
            
            counter += 1

    if visual:
        print(lst[low:high+1])

    if low < high:
        mid = (low + high) // 2

        if visual:
            print(lst[low:mid+1], lst[mid+1:high+1])

        mergeSort(lst, low, mid, visual=visual)
        mergeSort(lst, mid+1, high, visual=visual)
        merge(low, mid, high)

        if visual:
            print(lst[low:high+1])
    return lst



def mergeSortSimple(lst, visual=False):
    """
    Simpler Python implementation, but requires more lists in memory,
    the pop() method, and does not alter original list in memory.
    :param lst:    List with comparable items
    :param visual: Set to true to output visual
    :return:       List sorted in ascending order
                   Note: Unlike the previous implementation, this does
                   not alter the original list in memory
    """

    def merge(left, right):
        """
        :param left:  Left sublist
        :param right: Right sublist
        :return:      List sorted in ascending order
        """
        sorted = []
        while left and right:
            sorted.append((left if left[0] <= right[0] else right).pop(0))
        
        sorted = sorted + left + right
        if visual:
            print(sorted)
        return sorted

    if visual:
        print(lst)

    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    
    if visual:
        print(lst[:mid], lst[mid:])
    return merge(mergeSortSimple(lst[:mid], visual=visual), 
                 mergeSortSimple(lst[mid:], visual=visual))