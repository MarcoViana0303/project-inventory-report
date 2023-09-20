from typing import Dict
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        # Gera um relatório simples usando o método da classe base
        simple_report = super().generate()

        # Obtém a contagem de estoque por empresa usando um método interno
        company_stock_counts = self._get_company_stock_counts()

        # Inicializa o relatório completo com o relatório simples
        complete_report = (
            f"{simple_report}\n"
            "Stocked products by company:\n"
        )

        # Adiciona a contagem de estoque por empresa ao relatório completo
        for company, count in company_stock_counts.items():
            complete_report += f"- {company}: {count}\n"

        # Retorna o relatório completo
        return complete_report

    def _get_company_stock_counts(self) -> Dict[str, int]:
        # Coleta todos os produtos de todos os estoques
        all_products = [
            product
            for inventory in self.inventories
            for product in inventory.data
        ]

        # Inicializa um dicionário para contagem de estoque por empresa
        company_counts: Dict[str, int] = {}

        # Conta a quantidade de produtos por empresa
        for product in all_products:
            company_name = product.company_name
            if company_name in company_counts:
                company_counts[company_name] += 1
            else:
                company_counts[company_name] = 1

        # Retorna o dicionário de contagem de estoque por empresa
        return company_counts
