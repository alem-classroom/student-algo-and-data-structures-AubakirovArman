def linear_search(lst, to_find):
  try:
    return lst.index(to_find)
  except:
    return -1
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
