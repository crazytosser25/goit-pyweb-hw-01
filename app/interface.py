"""imports"""
from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def asking(self, phrase):
        pass

    @abstractmethod
    def answer(self, phrase):
        pass


class CommandLineInterface(Interface):

    def asking(self, phrase):
        return input(f'{phrase}')

    def answer(self, phrase):
        print(phrase)
