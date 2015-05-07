PRAGMA foreign_keys = ON

DROP TABLE IF EXISTS Movies;
CREATE TABLE  Movies(
        id INTEGER PRIMARY KEY,
        name TEXT,
        raiting FLOAT);

INSERT INTO Movies VALUES('Avengers: Age of Ultron', 8.1);
INSERT INTO Movies VALUES('Furious Seven', 7.8);
INSERT INTO Movies VALUES('Iron Man 3', 7.3);

DROP TABLE IF EXISTS Projections;
CREATE TABLE IF NOT EXISTS Projections(
        id INTEGER PRIMARY KEY,
        movie_id INTEGER,
        type TEXT,
        projection_date DATE,
        time TIME,
        FOREIGN KEY(movie_id) REFERENCES Movies(id));

INSERT INTO Projections VALUES(1, '3D', 2014-04-01, 19:10);
INSERT INTO Projections VALUES(1, '2D', 2014-04-01, 19:00);
INSERT INTO Projections VALUES(1, '4DX', 2014-04-01, 21:00);
INSERT INTO Projections VALUES(3, '2D', 2014-04-05, 20:20);
INSERT INTO Projections VALUES(2, '3D', 2014-05-02, 20:15);
INSERT INTO Projections VALUES(2, '3D', 2014-08-09, 19:30);
INSERT INTO Projections VALUES(2, '2D', 2015-09-08, 20:00);

DROP TABLE IF EXISTS Reservations;
CREATE TABLE IF NOT EXISTS Reservations(
        id INTEGER PRIMARY KEY,
        username TEXT,
        projection_id INTEGER,
        row INTEGER,
        col INTEGER,
        FOREIGN KEY(projection_id) REFERENCES Projections(id));
