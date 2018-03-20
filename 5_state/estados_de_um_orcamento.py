from EstadoDoImpostoInterface import EstadoDoImpostoInterface


class Analise(EstadoDoImpostoInterface):
    def aplica_desconto_extra(self, orcamento):
        if not self.desconto_ja_aplicado:
            orcamento.adiciona_desconto(orcamento.valor * 0.05)
            self.desconto_ja_aplicado = True
        else:
            raise Exception("O desconto não pode ser aplicado duas vezes")

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception("Orcamento deve estar reprovado ou aprovado para ser finalizado")

    def __str__(self):
        return "Em análise"


class Aprovado(EstadoDoImpostoInterface):
    def aplica_desconto_extra(self, orcamento):
        if not self.desconto_ja_aplicado:
            orcamento.adiciona_desconto(orcamento.valor * 0.02)
            self.desconto_ja_aplicado = True
        else:
            raise Exception("O desconto não pode ser aplicado duas vezes")

    def aprova(self, orcamento):
        raise Exception("Orcamento já aprovado")

    def reprova(self, orcamento):
        raise Exception("Orcamento aprovado não pode ser reprovado")

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

    def __str__(self):
        return "Aprovado"


class Reprovado(EstadoDoImpostoInterface):
    def aplica_desconto_extra(self, orcamento):
        raise Exception("Orcamento reprovado não recebe desconto extra")

    def aprova(self, orcamento):
        raise Exception("Orcamento reprovado não pode ser aprovado")

    def reprova(self, orcamento):
        raise Exception("Orcamento já reprovado")

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

    def __str__(self):
        return "Reprovado"


class Finalizado(EstadoDoImpostoInterface):
    def aplica_desconto_extra(self, orcamento):
        raise Exception("Orcamento finalizado não recebe desconto extra")

    def aprova(self, orcamento):
        raise Exception("Orcamento finalizado não pode ser aprovado")

    def reprova(self, orcamento):
        raise Exception("Orcamento fimalizado não pode ser reprovado")

    def finaliza(self, orcamento):
        raise Exception("Orcamento já finalizado")

    def __str__(self):
        return "Finalizado"
