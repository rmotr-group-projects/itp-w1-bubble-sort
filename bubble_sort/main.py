"""This is the entry point of the program."""


def bubble_sort(list_of_numbers):
    for j in range(len(list_of_numbers)):
        for i in range(1, len(list_of_numbers)):
            x = list_of_numbers[i-1]
            y = list_of_numbers[i]
            if y<x:
                list_of_numbers[i] = x
                list_of_numbers[i-1] = y
    return list_of_numbers
            
            


if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
