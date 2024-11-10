class GenericTree:
    # Constructor
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def insert(self, child):
        try:
            self.children.append(child)
            child.parent = self
        except AttributeError:
            print("Failed adding: {}".format(child.value))
            print("{} is not a Directory".format(self.value))
    
    def delete(self):
        p = self.parent
        self.parent = None
        p.children.remove(self)

    def getLevel(self):
        p = self.parent
        level = 0
        while p:
            p = p.parent
            level += 1
        return level

    def printTree(self):
        if self.parent is None:
            print("|---", self.value)
        if self.children and len(self.children):
            for child in self.children:
                level = child.getLevel()
                print("\t"*level, "|---", child.value)
                child.printTree()
        else:
            return

class Dir(GenericTree):
    def __init__(self, value):
        super().__init__(value)

class File(GenericTree):
    def __init__(self, value):
        super().__init__(value)
        self.children = None

root = Dir('root')
file1 = File('index.js')
dir1 = Dir('data')
root.insert(file1)
root.insert(dir1)

file2 = File('data1.csv')
file3 = File('data2.xlsx')
dir1.insert(file2)
dir1.insert(file3)

root.printTree()

dir1.delete()

root.printTree()