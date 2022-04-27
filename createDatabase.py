import sqlite3

def create(db_name):
    mydb = sqlite3.connect(f"{db_name}.db")
    print(f"Database named '{db_name}' was successfully created!")

    mydb.close()

if __name__ == "__main__":
    create("exemple")
