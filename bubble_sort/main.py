"""This is the entry point of the program."""
'''   n = length(A)
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
end procedure'''

def bubble_sort(list_of_numbers):
    n = len(list_of_numbers)
    swapped = True
    while swapped:
        swapped = False
        for num in range(1, n):
            if list_of_numbers[num-1] > list_of_numbers[num]:
                list_of_numbers[num-1], list_of_numbers[num] = list_of_numbers[num], list_of_numbers[num-1]
                swapped = True
    return list_of_numbers

if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
