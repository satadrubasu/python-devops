""" Model for Airline and Aircrafts exercise

1. Instance methods are methods which need the 'self' reference and are called on object/instance of the class
"""

class Flight:
    """ Class to hold an operating flight Code
        Note A Flight Object should have an Aircraft Object to reference all attributes of Airracft basic has-a relationship from oop

        1. f = Flight("BA773",Aircraft("G-EU","Airbus A312",num_rows=22,num_seats_per_row=6))

        2. Seating Allocation using list of dict
            each entry of the list will represent the row , and the dictionary will store the seat Name and a value holding NONE or name of passenger
            [{A:Rohit,B:Virat},{A:Chuck,B:Robbins,C:None},{},{},{}]

    """

    def __init__(self,flightNumber,aircraft):
        """  initializer with Class Invariant Checks  """
        if not flightNumber[:2].isalpha():
            raise ValueError(f"Cannot initialize a Flight whose first two characters arent Alpha Numeric : {flightNumber}")

        if not flightNumber[:2].isupper():
            raise ValueError(f"First two characters should be Upper case for a Valid Flight Number : {flightNumber}")

        if not (flightNumber[2:].isdigit() and int(flightNumber[2:]) <=9999):
            raise ValueError(f"Character 3 onwards should be a digits from 0 to 9999 : {flightNumber}")

        self._flightNumber = flightNumber
        self._aircraft = aircraft

        ## For Seat Allocation part , tuple unpacking
        rows,seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def flighNumber(self):
        return self._flightNumber

    def airlineCode(self):
        return self._flightNumber[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self,seat,passenger):
        """ Allocate a set to a passenger
         Args:
           seat :e.g 12C , 7F
           passenger : name of passenger

           Raises:
             ValueError: If the seat is unavailable
        """
        rows,seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]  # Take all from the string slice BUT THE LAST CHARACTER
        if letter not in seat_letters:
            raise ValueError(f"Invalid Set Letter {letter}")
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid Seat Row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid Row Number : {row}")

        if self._seating[row][letter] is not None:
            raise ValueError(f"Set {seat} is alreadfy booked")

        self._seating[row][letter] = passenger

########## three classes below showcase the Duck Typing Polymorphism  ##########
# Here Aircraft acts like the base class with three defined behaviour methods :
#  - registration - model - seating_plan
# Note how the 2 classes Boeing777 Airbus319 have the same methods but no syntax like java to say implements Aircraft.
# How the
#   3. f = Flight("BA773", Aircraft("G-EU", "Airbus A312", num_rows=22, num_seats_per_row=6))
#      f = Flight("BA773", Aircraft("G-EU", "Airbus A312", num_rows=22, num_seats_per_row=6))
####################################################################################
class Aircraft:
    """ Class to define varying aircraft type objects
    SEATING PLAN ( I is ommited to avoid confusion with 1 )
      A B C D E F G H J K
    """
    def __init__(self,registration,model,num_rows,num_seats_per_row):
        if not int(num_rows)>0 or not int(num_seats_per_row)>0:
            raise ValueError(f"Number of rows OR seats per row in  an aircraft can't be 0 or less")

        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1,self._num_rows+1),"ABCDEFGHJK"[:self._num_seats_per_row])
        # returns a tuple depending on the variables. e.g (range(1, 23), 'ABCDEF')


class Boeing777:

    def __init__(self,registration):
        self._registration = registration

    def registration(self,registration):
        return self._registration

    def model(self):
        return "Boeing777"

    def seating_plan(self):
        return (range(1, 56), "ABCDEFGHJK")

    def num_seats(self):
        rows,row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

class Airbus391:

    def __init__(self,registration):
        self._registration = registration

    def registration(self,registration):
        return self._registration

    def model(self):
        return "Airbus319"

    def seating_plan(self):
        return (range(1, 23), "ABCDEF")

    def num_seats(self):
        rows,row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


def make_flight():
    """
      A Module Level function available at airtravel modeule level
    """
    f = Flight("BA773", Aircraft("G-EU", "Airbus A312", num_rows=22, num_seats_per_row=6))
    f.allocate_seat("3B","Rohit")
    f.allocate_seat("3C", "Virat")
    f.allocate_seat("3D", "Anushka")
    f.allocate_seat("13B", "Ganguly")
    f.allocate_seat("12B", "Sachin")
    return f
