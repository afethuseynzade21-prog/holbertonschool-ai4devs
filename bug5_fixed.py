import sqlite3


def find_user(conn, username):
    """Return the row of the user with the given username, or None."""
    # Fix: parameterized query, the username is passed as data and never becomes SQL code
    query = "SELECT id, username, role FROM users WHERE username = ?"
    return conn.execute(query, (username,)).fetchone()


if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER, username TEXT, role TEXT)")
    conn.execute("INSERT INTO users VALUES (1, 'alice', 'admin')")
    conn.execute("INSERT INTO users VALUES (2, 'bob', 'user')")

    print(find_user(conn, "bob"))           # expected: (2, 'bob', 'user')
    print(find_user(conn, "carol"))         # expected: None
    print(find_user(conn, "x' OR '1'='1"))  # expected: None (not the first user)
