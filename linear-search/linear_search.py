def linear_search(lst, to_find):
    for idx,val in enumerate(lst):
        if val==to_find:
            return idx
    return -1
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
