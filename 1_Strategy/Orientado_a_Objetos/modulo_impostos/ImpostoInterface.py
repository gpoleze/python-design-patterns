from abc import ABC, abstractmethod


class ImpostoInterface(ABC):

    @abstractmethod
    def calcula(self, orcamento):
        pass
