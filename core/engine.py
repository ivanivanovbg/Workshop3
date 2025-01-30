import os
import core.command_factory as command_factory


class Engine:
    def __init__(self, factory):
        if isinstance(factory,command_factory.CommandFactory):
            self._command_factory = factory
            self._output = []
        else:
            raise ValueError("Invalid command factory provided !")


    def start(self):
        print("Enter command:")
        while True:
            try:
                input_line = input()
                command = self._command_factory.create(input_line)
                self._output.append(command.execute())
            except ValueError as verr:
                self._output.append(verr.args[0])

    def spill_the_beans(self):
        return os.linesep.join(self._output)
