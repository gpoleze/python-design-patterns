from EstadoDoImpostoInterface import EstadoDoImpostoInterface
from estados_de_um_orcamento import Analise


class Orcamento():
    def __init__(self):
        self.__itens = []
        self.estado_atual = Analise()
        self.__desconto_extra = 0

    # quando a propriedade for acessada, ela soma cada item retornando o valor do orçamento
    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    # retornamos uma tupla, já que não faz sentido alterar os itens de um orçamento
    def obter_itens(self):
        return tuple(self.__itens)

    # perguntamos para o orçamento o total de itens
    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto(self, valor):
        self.__desconto_extra += valor

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)


if __name__ == '__main__':
    from Item import Item

    orcamento = Orcamento()
    # adicionando itens ao orçamento
    orcamento.adiciona_item(Item('ITEM 1', 100))
    orcamento.adiciona_item(Item('ITEM 2', 50))
    orcamento.adiciona_item(Item('ITEM 3', 400))

    print(f'Estado atual: {orcamento.estado_atual} - Valor sem desconto extra {orcamento.valor}')

    orcamento.aplica_desconto_extra()
    print(f'Valor com desconto extra (em aprovação) {orcamento.valor}')
    # imprime 522.5 porque descontou 5% de 550.0

    orcamento.aprova()
    orcamento.aplica_desconto_extra()
    print(f'Estado atual: {orcamento.estado_atual} - Valor com desconto extra {orcamento.valor}')
    # imprime 512.05 porque descontou 2% de 522.5

    # orcamento.aplica_desconto_extra()
    # Levanta excecao por aplicar o mesmo desconto duas vezes

    orcamento.finaliza()

    # orcamento.aplica_desconto_extra()