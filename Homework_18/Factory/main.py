from market import Market


if __name__ == "__main__":
    product_color = input("Enter product color(green, yellow, red): ")
    product_shape = input("Enter product shape(round, tapered, prolonged, herbaceous): ")
    product_size = input("Enter size of the product(small, big): ")
    prod = Market.get_product(product_color, product_shape, product_size)
    print(prod)
