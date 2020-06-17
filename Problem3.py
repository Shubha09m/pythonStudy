# Recursive Python program for level order traversal of Binary Tree

# A node structure


class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)

    # Print nodes at a given level


def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data)
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)





def height(node):
    if node is None:
        return 0
    else:

        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1



root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right=Node(4)

print("Level order traversal of binary tree is -")
printLevelOrder(root)