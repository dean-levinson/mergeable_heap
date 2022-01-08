from interactive_builder import InteraciveBuilder


class ConsoleMenu(object):
    def __init__(self, builder):
        self.builder = builder # type: InteraciveBuilder
        self.OPTIONS = {
            "makeheap": self.builder.make_heap,
            "insert": self.builder.insert,
            "union": self.builder.union,
            "min": self.builder.min,
            "extractmin": self.builder.extract_min,
            "print": self.builder.print,
            "printprev": self.builder.print_prev,
            "help": self.display_options_menu,
            "exit": self.exit
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
*) PrintPrev
*) Help
*) Exit
        """
        print(options)

    def loop(self):
        """
        Generate the console to the user.
        """
        self.display_options_menu()
        while True:
            command = input(">>> ").lower().strip()
            arg = None
            if len(command.split()) == 2:
                command, arg = command.split()
                if not arg.isdigit():
                    print("Second arg must be number")
                arg = int(arg)
            elif len(command.split()) > 2:
                print("Unsupported args")

            if command in self.OPTIONS:
                if arg:
                    self.OPTIONS[command](arg)
                else:
                    self.OPTIONS[command]()

            elif command:
                print("Invalid input. Run 'Help' for more information")

    @staticmethod
    def exit():
        print("Goodbye :)")
        exit(0)
