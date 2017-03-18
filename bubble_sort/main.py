"""This is the entry point of the program."""


def bubble_sort(a_list):
  place_holder = ""
  for first in range(len(a_list)):
    for second in range(len(a_list)):
      if a_list[first] < a_list[second]:
        place_holder = a_list[first]
        a_list[first] = a_list[second]
        a_list[second] = place_holder
        
  print(a_list)
  return a_list


if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
