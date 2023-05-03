from abc import ABC, abstractmethod

class AbstractAlgorithm(ABC):
    def __init__(self):
        self.found = False
        self.visited_fields = []
        self.found_path = []

    @abstractmethod
    def find(self):
        pass

    @abstractmethod
    def follow_found_path(self):
        pass
