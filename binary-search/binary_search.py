
def binary_search(lst, fnd):
    if lst[0]==fnd:
        return 0
    elif lst[len(lst)-1]==fnd:
        return len(lst)-1
    elif len(lst)==2:
        return -1
    elif len(lst)==1 and lst[0]!=fnd:
        return -1
    col=0
    mid=len(lst)//2
    # print('*')
    # print(mid)
    # print(len(lst[:mid]))
    # print(len(lst[mid:]))
    # print(lst[:mid])
    # print(lst[mid:])
    # print(lst)
    # print('*')
    # input()
    if lst[mid]>fnd and (lst[mid-1]<fnd) ==False:
        return binary_search(lst[:mid], fnd)
    elif lst[mid]<fnd and (lst[mid+1]>fnd) == False:
        col=len(lst[:mid])
        return binary_search(lst[mid:], fnd)+col
    elif lst[mid]==fnd:
        return mid+col
    elif lst[mid]!=fnd and lst[mid+1]>fnd and lst[mid-1]<fnd:
        return -1
    
