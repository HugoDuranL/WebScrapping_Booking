from enum import Enum

class OrdenacaoPaginaEnum(Enum):
    popularity = 'popularity', 1
    upsort_bh = 'upsort_bh', 2
    price = 'price', 3


    def __str__(self):
        return self.name
