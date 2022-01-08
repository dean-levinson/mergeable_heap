from exceptions import HeapEmpty
from data_structures.linked_list import LinkedList


class MergeableHeap(object):
    def __init__(self):
        self.list = LinkedList()  # doubly-linked list

    def insert(self, item):
        self.list.insert(item)

    def _find_min_node(self):
        """
        Iterates over the nodes to find to node with the minimum value.
        Raises HeapEmpty if the heap is empty.
        """
        if not self.list.size:
            raise HeapEmpty()

        min_node = self.list.head
        for node in self.list:
            if node.value < min_node.value:
                min_node = node
        return min_node

    def min(self):
        return self._find_min_node().value

    def extract_min(self):
        min_node = self._find_min_node()
        self.list.delete_node(min_node)
        return min_node.value

    def union(self, other_heap):
        my_items = set()
        for node in self.list:
            my_items.add(node.value)
        for node in other_heap.list:
            if node.value in my_items:
                other_heap.list.delete_node(node)
        self.list.extend_list(other_heap.list)

    def __str__(self):
        return str(self.list)


if __name__ == '__main__':
    h1 = MergeableHeap()
    h1.insert(2)
    h1.insert(1)
    h1.insert(3)
    h1.insert(11)
    h1.insert(13)
    h1.insert(15)
    print(h1)
    print(h1, h1.min())
    print(h1.extract_min())
    print(h1.min())

    h2 = MergeableHeap()
    h2.insert(8)
    h2.insert(3)
    h2.insert(4)
    h2.insert(11)

    h1.union(h2)
    print(h1)
