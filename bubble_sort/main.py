"""This is the entry point of the program."""


def bubble_sort(list_of_numbers):
    flag = True                 # Flag for passing arguments
    while flag:                 # Iterate until a clean pass is achieved
        flag = False            # If it is a clean pass, this will remaun so
        # Run through all adjacent pairs
        for i in range( len(list_of_numbers) - 1 ):
            # Swap the adjacent pairs if they are not ordered
            if list_of_numbers[i] > list_of_numbers[i+1]:
                flag = True     # Raise flag as operated
                [list_of_numbers[i], list_of_numbers[i+1]] = [list_of_numbers[i+1], list_of_numbers[i]]
                
    return list_of_numbers


if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
