from market import Market

if __name__ == "__main__":
    attributes = [input("Enter product color(green, yellow, red): "),
                  input("Enter product shape(round, tapered, prolonged, herbaceous): "),
                  input("Enter product size(small or big): ")]
    prod = Market.get_product(attributes)
    print(prod)
