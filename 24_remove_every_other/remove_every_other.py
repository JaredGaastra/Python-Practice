def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    # for num in lst:
    #     answer = []
    #     index = lst.index(num)
    #     if index % 2 == 0:
    #         answer.append(index)
    
    # return answer
    
    return lst[::2]