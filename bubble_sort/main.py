#you need to pass the test so that travis doesnt get mad
#all of your functions are returning none
#you should RETURN, not only print (dont need to print at all if you dont wanna)
def bubble_sort(list_of_numbers):
    n = len(list_of_numbers)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if list_of_numbers[i-1] > list_of_numbers[i]:
                list_of_numbers[i-1], list_of_numbers[i] = list_of_numbers[i]\
                , list_of_numbers[i-1]
                swapped = True
    return list_of_numbers

#this here is not important
if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
    
    
"""
def swap(array, index1, index2):
    
    Java array swapping memes --> saving a few bytes of memory
    
    x = array[index1]
    array[index1] = array[index2]
    array[index2] = x
    return x
    
    Python array swapping memes
    
    x, y = y, x

procedure bubbleSort( A : list of sortable items )
   n = length(A)
   repeat 
     swapped = false
     for i = 1 to n-1 inclusive do
       /* if this pair is out of order */
       if A[i-1] > A[i] then
         /* swap them and remember something changed */
         swap( A[i-1], A[i] )
         swapped = true
       end if
     end for
   until not swapped
end procedure
"""
