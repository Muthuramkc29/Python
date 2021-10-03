# Finding Left occurance of a number  using Binary Search in a Sorted array
# Best way of finding OCCURANCES USING BINARY SEARCH

def find_left_occurance(numbers_list,number_to_find):

    left_index = 0
    right_index = len(numbers_list)-1
    mid_index = 0
    result = -1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            result = mid_index                              # Instead Returning mid_index, We find First Occurance
            right_index = mid_index - 1                     # right_index = mid_index - 1, to find First Occurance
        elif mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return result                                            # FIRST OCCURANCE.....

# Finding Right or Last occurance of a number  using Binary Search in a Sorted array

def find_last_occurance(numbers_list, number_to_find):

    left_index = 0
    right_index = len(numbers_list)-1
    mid_index = 0
    result = -1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            result = mid_index                              # Instead Returning mid_index, We find LAST Occurance
            left_index = mid_index + 1                      # left_index = mid_index + 1, to find LAST Occurance
        elif mid_number < number_to_find:
            left_index = mid_index + 1
        elif mid_number > number_to_find:
            right_index = mid_index - 1

    return result                                            # LAST OCCURANCE

def find_occurances(numbers_list, number_to_find):
    first_index_occurance = find_left_occurance(numbers_list, number_to_find)
    last_index_occurance = find_last_occurance(numbers_list, number_to_find)

    return [*range(first_index_occurance,last_index_occurance + 1)]

if __name__ == '__main__':

    numbers_list = [1,4,6,15,15,15,15,15,15,15,34,34,56]
    number_to_find = 15
    indices = find_occurances(numbers_list, number_to_find)
    print(f"Indexes of number {number_to_find} : {indices}")
