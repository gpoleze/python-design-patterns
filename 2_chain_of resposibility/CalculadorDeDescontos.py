from descontos import DescontoPorCincoItens, DescontoPorMaisDeQuinhentosReais, SemDesconto


class CalculadorDeDescontos(object):
    def calcula(self, orcamento):
        desconto = DescontoPorCincoItens(
            DescontoPorMaisDeQuinhentosReais(
                SemDesconto()))

        return desconto.calcula(orcamento)


if __name__ == '__main__':
    from Orcamento import Orcamento
    from Item import Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B',  50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))
    # orcamento.adiciona_item(Item('Item D', 200.0))
    # orcamento.adiciona_item(Item('Item E', 150.0))
    # orcamento.adiciona_item(Item('Item F', 100.0))

    calculador_de_descontos = CalculadorDeDescontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    # print(f'Desconto calculado : {desconto}')
    print(f'Desconto calculado : {desconto}')
    # imprime 38.5
