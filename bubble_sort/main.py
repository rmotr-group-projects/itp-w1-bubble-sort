"""This is the entry point of the program."""


def bubble_sort(list_of_numbers) : 
    current = 0

    if isinstance(list_of_numbers, list) : 
        while current < len(list_of_numbers) : 
            for i in range(len(list_of_numbers)) : 
                if list_of_numbers[current] < list_of_numbers[i] : 
                    list_of_numbers[current], list_of_numbers[i] = list_of_numbers[i], list_of_numbers[current]
                else : 
                    pass
            current += 1
        return list_of_numbers
    else : 
        return "Not valid list"

if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
