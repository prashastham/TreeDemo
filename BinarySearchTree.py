class BSTree:
    # Construtor
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    # Insert a new valie
    def insert(self, value):
        if self.value == value:
            return
        elif self.value < value:
            if self.right is None:
                self.right = BSTree(value)
                self.right.parent = self
            else:
                self.right.insert(value)
        else:  # self.value > value
            if self.left is None:
                self.left = BSTree(value)
                self.left.parent= self
            else:
                self.left.insert(value)

    # Search for a value
    def search(self, value):
        if self.value == value:
            print("{} was found".format(value))
            return True

        if self.value > value:
            if self.left != None:
                self.left.search(value)
            else:
                print("{} was not found".format(value))
                return False

        elif self.value < value:
            if self.right != None:
                self.right.search(value)
            else:
                print("{} was not found".format(value))
                return False

    # Function to check if a node is a leaf node
    def isLeaf(self):
        if self.right == None and self.right == None:
            return True
        else:
            return False

    # Function to find the maximum value of a tree
    def maxVal(self):
        if self.right is None:
            return self.value
        else:
            return self.right.maxVal()

    # Deletion of a node
    def delete(self, value):
        if self.value > value:
            if self.left != None:
                self.left.delete(value)
                return
            else:
                print("{} was not found".format(value))
                return False

        if self.value < value:
            if self.right != None:
                self.right.delete(value)
                return
            else:
                print("{} was not found".format(value))
                return False

        if self.value == value:
            # If node is a leaf node:
            #   Unset the node
            #   Remove connection from parent
            if self.isLeaf():
                if self.parent.left is not None and self.parent.left.value == value:
                    self.parent.left = None
                if self.parent.right is not None and self.parent.right.value == value:
                    self.parent.right = None
                self.value = None
                return
            # If a node has no left child: 
            #   Assign values of right child
            elif self.left is None:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return
            # If node has a left child: 
            #   Assign max of the sub tree
            #   Delete that value from the subtree
            else:
                self.value = self.left.maxVal()
                self.left.delete(self.value)
                return

    # Utility function to print BST
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = "%s" % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = "%s" % self.value
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = "%s" % self.value
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = "%s" % self.value
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


## Depth first traversal
# Inorder
def inOrderTraversal(root):
    if root is None:
        return
    # Traverse the left subtree
    inOrderTraversal(root.left)
    # Print value
    print(root.value, end=" ")
    # Traverse the right subtree
    inOrderTraversal(root.right)

# Preorder
def preOrderTraversal(root):
    if root is None:
        return
    # Print value
    print(root.value, end=" ")
    # Traverse the left subtree
    preOrderTraversal(root.left)
    # Traverse the right subtree
    preOrderTraversal(root.right)

# Postorder
def postOrderTraversal(root):
    if root is None:
        return
    # Traverse the left subtree
    postOrderTraversal(root.left)
    # Traverse the right subtree
    postOrderTraversal(root.right)
    # Print value
    print(root.value, end=" ")

## Breadth first traversal (level order traversal)
def levelOrderTraversal(root):
    if not root:
        return
    # Create empty queue
    queue = []
    # Enqueue the root node of the tree
    queue.append(root)
    # Loop while queue is not empty
    while(len(queue)):
        # Dequeue node from queue and visit node
        curr = queue[0]
        queue.remove(curr)
        print(curr.value, end=" ")

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)


tree = BSTree(20)
tree.insert(30)
tree.insert(15)
tree.insert(18)
tree.insert(4)
tree.insert(11)
tree.insert(16)
tree.insert(2)
tree.insert(19)
tree.insert(31)

tree.display()

# tree.search(11)
# tree.search(12)
# tree.search(30)
# tree.search(32)

tree.delete(31)
tree.display()
tree.delete(18)
tree.display()
tree.delete(20)
tree.display()

print("\nIn order traversal: ")
inOrderTraversal(tree)
print("\nPre order traversal: ")
preOrderTraversal(tree)
print("\nPost order traversal: ")
postOrderTraversal(tree)

print("\nLevel order traversal: ")
levelOrderTraversal(tree)