from timeit import timeit
from random import shuffle
import heapq
import matplotlib.pyplot as plt
from math import log2


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
        self.best = log2(len(array))
        self.duplicates = {start}  # set of values
        self.root = Node(value=start)
        self.missing = []
        self.wrong = []
        self.max_r = 0
        self.spins = 0
        self.build(array)

    def build(self, array):
        length = len(array)
        # self.plot()
        for i in range(1, length):
            x = array[i]
            self.insert(x)
            # self.plot()

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

        rotates = 0
        while start:
            left, right = start.balance()
            if abs(left-right) > 1:
                start = self.rotate(start, left, right)
                rotates += 1
                break
            else:
                start.depth = max(left, right) + 1
                start = start.parent
        self.max_r = max(self.max_r, rotates)
        self.spins += rotates

    def rotate(self, node, left, right):

        parent = node.parent
        direction = parent.direction(node) if parent else 0

        if left > right:
            child = node.left_child
            _left, _right = child.balance()
            if _left > _right:
                self.update_parent(parent, child, direction, node)
                # parent->child update
                if child.right_child:
                    child.right_child.parent = node
                child.right_child, node.left_child = node, child.right_child
                self.update_depth([node, child])
            else:
                grandchild = child.right_child
                self.update_parent(parent, grandchild, direction, node)
                # parent->child update
                if grandchild.left_child:
                    grandchild.left_child.parent = child
                if grandchild.right_child:
                    grandchild.right_child.parent = node
                child.parent = grandchild
                child.right_child, node.left_child = grandchild.left_child, grandchild.right_child
                grandchild.left_child, grandchild.right_child = child, node
                self.update_depth([node, child, grandchild])
        else:
            child = node.right_child
            _left, _right = child.balance()
            if _right > _left:
                self.update_parent(parent, child, direction, node)
                # parent->child update
                if child.left_child:
                    child.left_child.parent = node
                child.left_child, node.right_child = node, child.left_child
                self.update_depth([node, child])
            else:
                grandchild = child.left_child
                self.update_parent(parent, grandchild, direction, node)
                # parent->child update
                if grandchild.left_child:
                    grandchild.left_child.parent = node
                if grandchild.right_child:
                    grandchild.right_child.parent = child
                child.parent = grandchild
                child.left_child, node.right_child = grandchild.right_child, grandchild.left_child
                grandchild.right_child, grandchild.left_child = child, node
                self.update_depth([node, child, grandchild])

        return parent

    def update_depth(self, nodes):
        """ Updates each node in nodes """
        for node in nodes:
            node.set_depth()

    def update_parent(self, parent, node, direction, child):

        node.parent = parent
        child.parent = node
        if direction == 1:
            parent.left_child = node
        elif direction == 2:
            parent.right_child = node
        else:
            self.root.parent = node
            self.root = node

    def plot(self):
        max_depth = self.root.depth
        print(max_depth, 'log: ', self.best)
        tree = [(self.root, 0, 0)]
        levels = [[None]*pow(2, x) for x in range(max_depth)]
        while len(tree):
            node, level, index = tree.pop()
            levels[level][index] = node
            level += 1
            for child in [(node.left_child, level, index*2), (node.right_child, level, index*2 + 1)]:
                if child[0]:
                    tree.append(child)

        # print([[__.value if __ else None for __ in _] for _ in levels])
        plt.figure(1)
        for i in range(max_depth):
            x = []
            y = []
            for j in range(len(levels[i])):
                space = 1/(1 + pow(2, i))
                value = levels[i][j]
                if value:
                    _x = space*(j+1)
                    _y = max_depth-i
                    x.append(_x)
                    y.append(_y)
                    plt.annotate(value.value, (_x, _y))
                    draw_x = []
                    draw_y = []
                    space_2 = 1/(1 + pow(2, i+1))
                    __x = space_2*(1+j*2)
                    children = [(value.left_child, __x), (value, _x), (value.right_child, __x+space_2), ]
                    for (child, index) in children:
                        if child:
                            draw_x.append(index)
                            draw_y.append(_y-1+(child == value))
                    plt.plot(draw_x, draw_y, linewidth=1, linestyle='--', color='black')

            plt.scatter(x, y)
        plt.show()

    def worst_search(self):
        start = self.root
        while start:
            left, right = start.balance()
            if left > right:
                start = start.left_child
            else:
                start = start.right_child

    def __str__(self):
        max_depth = self.root.depth
        print(max_depth, 'log: ', self.best)
        result = ''
        tree = [(self.root, 0, 0)]
        values = set()
        relationships = set()
        start = ('root', self.root.value)
        relationships.add(start)
        limit = 0
        while len(tree):
            node, level, index = tree.pop()
            values.add(node.value)
            limit = max(limit, node.value)
            left = node.left_child.value if node.left_child else None
            right = node.right_child.value if node.right_child else None
            parent = node.parent.value if node.parent else 'root'

            for real in [(node.value, left), (node.value, right), (node.value, parent)]:
                relationships.add(real)

            string = ['node', node.value, parent, 'left:', left, 'right:', right, 'depth:', node.depth]
            string = " ".join(map(str, string))
            result += string
            result += '\n'
            level += 1
            for child in [(node.left_child, level, index*2), (node.right_child, level, index*2 + 1)]:
                if child[0]:
                    tree.append(child)

        for i in range(limit+1):
            if not (i in values):
                self.missing.append(i)

        for real in relationships:
            x, y = real
            if x and y:
                if not((y, x) in relationships):
                    self.wrong.append(real)

        return result


A = list(range(5*10**5))
# while 1:
#     shuffle(A)
#     test = AVL(A)
#     if abs(test.best - test.root.depth) >= 2:
#         break
# A = list(range(4))
test = AVL(A)
# print(A)
# print(test)
# test.plot()
# print('missing', test.missing)
# print('wrong', test.wrong)
print('max spins', test.max_r)
print('spins', test.spins)

print('done in', timeit('test.worst_search()', setup='from __main__ import test', number=5*10**5))
