class Passenger:
    """
    Represent an airline passenger.
    """

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return '{self.firstname} {self.lastname}'.format(self=self)


class Flight:
    """
        Represents an airline flight.
    """

    def __init__(self, flight_num, origin, destination, capacity=None):
        self.flight_num = flight_num
        self.passengers = []
        self.origin = origin
        self.destination = destination
        self.capacity = capacity

    def __str__(self):
        return 'Flight: {self.flight_num} from {self.origin} to {self.destination}'.format(self=self)

    def add_passenger(self, passenger: Passenger):
        """Appends a passenger to the passenger parameter (list)

            Parameters:
            passenger (Passenger): A passenger object
        """

        self.passengers.append(passenger)
