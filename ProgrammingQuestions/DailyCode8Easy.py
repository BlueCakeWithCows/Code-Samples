#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def isUnival(self):
        if hasattr(self, 'unival'): return self.unival
        
        unival = True
        children = [self.left, self.right] 
        for chil in filter(None, children):
            if chil.val != self.val: unival = False
        self.unival = unival
        
    def countUnival(self):
        self.isUnival()
        sum = 0
        if self.left != None: sum += self.left.countUnival()
        if self.right != None: sum += self.right.countUnival()
        if self.unival: sum +=1 
        return sum
    

if __name__ == "__main__":
    root = Node(0, Node(1), Node(0, Node(1,Node(1), Node(1)),Node(0)))
    assert root.countUnival() == 5
    

