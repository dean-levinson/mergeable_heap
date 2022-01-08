from interactive_builder import InteraciveBuilder
from runners import ConsoleRunner, FileRunner
from data_structures.sorted_mergeable_heap import SortedMergeableHeap
from data_structures.mergeable_heap import MergeableHeap
from data_structures.disjoint_mergeable_heap import DisjointMergeableHeap


FILE_PATH = "heap_instructions.txt"


def choose_heap():
    heap_dict = {
        "1": SortedMergeableHeap,
        "2": MergeableHeap,
        "3": DisjointMergeableHeap,
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
    2) From path - "./heap_instructions.txt"

Enter your choice here: """
        choice = input(prompt)
        if not choice.isdigit() or int(choice) > 2 or int(choice) < 1:
            print("Invalid input. try again...")
        else:
            return choice == "1"


def main():
    heap_cls = choose_heap()
    should_forbid_jointed_items = bool(heap_cls == DisjointMergeableHeap)
    builder = InteraciveBuilder(heap_cls, should_forbid_jointed_items)
    if from_console():
        runner = ConsoleRunner(builder)
        runner.loop()

    else:
        runner = FileRunner(builder)
        runner.run_commands_from_file(FILE_PATH)


if __name__ == '__main__':
    main()
