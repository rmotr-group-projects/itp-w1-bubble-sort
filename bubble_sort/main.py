"""This is the entry point of the program."""

"""
def bubble_sort(list_of_numbers):
    flag = True
    while flag:
        flag = False
        for i, item in enumerate(list_of_numbers):
            if i+1<len(list_of_numbers) and list_of_numbers[i+1]<list_of_numbers[i] :
                list_of_numbers[i], list_of_numbers[i+1] = list_of_numbers[i+1], item
                flag = True
                
    return list_of_numbers    
    pass
"""
def bubble_sort(list_of_numbers):
    counter = len(list_of_numbers)
    temp = 0
    while counter>0:
        for i, item in enumerate(list_of_numbers):
            if i+1<counter and list_of_numbers[i+1]<list_of_numbers[i] :
                #list_of_numbers[i], list_of_numbers[i+1] = list_of_numbers[i+1], item
                temp = list_of_numbers[i+1]
                list_of_numbers[i+1] = item
                list_of_numbers[i] = temp
                #print (item)
        counter -= 1        
                
    return list_of_numbers    
    
if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))