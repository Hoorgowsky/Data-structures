from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    head: 'Node'
    tail: 'Node'

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        wierzcholek = Node(value)
        if self.head is None:
            self.head = wierzcholek
        else:
            tmp = self.head
            self.head = wierzcholek
            self.tail = tmp
            self.head.next = tmp
        return

    def append(self, value):
        wierzcholek = Node(value)
        if self.head is None:
            self.head = wierzcholek
        else:
            pocz = self.head
            while pocz.next is not None:
                pocz = pocz.next
            pocz.next = wierzcholek
            self.tail = wierzcholek
        return

    def node(self, index):
        pocz = self.head
        i = 0
        while i is not index:
            pocz = pocz.next
            i += 1
        return pocz

    def insert(self, index, value):
        item = self.node(index)
        tmp = item.next
        wierzcholek = Node(value)
        self.node(index).next = wierzcholek
        self.node(index).next.next = tmp
        return


    def pop(self):
        item = self.node(0)
        self.head = item.next
        return item

    def remove_last(self):
        pocz = self.head
        poprzedni = None
        while pocz.next is not None:
            poprzedni = pocz
            pocz = pocz.next
        poprzedni.next = None
        self.tail = poprzedni
        return pocz

    def len(self):
        pocz = self.head
        i = 0
        while pocz is not None:
            pocz = pocz.next
            i += 1
        return print('Dlugosc listy: ', i)

    def print(self):
        obecny = self.head
        while obecny is not None:
            print(obecny.value, '~> ', end='')
            obecny = obecny.next
        print("Null")
        return

    def remove(self, index):
        item = self.node(index)
        tmp = item.next.next
        item.next = tmp
        return


lista_ = LinkedList()
lista_.append(3)
lista_.append(2)