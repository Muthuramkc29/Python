class Node:                                           # NODE Consists of a data value and a reference to next element
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None      # HEAD HOLDS THE MEMORY REFERENCE OF FIRST Element or head of a first node

    def insert_at_beginning(self, data):
        node = Node(data, self.head)       # HENCE HEAD OF new NODE is been set to new_node's memory location
        self.head = node                   # Hence it is added at first

    def insert_at_end(self, data):         # Inserting element at end
        if self.head is None:
            self.head = Node(data, None)
            return

        new_node = Node(data, None)

        itr = self.head                     # Head contains a node
        while itr.next:                     # While itr.next returns None, loop will happen
            itr = itr.next

        itr.next = new_node

    # Insert In_between

    def insert_after_node(self, data, x):     # eg: x = 20; Should find x's data in node, to insert After...

        itr = self.head
        while itr:         # Here head carries the NODE, Hence while itr.
            if itr.data == x:
                break
            itr = itr.next

        # if itr is None:
        #    print("Node not present in Linked List")
        # else:

        new_node = Node(data, itr.next)

        itr.next = new_node

    def insert_before_node(self, data, x):
        if self.head is None:
            raise Exception("No Node exists, then how to insert before?")

        if self.head.data == x:
            # ll.insert_at_beginning(data)
            new_node = Node(data, self.head)
            self.head = new_node
            return

        itr = self.head
        while itr.next is not None:
            if itr.next.data == x:
                break
            itr = itr.next

        if itr.next is None:
            print("The Value is not present")

        new_node = Node(data, itr.next)
        itr.next = new_node

    def delete_at_beginning(self):
        if self.head is None:                # Check whether the list is empty or not
            print("Linked List is Empty")
            return

        if self.head.next is None:
            self.head = None
            print("SLL is empty after deleting this element")
            return

        self.head = self.head.next           # Pointing the head to the next element, hence deleted first one.

    def delete_at_end(self):
        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is None:           # When only one element left then,
            self.head = None                 # if only one node is present then delete it, hence self.head is None
            print("SLL is empty after deleting this element")
            return

        itr = self.head
        while itr:
            if itr.next.next is None:        # itr.next.next throws an error because itr.next will be None and
                itr.next = None              # we will be calling none.ref is None which is not a promised text, we give
            itr = itr.next

    def delete_by_value(self, value):
        if self.head is None:
            print("Cant delete element")
            return

        if self.head.data == value:
            self.head = None
            return

        itr = self.head
        while itr.next is not None:              # Checking that next (ref) is None
            if itr.next.data == value:
                break
            itr = itr.next

        if itr.next is None:
            print("Should not give Value even you know its not there. okay ? ")
        else:
            itr.next = itr.next.next

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            ll.insert_at_end(data)

    def remove_at(self, index):                            # length = 5
        if index < 0 or index >= self.get_length():        # if index = 5, where length is 5,raise exception
            raise Exception("Not a Valid Index")

        if index == 0:
            self.head = self.head.next
            return

        # to insert at index 2, we should stop at index 1 to change the ref...
        itr = self.head
        count = 0                                         # Having a counter to count the index
        while itr:
            if count == index - 1:
                # we stop at index previous position
                itr.next = itr.next.next
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():        # if index = 5, where length is 5,raise exception
            raise Exception("Not a Valid Index")

        if index == 0:
            self.insert_at_beginning()
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                new_node = Node(data, itr.next)
                itr.next = new_node
                break
            itr = itr.next
            count += 1

    def get_length(self):
        count = 0

        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def print_linked_list(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head       # Where self.head holds a node as we insert
        l_list = ""

        while itr:
            l_list += str(itr.data) + "---->"
            itr = itr.next

        print(l_list)


ll = LinkedList()

# Length

print(ll.get_length())
ll.insert_values(["mango", "apple", "orange"])

ll.print_linked_list()

ll.remove_at(1)

ll.print_linked_list()

ll.insert_at(1, "figs")

ll.print_linked_list()
