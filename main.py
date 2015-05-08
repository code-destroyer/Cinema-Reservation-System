from magic_reservation_system import Reservations
from settings import DB_NAME, SQL_FILE


def get_movies(self, DB_NAME):
    self.movies = DB_NAME.show_movies()

    print("Current movies:")
    for movie in self.movies:
        print("{}({})".format(self.name, self.raiting))

def get_movie_projections(self, DB_NAME):
    self.movie_projections = DB_NAME.show_movie_projections()

    print("Projections for movie {}:".format(self.movie))
    for projection in self.movie_projections:
        print("{} {} ".format(self.date, self.time))

def main():
    print("Select the number of a command from the following menu:")
    print("....MENU....")
    print("1. Show movies.")
    print("2. Show movie projections.")
    print("3. Make reservation.")
    print("4. Cansel reservation.")
    print("5. Exit.")
    print("6. Help.")

    user_choice = input("Command: ")
    if user_choice is 1:
        pass
    elif user_choice is 2:
        pass
    elif user_choice is 3:
        pass
    elif user_choice is 4:
        pass
    elif user_choice is 5:
        pass
    elif user_choice is 6:
        pass
    else:
        print("Invalid command!")
