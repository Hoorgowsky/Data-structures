from typing import Any, List, Callable
import queue

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value):
        self.value = value
        self.children = []

    def is_leaf(self):
        if len(self.children) == 0:
            return print('Jest lisciem')
        else:
            return print('Nie jest lisciem')
        return

    def add(self, child):
        self.children.append(child)
        return


    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]):
        visit(self, end=' ')
        for child in self.children:
            child.for_each_deep_first(print)
        return

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]):
        visit(self, end=' ')
        q1 = queue.Queue()
        for childrens in self.children:
            q1.put(childrens)
        while q1.qsize() != 0:
            first = q1.get()
            visit(first, end=' ')
            for object in first.children:
                q1.put(object)
        return

    def search(self, value: Any):
        queue = []
        stan = False
        queue.append(self)
        for childrens in self.children:
            queue.append(childrens)
        while len(queue) > 0:
            first = queue[0]
            if first.value == value:
                print("Dzieci bieżącego więzła zawierają podaną wartość")
                stan = True
                return
            else:
                queue.pop(0)
        if not stan:
            print("Dzieci bieżącego więzła nie zawierają podanej wartości")
        return

    def __str__(self):
        return self.value



class Tree:
    root: 'TreeNode'

    def __init__(self, TreeNode):
        self.root = TreeNode

    def add(self, value: Any, parent_value: Any):
        if self.root.value is not None:
            q1 = queue.Queue()
            q1.put(self.root)
            while q1.qsize() != 0:
                first = q1.get()
                for elements in first.children:
                    q1.put(elements)
                if first.value == parent_value:
                    baby = TreeNode(value)
                    first.add(baby)
        else:
            print('Nie ma korzenia')
            return
        return

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]):
        q1 = queue.Queue()
        q1.put(self.root)
        while q1.qsize() != 0:
            first = q1.get()
            visit(first.value, end=' ')
            for elements in first.children:
                q1.put(elements)
        return

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]):
        visit(self.root, end=' ')
        for child in self.root.children:
            child.for_each_deep_first(print)
        return







root = TreeNode('F')
drzewo = Tree(root)
drzewo.add('B', root.value)
drzewo.add('G', root.value)
drzewo.add('A', 'B')
drzewo.add('D', 'B')
drzewo.add('C', 'D')
drzewo.add('E', 'D')
drzewo.add('I', 'G')
drzewo.add('H', 'I')

root.is_leaf()
drzewo.for_each_level_order(print)
print()
drzewo.for_each_deep_first(print)
print()
root.search('O')


