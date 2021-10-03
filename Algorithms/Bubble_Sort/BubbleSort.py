# BUBBLE SORT ALGORITHM

def bubble_sort(elements):
    # Outer Loop for till how many Times Inner Loop execute --> no of indexes
    for i in range(len(elements)-1):
        # For avoiding iterations for already swapped or sorted array
        swapped = False
        # Inner Loop -- Comparing two elements --> range(len(elements-1))
        for j in range(len(elements)-1-i):
            if elements[j] > elements[j+1]:
                temp = elements[j+1]
                elements[j+1] = elements[j]
                elements[j] = temp
                swapped = True
        # For Breaking OuterLoop
        if not swapped:
            break

if __name__ == '__main__':

    elements = [5,9,2,1,67,34,88,34]
    bubble_sort(elements)
    print(elements)
