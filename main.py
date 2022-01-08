from interactive_builder import InteraciveBuilder
from console_menu import ConsoleMenu
from data_structures.sorted_mergeable_heap import SortedMergeableHeap
from data_structures.mergeable_heap import MergeableHeap


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


def main():
    heap_cls = choose_heap()
    if from_console():
        cm = ConsoleMenu(InteraciveBuilder(heap_cls))
        cm.loop()

    else:
        pass


if __name__ == '__main__':
    main()
