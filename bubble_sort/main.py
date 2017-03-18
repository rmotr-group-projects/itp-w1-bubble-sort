"""This is the entry point of the program."""


def bubble_sort(list_of_numbers):
    number = list(list_of_numbers)
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            if list_of_numbers[j] < list_of_numbers[i]:
                list_of_numbers[j], list_of_numbers[i] = list_of_numbers[i], list_of_numbers[j]
    return list_of_numbers


if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
