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

#loading data
def load_data(file):
    with open(file, "r") as f:
        return json.load(f)

#urniversal check
def universal_check(cursor, tabel, column, value):
    #calls the table with the id of the table
    sql = f"select id{tabel} from {tabel} where {column} = %s"
    cursor.execute(sql, (value,))
    item = cursor.fetchone()
    #checks if the item exist, if so it returns true
    if item:
        return item[0]
    return False


#inserting continents
def inserting_continents(cursor, data):
    check =  universal_check(cursor, "Continents", "Continent_name", data["name"])
    if check:
        return check

    #inserting the item if its not in there
    insert_sql = "insert into Continents (Continent_name) values (%s)"
    cursor.execute(insert_sql, (data["name"],))

#inserting the categories
def insert_category(cursor, data):
    check = universal_check(cursor, "Categories", "Catagory_name", data["name"])
    if check:
        return check

    #inserting data
    insert_sql = "insert into Categories (Catagory_name) values (%s)"
    cursor.execute(insert_sql, (data["name"],))

#inserting the language
def insert_language(cursor, data):
    check = universal_check(cursor, "Languages", "Language_name", data["name"])
    if check:
        return check

#main
def main():
    db = connect_to_db()
    print("Connected to your database")

    #place where all the data is being held
    data = {
        "Continent": "json_files/continents.json",
        "Catagory": "json_files/catigory.json"
    }

    #creating the cursor
    cursor = db.cursor()
    print("cursor connected")

    for key, item in data.items():
        print("Using: ", key)

        #going to the right loaction
        match key:
            case "Continent":
                names = load_data(item)
                for name in names:
                    print(name)
                    #inserting the continents
                    inserting_continents(cursor, name)
            case "Catagory":
                names = load_data(item)
                for name in names:
                    print(name)
                    insert_category(cursor, name)

    #closing the database
    print("Finished inserting all data!!!")
    db.commit()
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()