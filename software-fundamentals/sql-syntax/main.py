import psycopg2
from flask import Flask, request, make_response
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import connection, cursor

app = Flask(__name__)

# connection - listen to the database
def get_database_connection(username: str) -> connection:
    return psycopg2.connect(f"dbname=movies user={username} host=localhost")

# cursor - how we interact with the database
def get_database_cursor(conn: connection) -> cursor:
    return conn.cursor(cursor_factory=RealDictCursor)

def search_movie(conn: connection, search: str) -> dict:
    with get_database_cursor(conn) as curs:
        curs.execute(
            "SELECT title, budget, overview, popularity FROM movies WHERE title ILIKE '%%s%';",
            [search]
            )
        rows = curs.fetchall()
    return rows

"api/movies/;DROP DATABASE movies;"

def load_all_movies(conn: connection) -> list[dict]:
    with get_database_cursor(conn) as curs:
        curs.execute(
            "SELECT title, budget, overview, popularity FROM movies;"
        )
        # fethchone, fetchmany, fetchall
        rows = curs.fetchall()
    return rows

@app.route('/movies', methods=['GET', 'POST'])
def movies():
    with get_database_connection("ruyzambrano") as conn:
        return load_all_movies(conn), 200

# Extra challenge: pagination

if __name__ == "__main__":
    app.run(port=8080, debug=True)