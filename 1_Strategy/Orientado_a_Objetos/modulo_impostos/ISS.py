from modulo_impostos.ImpostoInterface import ImpostoInterface


class ISS(ImpostoInterface):

    def calcula(self, orcamento):
        return orcamento.valor * 0.06
