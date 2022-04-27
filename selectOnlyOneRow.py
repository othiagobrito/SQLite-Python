import sqlite3

def connection(db_name):
    mydb = sqlite3.connect(f"{db_name}.db")
    return mydb

def insertData(db_name, table_name, name):
    mydb = connection(db_name)
    mycursor = mydb.cursor()

    for row in mycursor.execute(f"SELECT * FROM {table_name} WHERE name='{name}'"):
        print(f"Name: {row[0]}\nAge: {row[1]}")
        
    mydb.close()

if __name__ == "__main__":
    insertData("exemple", "people", "Thiago")
