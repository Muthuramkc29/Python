class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add value to left
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add value to right
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        # First visit LeftNodes and then Root Node and then RightNodes
        elements = []
        # visits left Tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit BaseNode
        elements.append(self.data)

        #visits Right Tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        # First visits Left node and then Right Node and then Root Node
        elements = []
        
        # visit Left Node
        if self.left:
            elements += self.left.post_order_traversal()
            
        # visit Right Node
        if self.right:
            elements += self.right.post_order_traversal()
            
        # visit Root node/ Base Node
        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        # Visit Root node/ Base Node and then Left node and then Right Node
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def min(self):
        #returns left most element
        if self.left is None:
            return self.data
        return self.left.min()

    def max(self):
        # returns max element
        c = self
        while c.right:
            c = c.right

        return c.data

    def sum(self):
        sum = 0
        ele = self.pre_order_traversal()
        for elem in ele:
            sum += elem

        return sum

    def search(self, value):
        if value == self.data:                          # If val == RootNode...
            return "Node is Found"

        if value < self.data:
            if self.left:                               # If statement for checking if the Node is Present or Not....
                self.left.search(value)

        if value > self.data:
            if self.right:                              # If statement for checkiing self.right Node...
                self.right.search(value)

        return "Node not present"

    def delete(self, value):
        # Only one value being deleted So only one operation allowed...
        # ITS RECURSION... SO one operation strictly at one iter...
        # if-elif-else --> either one operation at one time....
        if self.data == None:
            print("No BST created")
            return

        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
            else:
                print("Node not Present")
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
            else:
                print("Node not Present")
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            # 2 Theories --> From the right subtree of self FindMin value or From left FindMax
            max_val = self.left.max()
            self.data = max_val                           # Copying the minimum value from right subtree
            self.left = self.right.delete(max_val)        # Deleting the duplicate value
            # VALUE DELETED.....
        return self                                       # Returning the object

if __name__ == '__main__':

    # SIMPLY HELPER METHOD:
    def build_tree(elements):
        root_node = BinarySearchTreeNode(elements[0])        # Assigning RootNode

        for i in range(1, len(elements)):                    # Elements following BST RULE (add_child() method)
            root_node.add_child(elements[i])

        return root_node                                     # Returning root node in build_tree

    numbers = [17,4,1,20,9,23,18,34]
    # Here number tree is a Root Node which is in build_tree()
    number_tree = build_tree(numbers)
    print("INORDER:",number_tree.in_order_traversal())
    print("MIN ELEMENT:",number_tree.min())
    print("MAX ELEMENT:",number_tree.max())
    print("POST-ORDER:",number_tree.post_order_traversal())
    print("PRE-ORDER:",number_tree.pre_order_traversal())
    print("SUM:",number_tree.sum())
    # print(number_tree.search(10))
    number_tree.delete(20)
    print("INORDER:", number_tree.in_order_traversal())
