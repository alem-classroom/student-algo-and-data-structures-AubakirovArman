
def binary_search(inputArray, value):
    high = len(inputArray) - 1
    low = 0

    found = False
    loc = -1

    while(found != True):
        if(high < low):
            return -1

        mid = low + (high - low) // 2

        if(inputArray[mid] < value):
            low = mid + 1

        if(inputArray[mid] > value):
            high = mid - 1

        if(inputArray[mid] == value):
            return mid
