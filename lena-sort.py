lim =
class Node(object):
    """
        Node class for binary search tree
        Note:
            maximum length search tree created so depth = value-1
    """

    def __init__(self, x, parent=None):
        self.data = x
        self.left_child = None
        self.right_child = None
        self.parent = parent
        self.depth = x-1


class BinaryTree(object):
    """
        Nothing special here, just a binary search tree
    """

    def __init__(self, size):
        self.root = Node(size)
        start = self.root
        for i in range(size-1, 0, -1):
            start.right_child = Node(i, start)
            start = start.right_child
        self.end = start


def transversal(start, arr):
    """

    :param start: start Node
    :param arr: array of strings
    :return: array
    """

    arr.append(str(start.data))
    if start.leftChild:
        transversal(start.leftChild)
    elif start.right_child:
        transversal(start.right_child)


for _ in range(int(input())):
    len_i, c = [int(x) for x in input().split()]
    _max = len_i*(len_i+1)/2
    step = len(bin(len_i)[:2])
