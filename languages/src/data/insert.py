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

def main():
    print(load_credentials())

if __name__ == '__main__':
    main()