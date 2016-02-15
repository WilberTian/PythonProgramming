class BST(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
   
    def insert_left(self, value):
        self.insert(value)
    
    def insert_right(self, value):
        self.insert(value)
        
    def insert(self, value):
        if self.value == None:
            self.value = value
        else:
            if value > self.value:
                self.right = self.right and self.right.insert(value) or BST(value)
            else:
                self.left = self.left and self.left.insert(value) or BST(value)
        return self
        
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
        
        
if __name__ == "__main__":
    tree = BST()
    tree.insert(4)
    tree.insert(2)
    tree.insert(6)
    tree.insert(1)
    tree.insert(3)
    tree.insert(7)
    tree.insert(5)
    
    print tree.find(7)
    print tree.find(20)
    pass
        
            