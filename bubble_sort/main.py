def bubble_sort(list_of_numbers):
    length = len(list_of_numbers)
    n = length - 1
    cycle = True
    test = length
    while cycle == True:
        if test > 0:
            test = n
            for i in range(0,n):
                if list_of_numbers[i] > list_of_numbers[i+1]:
                    list_of_numbers[i],list_of_numbers[i+1] = list_of_numbers[i+1], list_of_numbers[i]
                    test += 1
                else:
                    test -= 1
        else:
            cycle = False


    return list_of_numbers