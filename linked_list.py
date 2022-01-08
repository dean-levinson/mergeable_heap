from typing import Optional
import itertools

from node import Node
from exceptions import ItemNotFound


class NodeIterator(object):
    """
    Iterates over the nodes (by using node.next) until node.next == None.
    Supports LinkedList obj and Node obj.
    """
    def __init__(self, v):
        if isinstance(v, LinkedList):
            self.cur = v.head
        elif isinstance(v, Node):
            self.cur = v
        else:
            raise Exception(f"{self.__class__.__name__} supports only LinkedList or Node objects")

    def __next__(self):
        if not self.cur:
            raise StopIteration
        cur, self.cur = self.cur, self.cur.next
        return cur

    def __iter__(self):
        return self


class LinkedList(object):
    def __init__(self):
        self.head = None  # type: Optional[Node]
        self.tail = None  # type: Optional[Node]
        self.size = 0

    def insert_node_right(self, node):
        """
        Inserts the given node to the right side of the list. changes self.tail and self.size accordingly.
        """
        if not self.head:
            self.head = node
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        self.tail = node

        node.next = None
        self.size += 1

    def insert_node_left(self, node):
        """
        Inserts the given node to the left side of the list. changes self.head and self.size accordingly.
        """
        if not self.tail:
            self.tail = node
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

        node.prev = None
        self.size += 1

    def insert_node_after(self, existing_node, new_node):
        """
        Inserts new_node after existing_node in the list. Change self.tail and self.size accordingly.
        Doesn't validate that existing_node belongs to this list - Undefined behaviour.
        """

        if existing_node.next:
            existing_node.next.prev = new_node
            new_node.next = existing_node.next
        else:
            self.tail = new_node

        existing_node.next = new_node
        new_node.prev = existing_node
        self.size += 1

    def insert_node_before(self, existing_node, new_node):
        """
        Inserts new_node before existing_node in the list. Change self.head and self.size accordingly.
        Doesn't validate that existing_node belongs to this list - Undefined behaviour.
        """
        if existing_node.prev:
            existing_node.prev.next = new_node
            new_node.prev = existing_node.prev
        else:
            self.head = new_node

        existing_node.prev = new_node
        new_node.next = existing_node
        self.size += 1

    def insert_after(self, node, item):
        self.insert_node_after(node, Node(item))

    def insert_before(self, node, item):
        self.insert_node_before(node, Node(item))

    def extend_list_right(self, other_list):
        """
        Append the given list to the right of my list, by concatenating self.tail with other_list.head.
        Change self.size accordingly - using other_list.size.
        """
        node = other_list.head
        if not self.head:
            self.head = node.head
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        self.tail = node
        self.size += other_list.size
        self.tail = other_list.tail

    def extend_list(self, other_list):
        self.extend_list_right(other_list)

    def insert_node(self, node):
        return self.insert_node_left(node)

    def insert_left(self, item):
        assert item != Node, "Use insert_node_left instead"
        self.insert_node_left(Node(item))

    def insert_right(self, item):
        assert item != Node, "Use insert_node_right instead"
        self.insert_node_right(Node(item))

    def insert(self, item):
        self.insert_left(item)

    def delete_node(self, node):
        """
        Deletes the given node from the list.
        """
        # Relies on the fact the given node belongs to this list - problem...
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        self.size -= 1

    def search(self, item):
        """
        Iterates over the nodes until find a node that has the value of item.
        Raises ItemNotFound Exception if couldn't find such node.
        """
        for node in iter(self):
            if node.value == item:
                return node
        else:
            raise ItemNotFound(item)

    def __len__(self):
        return self.size

    def __iter__(self):
        return NodeIterator(self)

    def __getitem__(self, index):
        """
        Makes the object support indexing. Doesn't support slicing.
        For example -
            self[2] will iterate over the first 3 nodes and will return the third one.
            self[-1] will iterate all over the list and will return the last node (self.tail).
        Raises IndexError if out of range.
        """
        assert isinstance(index, int)
        if index > self.size - 1:
            raise IndexError("list index out of range")

        index = index % self.size
        try:
            return next(itertools.islice(self, index, index + 1))
        except StopIteration:
            raise IndexError(index)

    # def __repr__(self):
    #     return f"<{self.__class__.__name__} values={{" + ", ".join([str(node.value) for node in iter(self)]) + "}>"

    def __str__(self):
        """
        Iterates over the list and returns string representation of the list values.
        """
        return "LinkedList([" + ", ".join([str(node.value) for node in iter(self)]) + "])"


if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert(4)
    l1.insert(3)
    l1.insert(2)

    l2 = LinkedList()
    l2.insert(41)
    l2.insert(5)
    l2.insert(5)

    print(l1)
    print(l2)
    print(l2[-1])
    l1.extend_list(l2)
    print(l1, l1.size)
