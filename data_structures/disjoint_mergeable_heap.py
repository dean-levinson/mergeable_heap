from data_structures.mergeable_heap import MergeableHeap


class DisjointMergeableHeap(MergeableHeap):
    def union(self, other_heap):
        self.list.extend_list(other_heap.list)


if __name__ == '__main__':
    h1 = DisjointMergeableHeap()
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

    h2 = DisjointMergeableHeap()
    h2.insert(8)
    h2.insert(3)
    h2.insert(4)
    h2.insert(11)

    h1.union(h2)
    print(h1)
