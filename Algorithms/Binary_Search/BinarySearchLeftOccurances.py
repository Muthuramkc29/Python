# Finding Left occurance of a number  using Binary Search in a Sorted array

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


if __name__ == '__main__':

    numbers_list = [1,4,6,15,15,15,15,15,15,15,34,34,56]
    number_to_find = 15
    first_occurance = find_left_occurance(numbers_list,number_to_find)
    print(f"Index of First occurance of {number_to_find} is at {first_occurance}th index")
