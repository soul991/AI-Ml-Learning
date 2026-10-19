class Laptop:
    storage_type = "SSD"

    def __init__(self, ram, storage, processor):
        self.ram = ram
        self.storage = storage
        self.processor = processor



    @classmethod
    def get_storage_type(cls):
        print(f"storage types of the laptop is {cls.storage_type}")


    def get_info(self):  #instance method
        print(f"Laptop has of ram of {self.ram} with a {self.storage} of {self.storage_type} storage and a {self.processor} processor.")


    @staticmethod
    def discount_calculator(price, discount):
        print(f"Final price = {int(price-((price*discount)/100))}")

l1 = Laptop("12 GB", "2TB", "Intel i5")
l2 = Laptop("8 GB", "1TB", "Intel i3")
l3 = Laptop("24 GB", "8TB", "Intel i9")

l1.get_info()
l2.get_storage_type()
l1.discount_calculator(40000, 22)