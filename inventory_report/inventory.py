from typing import List, Optional
from inventory_report.product import Product


class Inventory:
    # O construtor recebe um argumento 'data' que é uma
    # lista opcional de produtos.
    # Se 'data' for fornecido, ele é atribuído a '_data', caso
    # contrário, '_data' é inicializado como uma lista vazia.
    def __init__(self, data: Optional[List[Product]] = None):
        self._data: List[Product] = data if data is not None else []

    @property
    def data(self) -> List[Product]:
        # Propriedade 'data' que permite acesso à lista
        # '_data' de forma somente leitura.
        # Retorna uma cópia da lista '_data' para
        # evitar modificações indesejadas nos dados originais.
        return self._data.copy()

    def add_data(self, data: List[Product]) -> None:
        # recebe uma lista de produtos 'data'.
        # Adiciona todos os produtos da lista 'data' à lista '_data'.
        self._data.extend(data)
