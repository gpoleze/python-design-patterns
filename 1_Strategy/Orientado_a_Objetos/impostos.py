from abc import ABC, abstractmethod


class ImpostoInterface(ABC):
    @abstractmethod
    def calcula(self, orcamento):
        pass


class ICMS(ImpostoInterface):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ISS(ImpostoInterface):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06
