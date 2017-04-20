"""This is the entry point of the program."""

def bubble_sort(a_list):
    errors = True
    error_check = 0
    while errors:
        if len(a_list) == 0:
            return a_list
        for i in range(len(a_list) - 1):
            if a_list[i] > a_list[i+1]:
                temp = a_list[i+1]
                a_list[i+1] = a_list[i]
                a_list[i] = temp
            else:
                error_check += 1
        if error_check == len(a_list) - 1:
            return a_list
        else:
            error_check = 0


if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
