"""Model for aircraft flights."""

class Flight:
    """A Flight with a particular passenger aircraft."""

    def __init__(self, number, aircraft):
        # Check if the first 2 character are alpha chars
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}'")
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def allocate_seat(self, seat, passenger):
        """Alocate a seat in a passenger"""

        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already accupied")
        self._seating[row][letter] = passenger

    def aircraft_model(self):
        return self._aircraft.model()

    # Instance method - must pass self as an argument
    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")

        return row, letter

    def realocate_passenger(self, from_seat, to_seat):
        """Realocate a passenger to a different seat."""

        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to realocate in seat {from_seat}")

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[from_row][from_letter] is not None:
            raise ValueError(f"Seat {to_seat} already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s in None)
                for row in self._seating
                if row is not None)




class Aircraft:

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

class AirbusA319(Aircraft):

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"

class Boing777(Aircraft):

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "Boing 777"

    def seating_plan(self):
        return range(1, 56), "ABCDEGHJK"



def make_flight():
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat("12A", "Guido van Rossum")
    f.allocate_seat("15F", "Mnel Guida")
    f.allocate_seat("15E", "Gil Semedo")
    f.allocate_seat("1D", "Joel Simao")
    f.allocate_seat("1C", "Gorge de Liês")

    g = Flight("AF72", Boing777("G-GSPS"))
    g.allocate_seat("15K", "Lary van Rossum")
    g.allocate_seat("33G", "Jse Guida")
    g.allocate_seat("4B", "Brian Semedo")
    g.allocate_seat("4A", "Joelin Simao")

    return f, g