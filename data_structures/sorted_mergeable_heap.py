from data_structures.sorted_linked_list import SortedLinkedList
from exceptions import HeapEmpty


class SortedMergeableHeap(object):
    def __init__(self):
        self.sorted_list = SortedLinkedList()  # Sorted doubly-linked list

    def insert(self, item):
        self.sorted_list.insert(item)

    def min(self):
        if not self.sorted_list.size:
            raise HeapEmpty()

        return self.sorted_list.head.value

    def extract_min(self):
        ret = self.min()
        self.sorted_list.delete_node(self.sorted_list.head)
        return ret

    def union(self, other_heap):
        """
        Merged algorithm for sorted lists. Complexity of O(n).
        """

        new_list = SortedLinkedList()

        my_node = self.sorted_list.head
        other_node = other_heap.sorted_list.head

        while True:
            if my_node is None and other_node is not None:
                min_node = other_node
                other_node = other_node.next

            elif my_node is not None and other_node is None:
                min_node = my_node
                my_node = my_node.next

            elif my_node is None and other_node is None:
                break

            elif my_node.value < other_node.value:
                min_node = my_node
                my_node = my_node.next

            elif my_node.value > other_node.value:
                min_node = other_node
                other_node = other_node.next

            elif my_node.value == other_node.value:  # Duplication
                min_node = my_node
                my_node = my_node.next
                other_node = other_node.next

            else:
                raise Exception("Shouldn't get here")

            new_list.list.insert_node_right(min_node)

        self.sorted_list = new_list

    def __str__(self):
        return str(self.sorted_list)


if __name__ == '__main__':
    h1 = SortedMergeableHeap()
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

    h2 = SortedMergeableHeap()
    h2.insert(8)
    h2.insert(3)
    h2.insert(4)
    h2.insert(11)

    h1.union(h2)
    print(h1)
