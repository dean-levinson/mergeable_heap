from typing import Optional
import itertools

from linked_list import LinkedList


class SortedLinkedList(object):
    def __init__(self):
        self.list = LinkedList()  # type: LinkedList

    @property
    def head(self):
        return self.list.head

    @property
    def tail(self):
        return self.list.tail

    @property
    def size(self):
        return self.list.size

    def insert(self, item):
        for node in self.list:
            if item <= node.value:
                self.list.insert_before(node, item)
                return
        else:
            self.list.insert_right(item)

    def search(self, item):
        return self.list.search(item)

    def delete_node(self, node):
        self.list.delete_node(node)

    def __len__(self):
        return self.list.size

    def __iter__(self):
        return iter(self.list)

    def __getitem__(self, index):
        return self.list.__getitem__(index)

    # def __repr__(self):
    #     return f"<{self.__class__.__name__} values={{" + ", ".join([str(node.value) for node in iter(self)]) + "}>"

    def __str__(self):
        return "SortedLinkedList([" + ", ".join([str(node.value) for node in iter(self)]) + "])"


if __name__ == '__main__':
    l1 = SortedLinkedList()
    l1.insert(4)
    print(l1)
    l1.insert(3)
    print(l1)
    l1.insert(2)
    print(l1)
    l1.insert(5)
    print(l1)

