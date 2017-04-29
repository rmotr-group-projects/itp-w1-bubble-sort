"""This is the entry point of the program."""


def bubble_sort(list_of_numbers):
    #Determine how we break out of our while loop.
    #We have to use a while loop, because we don't
    #know how many iterations are needed.
	did_swaps_occur = True
	while did_swaps_occur == True:
	    #We need to know whether a swap happened, but not break
	    #out of the test if two numbers don't happen to be swapped.
	    #We use swap_test as a tracking method for this reason.
		swap_test = []
		#Logic here is that run through the range of the length
		#of the list, but not the last number. We do this because
		#we evaluate our current index to the value of the next index.
		#We get out of index range otherwise.
		for index in range(len(list_of_numbers) - 1):
			if list_of_numbers[index] > list_of_numbers[index + 1]:
			    #Not sure if we could do this without holding the pop
			    #value in a variable or not. We pop the current value,
			    #then insert after the next value.
				holdme = list_of_numbers.pop(index)
				list_of_numbers.insert((index + 1), holdme)
				#We mark that a swap did occur to inform our parent logic.
				swap_test.append("yes")
			else:
			    #We mark that a swap didn't occur here, but that
			    #doesn't mean a swap didn't happen elsewhere in
			    #the line.
				swap_test.append("no")
		#Let our parent logic know whether a swap happened in the line.
		if "yes" in swap_test:
			did_swaps_occur = True
		else:
			did_swaps_occur = False
	return list_of_numbers


if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
