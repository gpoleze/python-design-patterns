from abc import ABC, abstractmethod


def imposto_composto(_funcao):
    def wrapper(self, orcamento):
        return _funcao(self, orcamento) + self._calculo_do_outro_imposto(orcamento)

    return wrapper


class Imposto(ABC):
    def __init__(self, outro_imposto=None):
        self.__outro_imposto = outro_imposto

    def _calculo_do_outro_imposto(self, orcamento):
        if self.__outro_imposto is None:
            return 0
        return self.__outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento):
        pass

"""ISS e ICMS usao o design pattern Decorator de maneira plena"""
class ISS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self._calculo_do_outro_imposto(orcamento)


class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self._calculo_do_outro_imposto(orcamento)

"""O ImpostoComRegrasTemplate implementa a mesama coisa, mas usando o decorator do Python """
class ImpostoComRegrasTemplate(Imposto):

    @imposto_composto
    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return orcamento.valor * self.maior_taxaxao()
        return orcamento.valor * self.menor_taxaxao()

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maior_taxaxao(self):
        pass

    @abstractmethod
    def menor_taxaxao(self):
        pass


class ICPP(ImpostoComRegrasTemplate):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500.0

    def maior_taxaxao(self):
        return 0.07

    def menor_taxaxao(self):
        return 0.05


class IKCV(ImpostoComRegrasTemplate):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    def maior_taxaxao(self):
        return 0.1

    def menor_taxaxao(self):
        return 0.06

    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if (item.valor > 100):
                return True
            return False
