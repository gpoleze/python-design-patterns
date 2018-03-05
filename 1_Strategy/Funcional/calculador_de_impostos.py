class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, funcao_calculo_imposto):
        print(funcao_calculo_imposto(orcamento))


if __name__ == '__main__':
    import impostos
    from orcamento import Orcamento

    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(orcamento, impostos.calcula_ICMS)  # imprimie 50.0
    calculador_de_impostos.realiza_calculo(orcamento, impostos.calcula_ISS)  # imprime 30.0
