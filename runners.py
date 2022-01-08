import os

from interactive_builder import InteraciveBuilder


class BuilderRunner(object):
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
        }


class ConsoleRunner(BuilderRunner):
    def __init__(self, builder):
        super(ConsoleRunner, self).__init__(builder)
        self.OPTIONS.update({"help": self.display_options_menu,
                             "exit": self.exit})
        
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
                    print("Second arg must be number. try again!")
                    return

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


class FileRunner(BuilderRunner):
    def run_command(self, command):
        arg = None
        if len(command.split()) == 2:
            command, arg = command.split()
            if not arg.isdigit():
                print("Second arg must be number, skipping command...")
                return
            arg = int(arg)
        elif len(command.split()) > 2:
            print("Unsupported args. skipping command...")

        if command in self.OPTIONS:
            if arg:
                self.OPTIONS[command](arg)
            else:
                self.OPTIONS[command]()

        elif command:
            print("Invalid command. skipping...")

    def run_commands_from_file(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(file_path)

        with open(file_path, "r") as fp:
            data = fp.read()
        commands = data.splitlines()
        print(f"Running commands from '{file_path}'")
        for command in commands:
            print(f"Running '{command}'")
            self.run_command(command.lower().strip())
