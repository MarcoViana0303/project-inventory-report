from datetime import datetime
from typing import List, Dict
from inventory_report.inventory import Inventory


class SimpleReport:
    def __init__(self) -> None:
        self.inventories: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        """
        Adiciona um estoque à lista de inventários.

        Args:
            inventory (Inventory): O inventário a ser adicionado.
        """
        self.inventories.append(inventory)

    def generate(self) -> str:
        """
        Gera um relatório a partir dos inventários armazenados.

        Returns:
            str: O relatório gerado no formato especificado.
        """
        oldest_manufacturing_date = self._find_oldest_manufacturing_date()
        closest_expiration_date = self._find_closest_expiration_date()
        company_with_largest_inventory = (
            self._find_company_with_largest_inventory()
        )

        report = (
            f"Oldest manufacturing date: {oldest_manufacturing_date}\n"
            f"Closest expiration date: {closest_expiration_date}\n"
            f"Company with the largest inventory: "
            f"{company_with_largest_inventory}"
        )

        return report

    def _find_oldest_manufacturing_date(self) -> str:
        """
        Encontra a data de fabricação mais antiga entre
        todos os produtos nos inventários.

        Returns:
            str: A data de fabricação mais antiga no formato "YYYY-MM-DD".
        """
        all_products = [
            product
            for inventory in self.inventories
            for product in inventory.data
        ]
        oldest_date = min(
            datetime.strptime(product.manufacturing_date, "%Y-%m-%d")
            for product in all_products
        )
        return oldest_date.strftime("%Y-%m-%d")

    def _find_closest_expiration_date(self) -> str:
        """
        Encontra a data de validade mais próxima
        entre os produtos que ainda não venceram.

        Returns:
            str: A data de validade mais próxima no formato "YYYY-MM-DD".
        """
        today = datetime.today()
        all_products = [
            product
            for inventory in self.inventories
            for product in inventory.data
        ]
        valid_products = [
            product
            for product in all_products
            if datetime.strptime(product.expiration_date, "%Y-%m-%d") >= today
        ]

        if valid_products:
            closest_date = min(
                product.expiration_date for product in valid_products
            )
            return closest_date
        else:
            return ""

    def _find_company_with_largest_inventory(self) -> str:
        """
        Encontra a empresa com o maior
        estoque com base na contagem de produtos.

        Returns:
            str: O nome da empresa com o maior estoque.
        """
        all_products = [
            product
            for inventory in self.inventories
            for product in inventory.data
        ]
        company_counts: Dict[str, int] = {}

        for product in all_products:
            company_name = product.company_name
            if company_name in company_counts:
                company_counts[company_name] += 1
            else:
                company_counts[company_name] = 1

        if company_counts:
            largest_company = max(
                company_counts.keys(),
                key=lambda k: company_counts[k]
            )
            return largest_company
        else:
            return ""
