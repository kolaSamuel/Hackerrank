
class Node(object):
    def __init__(self, value=None, parent=None):
        self.value = value
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.count = 1
        self.depth = 1

    def balance(self):
        left = self.left_child.depth if self.left_child else 0
        right = self.right_child.depth if self.right_child else 0
        return left, right

    def direction(self, node):
        if node == self.left_child:
            return 1  # Left
        return 2  # right

    def set_depth(self):
        self.depth = max(self.balance()) + 1


class AVL(object):
    def __init__(self, array):
        start = array[0]
        self.duplicates = {start}  # set of values
        self.root = Node(value=start)
        self.build(array)

    def build(self, array):
        length = len(array)
        for i in range(1, length):
            x = array[i]
            self.insert(x)

    def insert(self, x):
        start = self.root
        while 1:
            value = start.value
            if x == value:
                start.count += 1
                break
            elif x > value:
                if start.left_child:
                    start = start.left_child
                else:
                    start.left_child = Node(value=x, parent=start)
                    break
            else:
                if start.right_child:
                    start = start.right_child
                else:
                    start.right_child = Node(value=x, parent=start)
                    break
        self.transverse_up(start)

    def transverse_up(self, start):

        while start:
            left, right = start.balance()
            if abs(left-right) > 1:
                start = self.rotate(start, left, right)
            else:
                start.depth = max(left, right) + 1
                start = start.parent

    def rotate(self, node, left, right):

        parent = node.parent
        direction = parent.direction(node) if parent else 0

        if left > right:
            child = node.left_child
            _left, _right = child.balance()
            if _left > _right:
                self.update_parent(parent, child, direction)
                child.right_child, node.left_child = node, child.right_child
                node.set_depth()
                child.set_depth()
            else:
                grandchild = child.right_child
                self.update_parent(parent, grandchild, direction)
                child.right_child, node.left_child = grandchild.left_child, grandchild.right_child
                grandchild.left_child, grandchild.right_child = child, node
                node.set_depth()
                child.set_depth()
                grandchild.set_depth()
        else:
            child = node.right_child
            _left, _right = child.balance()
            if _right > _left:
                self.update_parent(parent, child, direction)
                child.left_child, node.right_child = node, child.left_child
                node.set_depth()
                child.set_depth()
            else:
                grandchild = child.left_child
                self.update_parent(parent, grandchild, direction)
                child.left_child, node.right_child = grandchild.right_child, grandchild.left_child
                grandchild.right_child, grandchild.left_child = child, node
                node.set_depth()
                child.set_depth()
                grandchild.set_depth()

        return parent

    def update_parent(self, parent, node, direction):

        if direction == 1:
            parent.left_child = node
        elif direction == 2:
            parent.right_child = node
        else:
            self.root.parent = node
            node.parent = None
            self.root = node

    def __str__(self):
        result = ''
        tree = [self.root]

        while len(tree):
            node = tree.pop()
            left = node.left_child.value if node.left_child else None
            right = node.right_child.value if node.right_child else None
            parent = node.parent.value if node.parent else 'root'
            string = " ".join(map(str, ['node', node.value, parent, 'left:', left, 'right:', right]))
            result += string
            result += '\n'
            for child in [node.right_child, node.left_child]:
                if child:
                    tree.append(child)
        return result


test = AVL([2, 1, 0, 3, 4, 5])
print(test)
