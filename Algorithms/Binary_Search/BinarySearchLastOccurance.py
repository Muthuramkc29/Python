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


if __name__ == '__main__':

    numbers_list = [1,4,6,15,15,15,15,15,15,15,34,34,56]
    number_to_find = 15
    last_occurance = find_last_occurance(numbers_list,number_to_find)
    print(f"Index of Last occurance of {number_to_find} is at {last_occurance}th index")
