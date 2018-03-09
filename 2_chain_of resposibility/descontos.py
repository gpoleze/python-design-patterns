from abc import abstractmethod, ABC


class DescontosInterface(ABC):
    # def __init__(self, proximo_desconto):
    #     self._proximo_desconto = proximo_desconto

    @abstractmethod
    def calcula(self, orcamento):
        pass


class DescontoPorCincoItens(DescontosInterface):
    def __init__(self, proximo_desconto):
        self._proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            return self._proximo_desconto.calcula(orcamento)


class DescontoPorMaisDeQuinhentosReais(DescontosInterface):
    def __init__(self, proximo_desconto):
        self._proximo_desconto = proximo_desconto

    def calcula(self, orcamento):

        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return self._proximo_desconto.calcula(orcamento)


class SemDesconto(DescontosInterface):
    def calcula(self, orcamento):
        return 0.0
