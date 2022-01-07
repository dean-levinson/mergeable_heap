from typing import Optional
import itertools

from node import Node


class NodeIterator(object):
    def __init__(self, v):
        if isinstance(v, LinkedList):
            self.cur = v.head
        elif isinstance(v, Node):
            self.cur = v
        else:
            raise Exception(f"{self.__class__.__name__} supports only LinkedList or Node objects")
        self.first = True

    def __next__(self):
        # todo - refactor this
        if self.first:
            self.first = False
            if self.cur:
                return self.cur
            else:
                raise StopIteration

        if self.cur.next:
            self.cur = self.cur.next
            return self.cur
        else:
            raise StopIteration

    def __iter__(self):
        return self


class LinkedList(object):
    def __init__(self):
        self.head = None  # type: Optional[Node]
        self.tail = None  # type: Optional[Node]
        self.size = 0

    def insert_node_right(self, node):
        if not self.head:
            self.head = node
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        self.tail = node

        node.next = None
        self.size += 1

    def insert_node_left(self, node):
        if not self.tail:
            self.tail = node
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

        node.prev = None
        self.size += 1

    def insert_node_after(self, existing_node, new_node):
        # todo: consider add owner attr to Node so we can validate that this node belongs to this list

        if existing_node.next:
            existing_node.next.prev = new_node
            new_node.next = existing_node.next
        else:
            self.tail = new_node

        existing_node.next = new_node
        new_node.prev = existing_node
        self.size += 1

    def insert_node_before(self, existing_node, new_node):
        # todo: consider add owner attr to Node so we can validate that this node belongs to this list

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
        for node in iter(self):
            if node.value == item:
                return node
        else:
            raise Exception(f"{item} not found")

    def __len__(self):
        return self.size

    def __iter__(self):
        return NodeIterator(self)

    def __getitem__(self, index):
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
