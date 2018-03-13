from abc import ABC, abstractmethod


class Imposto(ABC):
    @abstractmethod
    def calcula(self, orcamento):
        pass


class ISS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06


class ImpostoComRegrasTemplate(Imposto):

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
