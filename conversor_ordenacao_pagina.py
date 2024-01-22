from ordenacao_pagina_enum import OrdenacaoPaginaEnum


def converter_tipo_paginacao(tipoPaginacao):
    mapeamento = {
        "Principais escolhas para estadias longas": OrdenacaoPaginaEnum.popularity,
        "Casas e apartamentos primeiro": OrdenacaoPaginaEnum.upsort_bh,
        "Preço (mais baixo primeiro)": OrdenacaoPaginaEnum.price
    }

    return mapeamento.get(tipoPaginacao, None)