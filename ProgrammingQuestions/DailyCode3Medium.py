#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def serialize(node):
    if node == None:
        return ""
    return str(node.val) + "," + serialize(node.left) + ","+serialize(node.right)
    
    
def deserialize_helper(string):
    dah  = string.split(',', 1)
    if len(dah)<2: 
        return None, ""
    value, rest = dah[0], dah[1]
    if value == "": return (None, rest)
    left, rest = deserialize_helper(rest) 
    right, rest = deserialize_helper(rest)
    node = Node(value, left, right)
    return (node, rest)
    
def deserialize(string):
    return deserialize_helper(string)[0]
    
if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    

