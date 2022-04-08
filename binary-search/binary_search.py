def binary_search(lst, to_find):
    if to_find in lst:
        if len(lst)==1:
            return 0
        else:
            mid=int(len(lst)/2)
            if lst[mid]>to_find:
                return binary_search(lst[:mid], to_find)
            elif lst[mid]<to_find:
                return binary_search(lst[mid:], to_find)
            else:
                return lst[mid]
    else:
        return -1
    # search for the element to_find inside lst
    # if found, return index of element
    # else return -1
