class CinemaHall:

    TAKEN_SEAT = 'X'
    AVAILABLE_SEAT = '.'

    def __init__(self):
        self.empty_hall = 10*'..........\n'
        self.result = self.empty_hall.strip('\n')
        self.movie_hall = [[spot for spot in row] for row in self.result.split('\n')]
        self.count_taken_seats = 0
        self.taken_seats = [['2','2']]

    def take_seats(self, seats):
        if self.check_seat_validity(seats):
            if self.movie_hall[int(seats[0]) - 1][int(seats[1]) - 1] is CinemaHall.AVAILABLE_SEAT:
                self.movie_hall[int(seats[0]) - 1][int(seats[1]) - 1] = CinemaHall.TAKEN_SEAT

    def check_prefixed_number_of_seats(self, number_of_seats):
        available_seats = self.movie_hall.count('.')
        return available_seats < number_of_seats

    def check_seat_availability(self, seats):
        if self.check_seat_validity(seats):
            return self.movie_hall[int(seats[0]) - 1][int(seats[1]) - 1] is CinemaHall.AVAILABLE_SEAT

    def check_seat_validity(self, seats):
        if int(seats[0]) < 0 or int(seats[0]) > 10 or int(seats[1]) < 0 or int(seats[1]) > 10:
            return False
        else:
            return True

    def get_cinema_hall(self):
        string = '   1 2 3 4 5 6 7 8 9 10\n'
        i = 1
        j = ' '
        count = 1
        for row in self.movie_hall:
            for seat in row:
                string += str(i) + j + ' ' + seat
                i = ''
                j = ''
            j = ' '
            count += 1
            i = count
            string += '\n'
        return string


CH = CinemaHall()
#print(CH.taken_seats_check(2))
#print(CH.get_cinema_hall())
#CH.take_seats((4, 10))
#print(CH.get_cinema_hall())
'''seats = '(2,2)'
list_of_valid_tuples = []
for i in range(10):
    for j in range(10):
        list_of_valid_tuples.append((i,j))
if seats in [str(s) for s in list_of_valid_tuples]:
    print([seats[0], seats[1]])'''
