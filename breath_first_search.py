from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def breadth_first_search(root):
    if not root:
        return []

    result = []
    queue = deque()

    queue.append(root)

    while queue:
        node = queue.popleft()  
        result.append(node.value)

        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Perform BFS on the tree
result = breadth_first_search(root)
print(result)
