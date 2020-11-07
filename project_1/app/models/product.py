class Product:

    def __init__(self, product_name, product_description, stock_on_hand, out_of_stock = False, cost_price, sell_price, id = None):
        self.product_name = product_name
        self.product_description = product_description
        self.stock_on_hand = stock_on_hand
        self.out_of_stock = out_of_stock
        self.cost_price = cost_price
        self.sell_price = sell_price
        self.id = id

    # Methods
