from typing import Any, Callable

class BinaryNode:
    value: Any
    left_child = 'BinaryNode'
    right_child = 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.value)

    def is_leaf(self):
        if self.left_child is not None:
            return True
        else:
            return False

    def add_left_child(self, value: Any):
        if self.left_child is None:
            self.left_child = BinaryNode(value)
        else:
            return False

    def add_right_child(self, value: Any):
        if self.right_child is None:
            self.right_child = BinaryNode(value)
        else:
            return False

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_in_order(print)
        visit(self, end=' ')
        if self.right_child is not None:
            self.right_child.traverse_in_order(print)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_post_order(print)
        if self.right_child is not None:
            self.right_child.traverse_post_order(print)
        visit(self, end=' ')

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self, end=' ')
        if self.left_child is not None:
            self.left_child.traverse_pre_order(print)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(print)


class BinaryTree:
    root: 'BinaryNode'

    def __init__(self, value):
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.root.left_child is not None:
            self.root.left_child.traverse_in_order(print)
        visit(self.root, end=' ')
        if self.root.right_child is not None:
            self.root.right_child.traverse_in_order(print)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.root.left_child is not None:
            self.root.left_child.traverse_post_order(print)
        if self.root.right_child is not None:
            self.root.right_child.traverse_post_order(print)
        visit(self.root, end=' ')

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self.root, end=' ')
        if self.root.left_child is not None:
            self.root.left_child.traverse_pre_order(print)
        if self.root.right_child is not None:
            self.root.right_child.traverse_pre_order(print)







# root = BinaryNode(10)
tree = BinaryTree(10)
print(tree.root)
tree.root.add_left_child(9)
print(tree.root.left_child)
tree.root.add_right_child(2)
print(tree.root.right_child)
tree.root.left_child.add_left_child(1)
print(tree.root.left_child.left_child)
tree.root.left_child.add_right_child(3)
print(tree.root.left_child.right_child)
tree.root.right_child.add_left_child(4)
print(tree.root.right_child.left_child)
tree.root.right_child.add_right_child(6)
print(tree.root.right_child.right_child)
#tree.traverse_in_order(print)
print()
tree.traverse_pre_order(print)





#tree.root.traverse_in_order(print)