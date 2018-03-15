class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        print(valor)


if __name__ == '__main__':
    from Orcamento import Orcamento
    from Item import Item

    # adicionado os impostos no import
    from impostos import ISS, ICMS, ICPP, IKCV

    orcamento = Orcamento()
    # adicionando itens ao orçamento
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))

    calculador_de_impostos = Calculador_de_impostos()
    print('ISS e ICMS')
    calculador_de_impostos.realiza_calculo(orcamento, ISS())    #imprime 50.0
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())   #imprime 30.0
    print('ISS com ICMS')
    calculador_de_impostos.realiza_calculo(orcamento, ICMS(ISS()))  # imprime 80.0
    calculador_de_impostos.realiza_calculo(orcamento, ISS(ICMS()))  # imprime 80.0

    # cálculo dos novos impostos
    print('ICPP e IKCV')
    calculador_de_impostos.realiza_calculo(orcamento, ICPP())  # imprime 25.0
    calculador_de_impostos.realiza_calculo(orcamento, IKCV())  # imprime 30.0
    print('ICPP com IKCV')
    calculador_de_impostos.realiza_calculo(orcamento, IKCV(ICPP()))  # imprime 55.0
    calculador_de_impostos.realiza_calculo(orcamento, ICPP(IKCV()))  # imprime 55.0