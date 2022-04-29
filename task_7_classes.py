class Vehicle:
    vehicle_type = "Ground Transport"
    __vehicle_number = 0

    def __init__(self, name, vehicle_mark, color):
        self.name = name
        self.color = color
        self.vehicle_mark = vehicle_mark
        Vehicle.__vehicle_number += 1

    def count(self):
        print(f"{self.__vehicle_number} vehicle")

    def display_general_info(self):
        print(f"{self.name} {self.vehicle_mark}, color: {self.color}")


class Bus(Vehicle):
    def __init__(self, name, vehicle_mark, color, number_of_seats, route):
        super().__init__(name, vehicle_mark, color)
        self._number_of_seats = number_of_seats
        self._route = route

    @property
    def number_of_seats(self):
        return self._number_of_seats

    @number_of_seats.setter
    def number_of_seats(self, seats):
        if isinstance(seats, int):
            self._number_of_seats = seats
        else:
            self._number_of_seats = 0

    @property
    def route(self):
        return self._route

    @route.setter
    def route(self, r):
        if r == "Unknown":
            self._route = "Depot"
        else:
            self._route = r

    def display_info(self):
        super().display_general_info()
        print(f"Parameters: available seats for passengers {self._number_of_seats}, route: {self._route}")


class Car(Vehicle):
    def __init__(self, name, vehicle_mark, color, weight):
        super().__init__(name, vehicle_mark, color)
        self.weight = weight

    def display_info(self, car_type):
        super().display_general_info()
        print(
            f"Parameters: {car_type} for transporting max weight {self.weight} kg")


busik1 = Bus("Bus", "Bohdan", "yellow", 45.8, "Unknown")
print(busik1.vehicle_type)
busik1.count()
busik1.display_info()

busik2 = Bus("Bus", "Ikarus", "white", 80, "Odesa-Dnepr")
busik2.count()
busik2.display_info()

truck = Car("Car", "Kamaz", "grey", 10000)
truck.count()
truck.display_info("truck")

car1 = Car("Car", "Mazda", "red", 500)
car1.count()
car1.display_info("passenger car")
