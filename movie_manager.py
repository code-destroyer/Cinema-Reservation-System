from settings import sql_file, db_name
from cinema_hall import CinemaHall
import sqlite3


class ManageMovies:

    def __init__(self):
        self.db = sqlite3.connect(db_name)
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()
        self.cursor2 = self.db.cursor()
        self.cursor3 = self.db.cursor()
        self.hall = CinemaHall()
        self.available_seats = 0

    def show_movies(self):
        result = self.cursor.execute('''SELECT * FROM Movies
                                ORDER BY rating''')
        for row in result:
            print('[{}] - {} - {}'.format(row['id'], row[1], row[2]))

    def show_movies_projections(self, movie_id, date=''):
        if date is '':
            self.cursor.execute('''SELECT id, time, type, projection_date FROM Projections
            WHERE movie_id = ?''', (movie_id,))
            for row in self.cursor:
                print('[{}] - {} {} {} - {} spots available'.format(row['id'], row['projection_date'], row['time'], row['type'], self.taken_seats_check(row['id'])))
        else:
            self.cursor.execute('''SELECT id, time, type
            FROM Projections WHERE movie_id = ? AND projection_date = ?
            ORDER BY projection_date''', (movie_id, date))
            for row in self.cursor:
                print('[{}] - {} {} - {} spots available'.format(row['id'], row['time'], row['type'], self.taken_seats_check(row['id'])))
        #return result

    def get_movie_name(self, movie_id, date=''):
        result = self.cursor.execute('''SELECT name FROM Movies WHERE id = ?''',(movie_id))
        for row in result:
            if date == '':
                print('Projections for movie "{}": \n'.format(row['name']))
            else:
                print('Projections for movie "{}" on date {}: \n'.format(row['name'], date))


    #def check_seat_availability(self, tickets):
     #   available_seats = self.movie_hall.count('.')
      #  return available_seats < tickets

    def projection_id_check(self, projection_id):
        self.cursor.execute('''SELECT id FROM Projections WHERE movie_id = ?''', (projection_id))
        valid_IDs = []
        for row in self.cursor:
            valid_IDs.append(row['id'])
        return valid_IDs

    def taken_seats_check(self, projection_id):
        self.cursor2.execute('''SELECT row, col FROM Reservations
                              WHERE projection_id = ?''', (projection_id,))
        self.hall.count_taken_seats = 0
        for row in self.cursor2:
            self.hall.taken_seats.append([row['row'], row['col']])
            self.hall.count_taken_seats += 1
        self.available_seats = 100 - self.hall.count_taken_seats
        return self.available_seats

    def store_taken_seats(self, projection_id):
        self.cursor3.execute('''SELECT row, col FROM Reservations
                              WHERE projection_id = ?''', (projection_id,))
        self.hall.taken_seats = []
        for row in self.cursor3:
            self.hall.taken_seats.append([row['row'], row['col']])

    def make_reservation(self, name, projection_id, seats):
        #self.hall.take_seats(seats)
        self.cursor.execute('''INSERT INTO Reservations(username, projection_id, row, col)
                               VALUES (?,?,?,?)''',(name, projection_id, seats[0], seats[1]))


def main():
    m = ManageMovies()
    #print(m.hall.get_cinema_hall())
    #print(m.taken_seats_check(2))
    print(m.projection_id_check('2'))
if __name__ == '__main__':
    main()
