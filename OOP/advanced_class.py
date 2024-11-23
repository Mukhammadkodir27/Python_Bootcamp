class Car:
    is_new = True
    is_used = False
    def __init__(self, name=None, brand=None, color=None, year=None):
        self.name = name if name else "Default Name"
        self.brand = brand if brand else "Default Brand"
        self.color = color if color else "Default Color"
        self.year = year if year else 2024
    def get_car_info(self):
        return f"This is {self.name} manufactured by {self.brand} in {self.year}"
tesla_s1 = Car()
tesla_s1.is_electric = True
print(f"{tesla_s1.get_car_info()} and operates in electricity" if tesla_s1.is_electric else f"This car is not electric")
