from item import Item

class Phone(Item):
    pay_rate = 0.5
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / metods
        super().__init__(
            name, price, quantity
        )

        # Run validation to received arguments
        assert broken_phones >= 0, f"Quantity {broken_phones} is not greater or equal to zero!"

