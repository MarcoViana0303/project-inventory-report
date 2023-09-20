from inventory_report.product import Product


def test_product_report() -> None:
    # Dados de exemplo para criar um objeto Product
    id = "1"
    product_name = "Farinha"
    company_name = "Farinini"
    manufacturing_date = "01-05-2021"
    expiration_date = "02-06-2023"
    serial_number = "TY68 409C JJ43 ASD1 PL2F"
    storage_instructions = "precisa ser armazenado em local protegido da luz"

    # Cria um objeto Product com os dados de exemplo
    product = Product(
        id=id,
        product_name=product_name,
        company_name=company_name,
        manufacturing_date=manufacturing_date,
        expiration_date=expiration_date,
        serial_number=serial_number,
        storage_instructions=storage_instructions
    )

    # Verifica se o método __str__ retorna a frase correta
    expected_report = (
        f"The product {id} - {product_name} "
        f"with serial number {serial_number} "
        f"manufactured on {manufacturing_date} "
        f"by the company {company_name} "
        f"valid until {expiration_date} "
        "must be stored according to the following instructions: "
        f"{storage_instructions}."
    )
    assert str(product) == expected_report


if __name__ == "__main__":
    test_product_report()
