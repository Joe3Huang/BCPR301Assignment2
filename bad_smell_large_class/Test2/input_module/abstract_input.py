from abc import ABCMeta, abstractmethod


class AbstractInput(metaclass=ABCMeta):
    @abstractmethod
    def input(self):
         pass

    def input(self, prompt, output_key, validator_method):
        while True:
            try:
                input_data = self.view.input(prompt)
                if validator_method(input_data):
                    break
                else:
                    self.view.show("That was no valid input.  Try again...")
            except ValueError:
                self.view.show(
                    "Oops!  That was no valid number.  Try again...")
        return {output_key: input_data}

