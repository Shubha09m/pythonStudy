
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def minimum_path(self,root, path, k):
        if root is None:
            return False
        path.append(root.key)

        if root.key == k:
            path.pop()
            return True

        if ((root.left != None and self.minimum_path(root.left, path, k)) or
            (root.right != None and self.minimum_path(root.right, path, k))):
            return True

        path.pop()
        return False



    def common(self,root, n1, n2):

        path1 = []
        path2 = []

        if (not self.minimum_path(root, path1, n1) or not self.minimum_path(root, path2, n2)):
            return -1


        i = 0

        set_a=set(path1)
        set_b=set(path2)
        if (set_a & set_b):
            list1=list(set_a & set_b)
            if len(list1)!=1:
                list1.sort()
                return list1[0],list1[1]
            else:
                return list1[0]



root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
root.right.right.left = Node(6)


print (root.common(root, 4, 6))
