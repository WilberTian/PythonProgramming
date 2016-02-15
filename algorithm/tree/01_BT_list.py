def BinaryTreeList(root):
    return [root, [], []]
    
def insertLeft(root, newBranch):
    temp = root.pop(1)
    if len(temp) > 1:
        root.insert(1, [newBranch, temp, []])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root, newBranch):
    temp = root.pop(2)
    if len(temp) > 1:
        root.insert(2, [newBranch, [], temp])
    else:
        root.insert(2,[newBranch, [], []])
    return root    
    
def getRootVal(root):
    return root[0]
    
def getLeftChild(root):
    return root[1]
    
def getRightChild(root):
    return root[2]
    
if __name__ == "__main__":
    root = BinaryTreeList(6)
    insertLeft(root, 1)
    insertLeft(root, 4)
    insertRight(root, 7)
    insertRight(root, 9)
    print root