from inventory_report.product import Product


def test_create_product() -> None:
    # Dados de exemplo para criar um produto
    id = "12345"
    company_name = "ABC Inc."
    product_name = "Product XYZ"
    manufacturing_date = "2023-09-15"
    expiration_date = "2023-12-31"
    serial_number = "SN123456"
    storage_instructions = "Store in a cool, dry place."

    # Cria um objeto Product com os dados de exemplo
    product = Product(
        id=id,
        company_name=company_name,
        product_name=product_name,
        manufacturing_date=manufacturing_date,
        expiration_date=expiration_date,
        serial_number=serial_number,
        storage_instructions=storage_instructions
    )

    # Verifica se os atributos do objeto Product
    # correspondem aos dados de exemplo
    assert product.id == id
    assert product.company_name == company_name
    assert product.product_name == product_name
    assert product.manufacturing_date == manufacturing_date
    assert product.expiration_date == expiration_date
    assert product.serial_number == serial_number
    assert product.storage_instructions == storage_instructions


if __name__ == "__main__":
    test_create_product()
