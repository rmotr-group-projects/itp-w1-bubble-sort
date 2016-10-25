"""This is the entry point of the program."""


def bubble_sort(a):
    for j in range(len(a)-1):
        for i in range(len(a)-1):
            if a[i+1]<a[i]:
                a[i+1],a[i]=a[i],a[i+1]
            print(a)



        
    return a

if __name__ == '__main__':
    print(bubble_sort([9, 1, 3, 11, 7, 2, 42, 111]))
