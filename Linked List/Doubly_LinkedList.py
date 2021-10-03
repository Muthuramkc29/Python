class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):            #append()
        new_node = Node(data, None , self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            new_node = Node(data, None, None)
            self.head = new_node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        new_node = Node(data, itr, None)
        itr.next = new_node

    def delete_at_begin(self):
        if self.head is None:
            print("Linked List empty, cannot delete")
            return

        if self.head.next is None:
            self.head = None
            print("DLL is empty after deleting this element")
            return

        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self): #pop()
        if self.head is None:
            print("Linked List is empty, cant delete at end")
            return

        if self.head.next is None:
            self.head = None
            print("DLL is empty after deleting this element")
            return

        itr = self.head
        while itr:
            if itr.next.next is None:
                itr.next = None
            itr = itr.next

    def insert_after_node(self, data, x):
        if self.head is None:
            print("No value found, Linked List is empty")
            return

        if self.head.data == x:
            # ll.insert_at_end(data)
            self.head.next = Node(data, self.head, None)
            return

        itr = self.head
        while itr.next is not None:
            if itr.data == x:
                break
            itr = itr.next

        new_node = Node(data, self.head, itr.next)
        itr.next = new_node

    def insert_before_node(self, data, x):
        if self.head is None:
            print("No value found, Linked List is empty")
            return

        if self.head.data == x:
            ll.insert_at_beginning()
            return

        itr = self.head
        while itr.next.next is not None:
            if itr.next.data == x:
                break
            itr = itr.next

        new_node = Node(data, self.head, itr.next)
        itr.next = new_node

    def reversal(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        while itr.next is not None:
            itr = itr.next

        llstr = ""
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        l_lst = ""
        while itr is not None:
            l_lst += str(itr.data) + "----->"
            itr = itr.next
        print(l_lst)

    def get_length(self):
        if self.head is None:
            print("Linked List is empty")
            return

        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            ll.insert_at_end(data)


ll = LinkedList()

#insert values
ll.insert_values(["apple", "orange", "grapes"])
ll.print()
ll.reversal()




