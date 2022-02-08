from Homework_22.models.order import Orders
from Homework_22.repositories.order_repository import OrderRepository


if __name__ == '__main__':

    orders = OrderRepository()  # create
    order_1 = Orders(id=10, product_id=1, quantity=4)
    order_2 = Orders(id=11, product_id=2, quantity=7)
    orders.add_orders(order_1, order_2)

    orders.change_quantity(id=1, quantity=100)  # update
    orders.delete_order(id=7)  # delete

    new_orders = orders.get_orders()  # read
    for order in new_orders:
        print(order)


