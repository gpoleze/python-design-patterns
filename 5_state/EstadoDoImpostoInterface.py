from abc import ABC, abstractmethod


class EstadoDoImpostoInterface(ABC):

    def __init__(self):
        self.desconto_ja_aplicado = False

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass