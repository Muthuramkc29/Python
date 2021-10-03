import heapq

list1 = [1,3,5,7,4,2,9]
second_smallest_element = heapq.nsmallest(2,list1)[1]
print(heapq.nsmallest(2,list1))
print(second_smallest_element)
heapq.