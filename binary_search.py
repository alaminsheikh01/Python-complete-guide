def binary_search(list, item):
    low = 0
    heigh = len(list) - 1

    while low <= heigh:
        mid = (low + heigh)  #5
        guess = list[mid]

        if guess == item:
            return mid

        if guess > item:
            heigh = mid - 1

        else:
            low = mid + 1

    return None


my_list = [1, 3, 5, 7, 9, 4]
print(binary_search(my_list, 3))
