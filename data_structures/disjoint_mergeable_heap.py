from data_structures.mergeable_heap import MergeableHeap


class DisjointMergeableHeap(MergeableHeap):
    def union(self, other_heap):
        pass


if __name__ == '__main__':
    h = DisjointMergeableHeap()
    h.insert(2)
    h.insert(13)
    h.insert(3)
    h.insert(11)
    h.insert(1)
    print(h)
    print(h, h.min())
    print(h.extract_min())
    print(h.min())
