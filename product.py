class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.price}€ - {self.quantity}"

    def to_dict(self):
        return {
            "name" : self.name,
            "price" : self.price,
            "quantity" : self.quantity
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"], data["quantity"])
