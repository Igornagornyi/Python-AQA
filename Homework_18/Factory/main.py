from market import Market


if __name__ == "__main__":
    product_name = input("Enter product name (bannana, strawbarry, cellery or apple): ")
    prod = Market.get_product(product_name)
    print(prod)
