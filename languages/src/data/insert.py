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

def main():
    db = connect_to_db()
    print("Connected to your database")

if __name__ == '__main__':
    main()