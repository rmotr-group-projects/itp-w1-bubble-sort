"""This is the entry point of the program."""


def bubble_sort(list_of_numbers):
        for x in range(len(list_of_numbers) - 1, 0 , -1): # Iterate backwards through a list
            for y in range(x): # Iterate again until all numbers are sorted
                if list_of_numbers[y] > list_of_numbers[y + 1]:
                    list_of_numbers[y], list_of_numbers[y + 1] = list_of_numbers[y + 1], list_of_numbers[y] # if number before is bigger, swap the values
        return list_of_numbers     


if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
