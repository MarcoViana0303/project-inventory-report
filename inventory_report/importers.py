from typing import Dict, Type, List
from abc import ABC, abstractmethod
from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str):
        # Inicializador da class que recebe o caminho do arquivo como argumento
        self.path = path

    @abstractmethod  # Decorador que marca o método como abstrato
    def import_data(self) -> List[Product]:
        pass


class JsonImporter:
    pass


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
