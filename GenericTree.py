class TreeNode:
    # constructor
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def insert_child(self, child):
        self.children.append(child)
        child.parent = self

    def delete_node(self):
        p = self.parent
        self.parent = None
        p.children.remove(self)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

def print_tree(tree: TreeNode, level=0):
    if not tree.parent:
        print(tree.data)
    for child in tree.children:
        print("    "*level, "|---", child.data)
        if not len(child.children):
            level += 1
            print_tree(child, level)
            level -= 1
    

root  = TreeNode("root")

child1 = TreeNode("child1")
child2 = TreeNode("child2")
root.insert_child(child1)
root.insert_child(child2)

child3 = TreeNode("child3")
child4 = TreeNode("child4")
child1.insert_child(child3)
child2.insert_child(child4)

child5 = TreeNode("child5")
child6 = TreeNode("child6")
child1.insert_child(child5)
child2.insert_child(child6)

child7 = TreeNode("child7")
child3.insert_child(child7)

print_tree(root)

child1.delete_node()
print("--------------------")

print_tree(root)