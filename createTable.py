import sqlite3

def connection(db_name):
    mydb = sqlite3.connect(f"{db_name}.db")
    return mydb

def createTable(db_name, table_name):
    mydb = connection(db_name)
    mycursor = mydb.cursor()

    mycursor.execute(f"CREATE TABLE {table_name} (name text, age integer)")
    print(f"Table named '{table_name}' was successfully created!")
    mydb.commit()

    mydb.close()

if __name__ == "__main__":
    createTable("exemple", "people")
