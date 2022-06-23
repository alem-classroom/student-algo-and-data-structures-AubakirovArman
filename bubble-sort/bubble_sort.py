def bubble_sort(lst):
    for bs in range(len(lst)):
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                b=lst[i+1]
                lst[i+1]=lst[i]
                lst[i]=b
    return lst
    # sort the list via bubble sort
