class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        print(imposto.calcula(orcamento))


if __name__ == '__main__':
    from orcamento import Orcamento
    # from impostos import ICMS,ISS
    from modulo_impostos.ICMS import ICMS
    from modulo_impostos.ISS import ISS


    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())  # imprimie 50.0
    calculador_de_impostos.realiza_calculo(orcamento, ISS())  # imprime 30.0
