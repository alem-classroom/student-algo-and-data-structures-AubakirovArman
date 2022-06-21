def binary_search(lst, to_find):
    if to_find in lst:
        if len(lst)==1:
            return 0
        else:
            mid=int(len(lst)/2)
            if lst[mid]>to_find:
                return binary_search(lst[:mid], to_find)+len(lst[mid:])
            elif lst[mid]<to_find:
                return binary_search(lst[mid:], to_find)+len(lst[:mid])
            else:
                return mid
    else:
        return -1
