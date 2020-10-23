import mysql.connector as mysql_connector


def init():
    db = mysql_connector.connect(
        host = "localhost",
        user = "CS4404",
        password = "ox06ox06",
        database = "CS4404"
    )

    return db

    if __name__ == "__main__":
        init()
