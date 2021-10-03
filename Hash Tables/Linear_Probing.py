class HashTable:

    def __init__(self):
        self.max = 10                                   # Memory allocated
        self.arr = [None for i in range(self.max)]      # Hash table stores values in arrays(list), initially None

    def get_hash(self, key):                       # given KEY (string) converted to a index...
        h = 0
        for string in key:
            h += ord(string)

        return h%self.max

    def __setitem__(self, key, value):
        h = self.get_hash(key)

        if self.arr[h] is None:
            self.arr[h] = (key, value)
            return

        if self.arr[h] is not None:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, value)
            return

    def find_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]  # self.arr[h:] + self.arr[:h]

    def find_slot(self, key, index):
        prob_range = self.find_prob_range(index)
        for ind_val in prob_range:
            if self.arr[ind_val] is None:
                return ind_val
            if self.arr[ind_val][0] == key:
                return ind_val
        raise Exception("Hash Map is Full")

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.find_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.find_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index]=None
        print(self.arr)

    def print_arr(self):
        print(self.arr)

t = HashTable()
t['march 6'] = 130
t['march 7'] = 140
t['march 8'] = 150
t['march 17'] = 120
t['march 6'] = 190
t['march 22'] = 440
t.print_arr()
t['march 22']
del t['march 6']
t.print_arr()
del t['march 22']
t.print_arr()
