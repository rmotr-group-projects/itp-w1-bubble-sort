"""This is the entry point of the program."""


def bubble_sort(list_1):
    
    for n in range((len(list_1))):
        for m in range((len(list_1))):
            if list_1[n] < list_1[m]:
                list_1[n], list_1[m] = list_1[m], list_1[n]
            
    return list_1


if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
