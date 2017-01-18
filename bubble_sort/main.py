"""This is the entry point of the program."""


def bubble_sort(list_of_numbers):
    length = len(list_of_numbers)
    count  = 0
    while count < length:
        for x in range(length-count-1):
            if list_of_numbers[x] > list_of_numbers[x+1]:
                list_of_numbers[x+1], list_of_numbers[x] = list_of_numbers[x], list_of_numbers[x+1]
        count += 1
    return list_of_numbers


if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
