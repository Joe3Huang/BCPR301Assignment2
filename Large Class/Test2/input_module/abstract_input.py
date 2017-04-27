from abc import ABCMeta, abstractmethod


class AbstractInput(metaclass=ABCMeta):
    @abstractmethod
    def input(self):
        pass