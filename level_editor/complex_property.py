from abc import ABC, abstractmethod


class ComplexProperty(ABC):

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def to_str(self):
        ...
