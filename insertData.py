import sqlite3

def connection(db_name):
    mydb = sqlite3.connect(f"{db_name}.db")
    return mydb

def insertData(db_name, table_name, name, age):
    mydb = connection(db_name)
    mycursor = mydb.cursor()

    mycursor.execute(f"INSERT INTO {table_name} VALUES ('{name}', {age})")
    print(f"{name} was successfully into {table_name}'s table!")
    mydb.commit()

    mydb.close()

if __name__ == "__main__":
    insertData("exemple", "people", "Thiago", 24)
    insertData("exemple", "people", "Pedro", 30)
    insertData("exemple", "people", "Joana", 27)
