class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Function to insert nodes in level order
def insertLevelOrder(arr, root, i, n):
    # Base case for recursion
    if i < n:
        temp = newNode(arr[i])
        root = temp

        # insert left child
        root.left = insertLevelOrder(arr, root.left,
                                     2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, root.right,
                                      2 * i + 2, n)
    return root


def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)


# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    inOrder(root)

# trees = (5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))
