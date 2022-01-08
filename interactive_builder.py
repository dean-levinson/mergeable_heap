from functools import wraps

from exceptions import HeapEmpty


class InteraciveBuilder(object):
    """
    Wraps
    """
    def __init__(self, heap_obj):
        self.heap_cls = heap_obj
        self.current_heap = None
        self.previous_heap = None

    def make_heap(self):
        if self.current_heap:
            self.previous_heap = self.current_heap

        self.current_heap = self.heap_cls()

    @staticmethod
    def heap_operation(method):
        """
        Wraps methods that uses self.current_heap to validate that current_heap has already initialized.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            if not self.current_heap:
                print("You should initialize heap first...")
            else:
                return method(self, *args, **kwargs)

        return wrapper

    @heap_operation
    def insert(self, item):
        self.current_heap.insert(item)

    @heap_operation
    def union(self):
        if not self.previous_heap:
            print("You have initialized only one heap...")
        else:
            self.current_heap.union(self.previous_heap)

    @heap_operation
    def min(self):
        try:
            print(f"{self.current_heap.min()}")
        except HeapEmpty:
            print("Heap is empty")

    @heap_operation
    def extract_min(self):
        try:
            print(f"{self.current_heap.extract_min()}")
        except HeapEmpty:
            print("Heap is empty")

    @heap_operation
    def print(self):
        print(self.current_heap)
