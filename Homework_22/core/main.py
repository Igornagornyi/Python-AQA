from Homework_22.repositories.order_repository import OrderRepository


if __name__ == '__main__':

    orders = OrderRepository()  # create
    order_1 = {'id': 6, 'product_id': 1, 'quantity': 4}
    order_2 = {'id': 7, 'product_id': 2, 'quantity': 7}
    orders.add_order(order_1)
    orders.add_order(order_2)

    orders.change_quantity(id=1, quantity=100)  # update
    orders.delete_order(id=7)  # delete

    new_orders = orders.get_orders()  # read
    for order in new_orders:
        print(order)


