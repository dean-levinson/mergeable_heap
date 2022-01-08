from data_structures.linked_list import LinkedList


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
        """
        Iterates over the nodes.
        when find a node with bigger value then the item, inserts the item before that node and returns.
        """
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

    def __str__(self):
        """
        Iterates over the list and returns string representation of the list values.
        """
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

