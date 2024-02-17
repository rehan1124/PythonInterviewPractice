class Item:
    def __init__(self, name: str, price: int):
        self._name = name
        self._price = price

    def get_price(self):
        return self._price


class Order:
    def __init__(self, order_id, items: list):
        self._order_id = order_id
        self._items = items

    def calculate_total(self):
        total = sum(item.get_price() for item in self._items)
        return total


class OrderManager:
    def place_order(self, order: Order):
        total = order.calculate_total()
        print(f"Your order with total value of {total} INR has been placed.")


order_items = [Item("Product 1", 111), Item("Product 2", 222), Item("Product 3", 333)]
om = OrderManager()
om.place_order(Order(1, order_items))
