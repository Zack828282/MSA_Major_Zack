class Automobile():
    # Define a cunstructor
    # The constructor is a function that is called to create an automobile
    def __init__(self, make, model, vin, engine_size, owner, year, color):
        # Define class properties with the parameter values
        self.make = make
        self.model = model
        self.vin = vin
        self.engine_size = engine_size
        self.owner = owner
        self.year = year
        self.color = color
    
    # Create a method to print automobile data
    def print_data(self):
        print(f"{self.year} {self.make} {self.model}")
        print(f"VIN: {self.vin}, Engine size: {self.engine_size}")
        print(f"Owner: {self.owner}, Color: {self.color}\n")        