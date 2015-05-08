class Reservations:

    def __init__(self):
        self.cursor = self.db.cursor()

    def show_movies(self):
        self.cursor.execute('''SELECT name, raiting
                                FROM Movies
                                ORDER BY raiting''')

    def show_movie_projections(self, movie_id):
        self.cursor.execute('''SELECT Movies.name, Projections.movie_id,
                                            type, projection_date, time
                                FROM Movies movie JOIN Projections projection
                                ON Projections.movie_id = Movies.id
                                ORDER BY projection_date''')
