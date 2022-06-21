def binary_search(lst, to_find,col=0):
    if to_find in lst:
        if len(lst)==1:
            return 0
        else:
            mid=len(lst)//2
            
            if lst[mid]>to_find:
                return binary_search(lst[:mid], to_find,col)
            elif lst[mid]<to_find:
                return binary_search(lst[mid:], to_find,col+1)+len(lst[mid:])
            else:
                if col>1:
                    return mid-1
                return mid
    else:
        return -1
