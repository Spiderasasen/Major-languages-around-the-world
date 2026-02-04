import mysql.connector
import json

#path to load credentials
def load_credentials(path = "credentials.txt"):
    credentials = {}
    with open(path, "r") as f:
        for line in f:
            key,value = line.strip().split("=")
            credentials[key] = value
    return credentials

#connecting the data base
def connect_to_db():
    credentials = load_credentials()

    #checking if there is no error
    try:
        mydb = mysql.connector.connect(
            host = credentials["host"],
            user = credentials["user"],
            password = credentials["password"],
            database = credentials["database"]
        )
        return mydb

    #if there is it will tell us
    except Exception as e:
        print("Error loading your database: ", e)

#urniversal check
def universal_check(cursor, tabel, column, value) -> bool:
    #calls the table with the id of the table
    sql = f"select id{tabel} from {tabel} where {column} = %s"
    cursor.execute(sql, (value,))
    item = cursor.fetchone()
    #checks if the item exist, if so it returns true
    if item:
        return True
    return False


#inserting continents
def inserting_continents(cursor):
    if universal_check(cursor, "Continents", "Continent_name", "Europe"):
        return True
    return False

def main():
    db = connect_to_db()
    print("Connected to your database")

    #creating the cursor
    cursor = db.cursor()
    print("cursor connected")

    #inserting the continents
    inserting_continents(cursor)

    #closing the database
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()