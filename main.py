from functools import wraps

from sorted_mergeable_heap import SortedMergeableHeap
from mergeable_heap import MergeableHeap
from exceptions import HeapEmpty


def parse_commands_from_file(file_path):
    with open(file_path, "rb") as fp:
        data = fp.read()
    commands = data.split()


def choose_heap():
    heap_dict = {
        "1": SortedMergeableHeap,
        "2": MergeableHeap,
        # "3": DisjointMergeableHeap,
    }
    while True:
        prompt = """
    Choose one of the following options - 
        1) Sorted linked lists
        2) Unsorted linked lists
        3) Disjoint unsorted linked lists
        
    Enter your choice here: """
        choice = input(prompt)
        if not choice.isdigit() or int(choice) > 3 or int(choice) < 1:
            print("Invalid input. try again...")
        else:
            return heap_dict[choice]


def from_console():
    while True:
        prompt = """
    Choose one of the following options - 
        1) From console
        2) From path - "./heap_instructions"

    Enter your choice here: """
        choice = input(prompt)
        if not choice.isdigit() or int(choice) > 2 or int(choice) < 1:
            print("Invalid input. try again...")
        else:
            return choice == "1"


class InteraciveBuild(object):
    def __init__(self, heap_obj):
        self.heap_obj = heap_obj
        self.current_heap = None
        self.previous_heap = None

    def make_heap(self):
        if self.current_heap:
            self.previous_heap = self.current_heap

        self.current_heap = self.heap_obj()

    @staticmethod
    def heap_operation(method):
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
            print(f"min value - {self.current_heap.min()}")
        except HeapEmpty:
            print("Heap is empty")

    @heap_operation
    def extract_min(self):
        try:
            print(f"extracted min value - {self.current_heap.extract_min()}")
        except HeapEmpty:
            print("Heap is empty")

    @heap_operation
    def print(self):
        print(self.current_heap)


class ConsoleMenu(object):
    def __init__(self, builder):
        self.builder = builder # type: InteraciveBuild
        self.OPTIONS = {
            "makeheap": self.builder.make_heap,
            "insert": self.builder.insert,
            "union": self.builder.union,
            "min": self.builder.min,
            "extractmin": self.builder.extract_min,
            "print": self.builder.print
        }

    @staticmethod
    def display_options_menu():
        options = """
        Console Menu
        ============
        Options:
        *) MakeHeap
        *) Insert
        *) Union
        *) Min
        *) ExtractMin
        *) Print
        """
        print(options)

    def loop(self):
        self.display_options_menu()
        while True:
            command = input(">>> ").lower()
            args = []
            if len(command.split()) >= 2:
                command, *args = command.split()

            if command in self.OPTIONS:
                self.OPTIONS[command](*args)

            else:
                print("Invalid input")


def main():
    heap_obj = choose_heap()
    if from_console():
        cm = ConsoleMenu(InteraciveBuild(heap_obj))
        cm.loop()

    else:
        pass


if __name__ == '__main__':
    main()
