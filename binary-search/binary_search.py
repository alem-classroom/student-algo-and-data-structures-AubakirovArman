def binary_search(lst, to_find):
	if len(lst) == 0:
		return False
	else:
		mid = len(lst) // 2
		if lst[mid] == value:
			return binary_search(lst[mid + 1:], value)
		else:
			return binary_search(lst[:mid], value)
