

def bubble_sort(list_of_numbers):
    for i in range(len(list_of_numbers)):
        for k in range(len(list_of_numbers)-1, i, -1):
            if(list_of_numbers[k]<list_of_numbers[k-1]):
                swap(list_of_numbers, k, k-1)
    return list_of_numbers
    
def swap(list_of_numbers, x, y):
    temp = list_of_numbers[x]
    list_of_numbers[x] = list_of_numbers[y]
    list_of_numbers[y]=temp


if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
