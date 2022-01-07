from sorted_linked_list import SortedLinkedList


class SortedMergeableHeap(object):
    def __init__(self):
        self.sorted_list = SortedLinkedList()  # Sorted doubly-linked list

    def insert(self, item):
        self.sorted_list.insert(item)

    def min(self):
        if not self.sorted_list.size:
            raise Exception("List is empty")

        return self.sorted_list.head.value

    def extract_min(self):
        ret = self.min()
        self.sorted_list.delete_node(self.sorted_list.head)
        return ret

    def __str__(self):
        return str(self.sorted_list)


if __name__ == '__main__':
    h = SortedMergeableHeap()
    h.insert(2)
    h.insert(3)
    h.insert(11)
    h.insert(13)
    print(h)
    print(h, h.min())
    print(h.extract_min())
    print(h.min())
