"""This is the entry point of the program."""
def bubble_sort(list_of_numbers):
    for passnum in range(len(list_of_numbers)-1,0,-1):
        for i in range(passnum):
            if list_of_numbers[i]>list_of_numbers[i+1]:
                temp = list_of_numbers[i]
                list_of_numbers[i] = list_of_numbers[i+1]
                list_of_numbers[i+1] = temp
    return (list_of_numbers)


        
if __name__ == '__main__':
   print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
