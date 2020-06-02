from math import ceil, log2

def findTwoLargest(lst, visual=False):
    """
    Run a 'tournament', with the largest element winning. 
    Then find the second largest element by checking the loser list.
    :param lst:    List with comparable elements
    :param visual: Set to true to output visual
    :return:       Tuple with the two largest elements from the list
    """
    if len(lst) < 2:
        return lst

    if visual:
        print(lst)

    winners = []
    
    # For a winning number key, store a list of values that 
    # it 'beat' in the tournament 
    losers = {}

    start_size = 2**(ceil(log2(len(lst))))
    
    # Number of slots for the 'tournament round', 
    # including empty slots for byes.
    size = start_size
    
    # The number of elements, or non-empty slots on tournament round
    num_elements = len(lst)

    while size > 1:
        num_byes = size - num_elements
        index = 0
        # The first num_byes elements move on to next round automatically
        while index < num_byes:
            winners.append(lst[index])
            index += 1
        
        for i in range(index, num_elements, 2):
            first_greater = lst[i] > lst[i+1]

            winner  = lst[i] if first_greater else lst[i+1]
            loser = lst[i+1] if first_greater else lst[i]
            # Move on to next round
            winners.append(winner)

            if winner not in losers:
                losers[winner] = []
            # Add to list of values the winner has beaten
            losers[winner].append(loser)

        size /= 2
        num_elements = len(winners)
        lst = list(winners)
        winners = []

        if visual:
            print(lst)

    largest = lst[0]

    loser_list = losers[largest]
    second_largest = loser_list[0]

    if visual:
        print("Searching losers list for second largest")
        print(loser_list)

    for i in range(1, len(loser_list)):
        if loser_list[i] > second_largest:
            second_largest = loser_list[i]

    if visual:
        print(largest, second_largest)

    return (largest, second_largest)