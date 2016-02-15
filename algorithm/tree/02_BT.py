class BT(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def isLeaf(self):
        return self.left is None and self.right is None
        
    def insert_left(self, newNode):
        if not self.left:
            self.left = BT(newNode)
        else:
            temp = BT(self.left)
            temp.left = newNode
            self.left = temp
            
    def insert_right(self, newNode):
        if not self.right:
            self.right = BT(newNode)
        else:
            temp = BT(self.right)
            temp.right = newNode
            self.right = temp
    
    def __repr__(self):
        return "{}".format(self.value)
    
if __name__ == "__main__":            
    tree = BT(1)
    tree.insert_left(2)
    tree.insert_right(3)
    tree.left.insert_left(4)
    tree.left.insert_right(5)
    tree.right.insert_left(6)
    tree.right.insert_right(7)
    print tree