# Exercise Bubble_SORT

# BUBBLE SORT ALGORITHM

def bubble_sort(elements,key):
    # Outer Loop for till how many Times Inner Loop execute --> no of indexes
    for i in range(len(elements)-1):
        # For avoiding iterations for already swapped or sorted array
        swapped = False
        # Inner Loop -- Comparing two elements --> range(len(elements-1))
        for j in range(len(elements)-1-i):
            if elements[j][key] > elements[j+1][key]:
                temp = elements[j+1]
                elements[j+1] = elements[j]
                elements[j] = temp
                swapped = True
        # For Breaking OuterLoop
        if not swapped:               # Swapped will be True... If not(recognises either Swapped or Not)..
            break                     # And giving condition

if __name__ == '__main__':

    elements = elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    bubble_sort(elements, key='transaction_amount')
    print(elements)
