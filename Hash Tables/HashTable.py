# Dictionaries - Uses HashTables Data Structure to store key,value Pairs....

class HashTable:

    def __init__(self):
        self.max = 100                                    # max item allocated in RAM in array
        self.arr = [None for i in range(self.max)]        # array of 100 elements, initially None

    def get_hash(self, key):

        h = 0                               # Holds the sum of key, each element's ASCII ord->Value of char
        for string in key:                  # for each letter in String(key)
            h += ord(string)                # Sending to ord(string) to get ASCII value, summing it in h.
        return h % self.max                 # returns h%self.max ---> mod returns INDEX to store in array[self.arr]

    def __setitem__(self, key, value):      # adding item of particular key holding that value

        h = self.get_hash(key)              # first get index to store in our array allocated
        self.arr[h] = value                 # Assign the value to that particular INDEX

    def __getitem__(self, key):             # Finding the value coressponds to that key

        h = self.get_hash(key)              # Find the index for that key
        return self.arr[h]                  # return the value of that index in array

    def print_arr(self):
        print(self.arr)


t = HashTable()
# t.add_item("march 6", 130)
# t.add_item("march 20", 140)
# t.add_item("march 9", 150)
t["march 6"] = 130                         # ITEM OPERATOR(__setitem__)
t["march 9"] = 140                         # ITEM OPERATOR

t.print_arr()
# print(t.get_item("march 20"))
print(t["march 6"])                        # Item Operator(__getitem__)
t.print_arr()
