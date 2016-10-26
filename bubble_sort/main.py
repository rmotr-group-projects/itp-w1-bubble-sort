"""This is the entry point of the program."""


def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers)-1,1,-1):
        for j in range(i):
            if list_of_numbers[j] > list_of_numbers[j+1]:
                placeholder = list_of_numbers[j]
                list_of_numbers[j] = list_of_numbers[j+1]
                list_of_numbers[j+1] = placeholder
            
    return list_of_numbers



if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
