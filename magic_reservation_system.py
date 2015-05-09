from movie_manager import ManageMovies
from cinema_hall import CinemaHall
import sqlite3
import sys
import re


class CommandLineInterface:

    def __init__(self):
        self.manager = ManageMovies()
        self.taken_by_you_seat = []

    def tuple_helper(self, seats):
        return re.findall('\d+', seats)

    def name_input(self):
        name = input('Step 1 (User): Choose name: ')
        if name == '':
            print('Invalid name!')
            self.name_input()
        for i in '0123456789':
            if i in name:
                print('Invalid name!')
                self.name_input()
        return name

    def ticket_input(self):
        tickets = input('Step 1 (User) Choose tickets: ')
        if tickets == '':
            print('Invalid tickets input!')
            self.ticket_input()
        for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if i in tickets:
                print('Invalid tickets input')
                self.ticket_input()
        return tickets

    def give_up_reservation(self):
        command = input('Press 1 to continue, 2 - to give up reservation: ')
        if command == '1':
            return True
        elif command == '2':
            print('You canceled your current request!')
            return False
        else:
            print('Invalid input!')
            self.give_up_reservation()
            return True

    def projection_availability_checker(self, tickets, movie_id):
        projection_id = input('Step 3 (Projection): Choose a projection: ')
        if int(projection_id) not in self.manager.projection_id_check(movie_id):
            print('No such projection for selected movie!')
            self.projection_availability_checker(tickets, movie_id)
        else:
            if self.manager.taken_seats_check(projection_id) < int(tickets):
                print("Not enough available seats!")
                self.manager.available_seats = 0
                self.projection_availability_checker(tickets, movie_id)
            else:
                self.manager.store_taken_seats(projection_id)
                for seat in self.manager.hall.taken_seats:
                    self.manager.hall.take_seats(seat)
        return projection_id

    def multiple_seat_selection(self, tickets):
        for i in range(1, int(tickets) + 1):
            seats = input('Step 4 (Seats): Choose seat {}: '.format(i))
            valid_tuple = self.tuple_helper(seats)
            if self.manager.hall.check_seat_validity(valid_tuple) and self.manager.hall.check_seat_availability(valid_tuple):
                if valid_tuple in self.taken_by_you_seat:
                    print('You already booked that seat!')
                    self.taken_by_you_seat = []
                    self.multiple_seat_selection(tickets)
                else:
                    self.taken_by_you_seat.append(valid_tuple)
            else:
                print('Invalid or already taken seat!')
                self.taken_by_you_seat = []
                self.multiple_seat_selection(tickets)

    def finalize(self):
        finalize_reservation = input("Enter keyword 'finalize' in order to submit your reservation, 'discard' - to give up reservation! ")
        if finalize_reservation == 'finalize':
            pass
        elif finalize_reservation == 'discard':
            print('You canceled your current request!')
            self.cinema_interface()
        else:
            print('Invalid input!')
            self.finalize()

    def cinema_interface(self):
        while True:
            command = input('Enter command: ')
            if command == 'show_movies':
                print('Current movies:')
                self.manager.show_movies()
            if command == 'show_movie_projections':
                movie_id = input("Enter movie_id: ")
                movie_date = input("Enter date(optional): ")
                self.manager.get_movie_name(movie_id, movie_date)
                print(self.manager.show_movies_projections(int(movie_id), movie_date))
            if command == 'make_reservation':
                name = self.name_input()
                tickets = self.ticket_input()
                if self.give_up_reservation():
                    pass
                else:
                    self.cinema_interface()
                print('Here is the list of the movies about to hit the big screen')
                self.manager.show_movies()
                movie_id = input('Step 2 (Movie): Choose a movie: ')
                print(self.manager.show_movies_projections(int(movie_id)))
                projection = self.projection_availability_checker(tickets, movie_id)
                #if self.give_up_reservation() is True:
                #   pass
                #else:
                #    self.reservation_process()
                print('Available seats (marked with a dot): ')
                print(self.manager.hall.get_cinema_hall())
                if self.give_up_reservation():
                    pass
                else:
                    self.cinema_interface()
                self.multiple_seat_selection(tickets)
                print("You're almost there! Check the info you have submitted for reservation :)\n Name: {}\n Movie ID: {}\n Projection ID: {}\n Number of tickets: {}\n".format(name,movie_id,projection,tickets))
                if self.give_up_reservation():
                    pass
                else:
                    self.cinema_interface()
                self.finalize()
                for seat in self.taken_by_you_seat:
                    self.manager.make_reservation(name, projection, seat)
                self.manager.db.commit()
                print('Congratulations! You successfully made your reservation! Enjoy the movie :)')
                sys.exit()

def main():
    CLI = CommandLineInterface()
    print("Welcome to NextDimensionCinema movie reservation system")
    print(55 * '*')
    print("Command list:\n 1 - show_movies\n 2 - show_movie_projections\n 3 - make_reservation")
    CLI.cinema_interface()








if __name__ == '__main__':
    main()
