from modulo_impostos.ImpostoInterface import ImpostoInterface


class ICMS(ImpostoInterface):

    def calcula(self, orcamento):
        return orcamento.valor * 0.1
