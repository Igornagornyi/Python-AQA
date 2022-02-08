from Homework_22.repositories.order_repository import OrderRepository
from Homework_22.repositories.product_repository import ProductRepository


rep = ProductRepository()
products = rep.get_products()
print(products)

rep2 = OrderRepository()
orders = rep2.get_orders()
print(orders)