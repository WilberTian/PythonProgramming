class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def find(self, value):
        if self.value == value:
            return self
        elif self.value > value and self.left:
            return self.left.find(value)
        elif self.value < value and self.right:
            return self.right.find(value)
        return None
    
    def __repr__(self):
        return "{}".format(self.value)

        
class BSTwithNodes(object):
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(value)
                        break
                elif value > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(value)
                        break
                else:
                    break

                    
if __name__ == "__main__":
    tree = BSTwithNodes()
    li = [4, 2, 6, 1, 3, 7, 5]
    for i in li: 
        tree.insert(i)
    print tree.root
    print tree.root.right
    print tree.root.right.left
    print tree.root.right.right
    print tree.root.left
    print tree.root.left.left
    print tree.root.left.right

    print tree.root.find(30)                            