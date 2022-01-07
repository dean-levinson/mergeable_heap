from linked_list import LinkedList


class MergeableHeap(object):
    def __init__(self):
        self.list = LinkedList()  # doubly-linked list

    def insert(self, item):
        self.list.insert(item)

    def _find_min_node(self):
        if not self.list.size:
            raise Exception("Heap is Empty")

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

    def __str__(self):
        return str(self.list)


if __name__ == '__main__':
    h = MergeableHeap()
    h.insert(2)
    h.insert(13)
    h.insert(3)
    h.insert(11)
    h.insert(1)
    print(h)
    print(h, h.min())
    print(h.extract_min())
    print(h.min())
