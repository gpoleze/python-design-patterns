# -*- coding: UTF-8 -*-
# nota_fiscal.py

from datetime import date


class Nota_fiscal(object):

    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes='', observadores=None):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if (len(detalhes) > 20):
            raise NameError('Detalhe da nota superior à 20 caracteres!')
        self.__detalhes = detalhes
        self.__itens = itens

        # chamando as funções
        if not observadores is None:
            for observador in observadores:
                observador(self)

        # demais métodos omitidos


if __name__ == '__main__':
    from observadores import (envia_por_email, salva_no_banco, imprime)
    from Item import Item

    itens = [
        Item(
            nome='ITEM A',
            valor=100
        ),
        Item(
            nome='ITEM B',
            valor=200
        )
    ]

    nota_fiscal = Nota_fiscal(
        cnpj='012345678901234',
        razao_social='FHSA Limitada',
        itens=itens,
        observadores=(envia_por_email, salva_no_banco, imprime)
    )
