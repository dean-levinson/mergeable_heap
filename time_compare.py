import random
from timeit import default_timer as timer

from data_structures.sorted_mergeable_heap import SortedMergeableHeap
from data_structures.mergeable_heap import MergeableHeap
from data_structures.disjoint_mergeable_heap import DisjointMergeableHeap


def time_compare():
    method = 'insert'
    print(f"\nCompare {method} -")
    laps = [10000, 100000, 1000000]
    for num_of_items in laps:
        print(f"\t{method} between {num_of_items} objects")

        # build heaps
        heaps = [SortedMergeableHeap(), MergeableHeap(), DisjointMergeableHeap()]

        # build SortedMergeableHeap separately because insert a lot of items takes time.
        items = list(set([random.randint(0, num_of_items * 10) for i in range(num_of_items)]))
        items.sort()
        for item in items:
            heaps[0].sorted_list.list.insert_right(item)

        for heap in heaps[1:]:
            items = list(set([random.randint(0, num_of_items * 10) for i in range(num_of_items)]))
            random.shuffle(items)
            for item in items:
                heap.insert(item)

        for heap in heaps:
            item_to_insert = random.randint(0, num_of_items * 10)
            print_method_time(heap, num_of_items, method, item_to_insert)

    method = 'min'
    print(f"\nCompare {method} -")
    for num_of_items in laps:
        print(f"\t{method} between {num_of_items} objects")

        # build heaps
        heaps = [SortedMergeableHeap(), MergeableHeap(), DisjointMergeableHeap()]

        # build SortedMergeableHeap separately because insert a lot of items takes time.
        items = list(set([random.randint(0, num_of_items * 10) for i in range(num_of_items)]))
        items.sort()
        for item in items:
            heaps[0].sorted_list.list.insert_right(item)

        for heap in heaps[1:]:
            items = list(set([random.randint(0, num_of_items * 10) for i in range(num_of_items)]))
            random.shuffle(items)
            for item in items:
                heap.insert(item)

        for heap in heaps:
            print_method_time(heap, num_of_items, method)

    method = 'extract_min'
    print(f"\nCompare {method} -")
    for num_of_items in laps:
        print(f"\t{method} between {num_of_items} objects")

        # build heaps
        heaps = [SortedMergeableHeap(), MergeableHeap(), DisjointMergeableHeap()]

        # build SortedMergeableHeap separately because insert a lot of items takes time.
        items = list(set([random.randint(0, num_of_items * 10) for i in range(num_of_items)]))
        items.sort()
        for item in items:
            heaps[0].sorted_list.list.insert_right(item)

        for heap in heaps[1:]:
            items = list(set([random.randint(0, num_of_items * 10) for i in range(num_of_items)]))
            random.shuffle(items)
            for item in items:
                heap.insert(item)

        for heap in heaps:
            print_method_time(heap, num_of_items, method)

    method = 'union'
    print(f"\nCompare {method} -")
    for num_of_items in laps:
        print(f"\t{method} between {num_of_items} objects")

        # build heaps
        heaps = [SortedMergeableHeap(), MergeableHeap(), DisjointMergeableHeap()]
        # build SortedMergeableHeap separately because insert a lot of items takes time.
        items = list(set([random.randint(0, num_of_items * 10) for i in range(num_of_items)]))
        items.sort()
        for item in items:
            heaps[0].sorted_list.list.insert_right(item)

        for heap in heaps[1:]:
            items = list(set([random.randint(0, num_of_items * 10) for i in range(num_of_items)]))
            random.shuffle(items)
            for item in items:
                heap.insert(item)

        other_heaps = [SortedMergeableHeap(), MergeableHeap(), DisjointMergeableHeap()]
        items = list(set([random.randint(0, num_of_items * 10) for i in range(num_of_items)]))
        items.sort()
        for item in items:
            other_heaps[0].sorted_list.list.insert_right(item)

        for heap in other_heaps[1:]:
            items = list(set([random.randint(0, num_of_items * 10) for i in range(num_of_items)]))
            random.shuffle(items)
            for item in items:
                heap.insert(item)

        for heap, other_heap in zip(heaps, other_heaps):
            print_method_time(heap, num_of_items, method, other_heap)


def print_method_time(heap, num_of_items, method, arg=None):
    start = timer()
    if arg:
        getattr(heap, method)(arg)
    else:
        getattr(heap, method)()
    end = timer()
    print(f"\t\t{heap.__class__.__name__}:".ljust(30), end - start)


if __name__ == '__main__':
    time_compare()
