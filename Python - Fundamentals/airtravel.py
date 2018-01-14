__author__ = "Prikly Grayp"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "priklygrayp@gmail.com"
__status__ = "Development"

from pprint import pprint as pp

'''Model for aircraft flights'''

class Flight:
    '''A flight wityh a particular passenger aircraft.'''

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{number}'.".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{number}'.".format(number))

        if not number[2:].isdigit() and int(number[2:]) <= 9999:
            raise ValueError("Invalid route number '{number}'.".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [ {letter:None for letter in seats} for _ in rows ]


    def number(self):
        return self._number


    def airline(self):
        return self._number[:2]


    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):
        '''Parse a seat designator into a valid row and letter.

        Args:
            seat: A seat designator such as '12F'

        Returns:
            A tuple containing an integer and a string for row and seat.
        '''
        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError('Invalid seat letter {}'.format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError('Invalid seat row {}'.format(row_text))

        if row not in row_numbers:
            raise ValueError('Invalid row number {}'.format(row))

        return row, letter


    def allocate_seat(self, seat, passenger):
        '''Allocate a seat to a passenger.
        
        Args:
            seat: A seat designator such as '12C' or '21F.
            passenger: The passenger name.
            
        Raises:
            ValueError: If the seat is unavailable.
        '''
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError('Seat {} already occupied'.format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        '''Relocate a passenger to a different seat.

        Args:
            from_seat: The existing seat designator for the passenger to be moved.

            to_seat: The new seat designator.
        '''

        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError('No passenger to relocate in seat {}'.format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError('Seat {} is already occupied'.format(to_seat))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                    for row in self._seating
                    if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        '''An iterable series of passenger seating allocations.'''
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, '{}{}'.format(row, letter))

class Aircraft:


    def __init__(self, registration):
        self._registration = registration


    def registration(self):
        return self._registration


    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


    # def __init__(self, registration, model, num_rows, num_seats_per_row):
    #     self._registration = registration
    #     self._model = model
    #     self._num_rows = num_rows
    #     self._num_seats_per_row = num_seats_per_row
    #
    #
    # def registration(self):
    #     return self._registration
    #
    #
    # def model(self):
    #     return self._model
    #
    #
    # def seating_plan(self):
    #     return (range(1, self._num_rows + 1), 'ABCDEFGHJK'[:self._num_seats_per_row])

class AirbusA319(Aircraft):


    def model(self):
        return 'Airbus A319'


    def seating_plan(self):
        return range(1, 23), 'ABCDEF'



class Boeing777(Aircraft):


    def model(self):
        return 'Boeing 777'


    def seating_plan(self):
        return range(1, 56), 'ABCDEGHJK'

def make_flights():
    f = Flight('BA758', AirbusA319='G-EUPT')
    f.allocate_seat('12A', 'Malcolm van Aardt')
    f.allocate_seat('11B', 'Bryoni Currin')
    f.allocate_seat('15F', 'Russ van Aardt')
    f.allocate_seat('15E', 'Barbara van Aardt')

    g = Flight('AF72', Boeing777='F-GSPS')
    g.allocate_seat('12A', 'Malcolm van Aardt')
    g.allocate_seat('11B', 'Bryoni Currin')
    g.allocate_seat('15G', 'Russ van Aardt')
    g.allocate_seat('15E', 'Barbara van Aardt')


def console_carde_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}"      \
             "  Flight: {1}"    \
             "  Seat: {2}"      \
             "  Aircraft: {3}"  \
             "  |:".format(passenger, seat, flight_number, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()

'''TEST 1'''
# a = Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=6)
# print(a.registration())
# print(a.model())
# print(a.seating_plan())

'''TEST 2'''
# f = Flight('QR370', Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=6))
# print(f.aircraft_model())

'''TEST 3'''
# f = Flight('QR370', Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=6))
# pp(f._seating)

'''TEST 4'''
# f = Flight('QR370', Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=6))
# f.allocate_seat('12A', 'Malcolm van Aardt')
# f.allocate_seat('12B', 'Bryoni Currin')
# f.allocate_seat('15F', 'Russ van Aardt')
# f.allocate_seat('15E', 'Malcolm van Aardt')
# pp(f._seating)

'''TEST 5'''
# f = Flight('QR370', Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=6))
# f.allocate_seat('12A', 'Malcolm van Aardt')
# f.allocate_seat('11B', 'Bryoni Currin')
# f.allocate_seat('15F', 'Russ van Aardt')
# f.allocate_seat('15E', 'Barbara van Aardt')
# pp(f._seating)
# f.relocate_passenger('11B', '12B')
# pp(f._seating)

'''TEST 6'''
# f = Flight('QR370', Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=6))
# f.allocate_seat('12A', 'Malcolm van Aardt')
# f.allocate_seat('11B', 'Bryoni Currin')
# f.allocate_seat('15F', 'Russ van Aardt')
# f.allocate_seat('15E', 'Barbara van Aardt')
# f.relocate_passenger('11B', '12B')
# pp(f.num_available_seats())

'''TEST 7'''
# f = Flight('QR370', Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=6))
# f.allocate_seat('12A', 'Malcolm van Aardt')
# f.allocate_seat('11B', 'Bryoni Currin')
# f.allocate_seat('15F', 'Russ van Aardt')
# f.allocate_seat('15E', 'Barbara van Aardt')
# f.relocate_passenger('11B', '12B')
# f.make_boarding_cards(console_carde_printer)

'''TEST 7'''
# a = AirbusA319('G-EUPT')
# print(a.num_seats())
# b = Boeing777('F-GSPS')
# print(b.num_seats())