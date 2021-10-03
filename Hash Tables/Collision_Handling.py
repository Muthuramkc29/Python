# CHAINING - Collision Handling

class HashTable:

    def __init__(self):
        self.max = 10                                    # max item allocated in RAM in array
        self.arr = [[] for i in range(self.max)]        # array of 100 elements, initially None

    def get_hash(self, key):

        h = 0                               # Holds the sum of key, each element's ASCII ord->Value of char
        for string in key:                  # for each letter in String(key)
            h += ord(string)                # Sending to ord(string) to get ASCII value, summing it in h.
        return h % self.max                 # returns h%self.max ---> mod returns INDEX to store in array[self.arr]

    def __setitem__(self, key, value):      # adding item of particular key holding that value

        h = self.get_hash(key)              # first get index to store in our array allocated
        found = False
        for index, element in enumerate(self.arr[h]):   # Handling Collision
            if element[0] == key:
                self.arr[h][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key,value))

    def __getitem__(self, key):             # Finding the value coressponds to that key

        h = self.get_hash(key)              # Find the index for that key
        for index in self.arr[h]:
            if index[0] == key:
                break

        print(index[1])

    def __delitem__(self, key):

        h = self.get_hash(key)

        for index in self.arr[h]:
            if index[0] == key:
                self.arr[h].remove(index)
                break

    def print_arr(self):
        print(self.arr)


t = HashTable()
t.__setitem__("march 6", 30)
t.__setitem__("march 7", 140)
t.__setitem__("march 8", 130)
t.__setitem__("march 17", 120)
print("Items Setted")
print("Succesfully Handled Collision")
print()
t.print_arr()
print("Getting user defined item")
t.__getitem__("march 17")
print("Deleted the item")
t.__delitem__("march 6")
t.print_arr()
print("Setted a Item")
t.__setitem__("march 6", 30)
t.print_arr()
