class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


countNode = 0


def preOrder(node, mx):
    global countNode

    if node == None:
        return
    if node.data >= mx:
        countNode += 1
        mx = max(node.data, mx)

    # Traverse to the left
    preOrder(node.left, mx)

    # Traverse to the right
    preOrder(node.right, mx)

def insertLevelOrder(arr, root, i, n):
    # Base case for recursion
    if i < n:
        temp = Tree(arr[i])
        root = temp

        # insert left child
        root.left = insertLevelOrder(arr, root.left,
                                     2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, root.right,
                                      2 * i + 2, n)
    return root

def solution(T):
    return preOrder(T, -100000)


if __name__ == "__main__":
    root = Tree(5)
    root.left = Tree(3)
    root.right = Tree(10)
    root.left.left = Tree(20)
    root.left.right = Tree(21)
    root.right.left = Tree(1)
    solution(root)
    print(countNode)

    arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    inOrder(root)

# trees = (5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))