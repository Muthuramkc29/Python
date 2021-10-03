class TreeNode:                                # BluePrint of a TreeNode
    def __init__(self, data):                  # data
        self.data = data
        self.children = []                     # contains Children
        self.parent = None                     # contains Parent

    def add_child(self, child):
        child.parent = self                    # so, Child.parent will be self...(object called itself a parent)
        self.children.append(child)            # Here child will be created, as it is a node of TreeNode...

    def print_tree(self):                               # printing Tree By RECURSION...
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):                       # Get level by Parent Memory (Available)
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

def build_product_tree():

    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Intel"))

    cellphone = TreeNode("CellPhone")
    cellphone.add_child(TreeNode("Iphone"))
    cellphone.add_child(TreeNode("Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    # print(tv.get_level())
    return root

if __name__=='__main__':
    root = build_product_tree()
    root.print_tree()
    pass
