# vehicle is the base class
class vehicle:
    def __init__(self):
        # dictionary of options
        self.vehicle_choices = {'make': '', 'model': '', 'color': '', 'doors': '', 'pushstart': '', 'transmission': ''}

    # functions for vehicle_choices in dictionary
    def setMake(self, make):
        self.vehicle_choices['make'] = make

    def setModel(self, model):
        self.vehicle_choices['model'] = model

    def setColor(self, color):
        self.vehicle_choices['model'] = color

    def setDoors(self, doors):
        self.vehicle_choices['doors'] = doors

    def setPushstart(self, pushstart):
        self.vehicle_choices['pushstart'] = pushstart

    def setTransmission(self, transmission):
        self.vehicle_choices['transmission'] = transmission

    # function for printing result
    def Options(self):
        print("")
        print(f"Your chosen dream car is listed below: ")
        print(f"The make: {self.vehicle_choices['make']}")
        print(f"The model: {self.vehicle_choices['model']}")
        print(f"The color: {self.vehicle_choices['color']}")
        print(f"The doors: {self.vehicle_choices['doors']}")
        print(f"The ignition type: {self.vehicle_choices['push start Y/N']}")


# car inherits from vehicle
class car(vehicle):
    def __init__(self):
        super().__init__()

    # override the method in the vehicle class
    def Options(self):
        print("")
        print(f"Your chosen dream car is listed below: ")
        print(f"The make: {self.vehicle_choices['make']}")
        print(f"The model: {self.vehicle_choices['model']}")
        print(f"The number of doors: {self.vehicle_choices['doors']}")
        print(f"The transmission type: {self.vehicle_choices['transmission']}")
        print(f"The ignition type: {self.vehicle_choices['pushstart']}")
        print("\n")


# pickup inherits from vehicle
class truck(vehicle):
    def __init__(self):
        super().__init__()

    # override the method in the vehicle class
    def Options(self):
        print("")
        print(f"Your chosen dream car is listed below: ")
        print(f"The make: {self.vehicle_choices['make']}")
        print(f"The model: {self.vehicle_choices['model']}")
        print(f"The number of doors: {self.vehicle_choices['doors']}")
        print(f"The transmission type: {self.vehicle_choices['transmission']}")
        print(f"The ignition type: {self.vehicle_choices['pushstart']}")
        print("\n")


print("Welcome to Mundo's Garage! Here, you can create you dream car!\n")
vehicle_type = "0"

while vehicle_type != "3":

    vehicle_type = input("Enter 1 to make a car and 2 to make a truck. Enter 3 to exit:\n")
    print("")

    if vehicle_type == "1":
        vehicle_choice = car()
        selected_make = input("Enter make: ")
        selected_model = input("Enter model: ")
        selected_color = input("Enter the color of your vehicle: ")
        selected_doors = input("Enter number of doors: ")
        selected_transmission = input("Enter standard or automatic for transmission type: ")
        selected_ignition = input("Type push start or key for the type of ignition: ")
        vehicle_choice.setMake(selected_make)
        vehicle_choice.setModel(selected_model)
        vehicle_choice.setColor(selected_color)
        vehicle_choice.setDoors(selected_doors)
        vehicle_choice.setTransmission(selected_transmission)
        vehicle_choice.setPushstart(selected_ignition)
        vehicle_choice.Options()

    elif vehicle_type == "2":
        vehicle_choice = car()
        selected_make = input("Enter make: ")
        selected_model = input("Enter model: ")
        selected_color = input("Enter the color of your vehicle: ")
        selected_doors = input("Enter number of doors: ")
        selected_transmission = input("Enter standard or automatic for transmission type: ")
        selected_ignition = input("Type push start or key for the type of ignition: ")
        vehicle_choice.setMake(selected_make)
        vehicle_choice.setModel(selected_model)
        vehicle_choice.setColor(selected_color)
        vehicle_choice.setDoors(selected_doors)
        vehicle_choice.setTransmission(selected_transmission)
        vehicle_choice.setPushstart(selected_ignition)
        vehicle_choice.Options()

    elif vehicle_type == "3":
        print("")
        print("Enjoy your dream vehicle!")
        print("")
    else:
        print("Wai..t we can get you in that Sports Car today, but you have to press 1 or 2 to continue! \n")
