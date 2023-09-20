# Importa o módulo json para lidar com arquivos JSON.
import json
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


class JsonImporter(Importer):
    # Implementa o método import_data exigido pela classe abstrata Importer.
    def import_data(self) -> List[Product]:
        # Abre o arquivo JSON no modo de leitura ("r").
        with open(self.path, "r") as json_file:
            # Lê os dados do arquivo JSON e os converte em um objeto Python.
            data = json.load(json_file)

        products = []

        # Itera sobre os itens do arquivo JSON.
        for item in data:
            # Cria um objeto Product para cada item,
            # com os atributos correspondentes.
            product = Product(
                id=item["id"],
                product_name=item["product_name"],
                company_name=item["company_name"],
                manufacturing_date=item["manufacturing_date"],
                expiration_date=item["expiration_date"],
                serial_number=item["serial_number"],
                storage_instructions=item["storage_instructions"]
            )
            products.append(product)

        return products


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
