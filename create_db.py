import sqlite3
import sys
from settings import db_name, sql_file


def main():

    conn = sqlite3.connect(db_name)

    with open(sql_file, "r") as f:
        conn.executescript(f.read())
    conn.commit()

if __name__ == '__main__':
    main()
