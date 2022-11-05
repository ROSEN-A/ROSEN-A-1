import mysql.connector
# Run this code only after you've finished the setups
# listed in the README.md
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="rosendb"
)

cur = mydb.cursor()
print("Test #1: Test if the database 'rosendb' exists")
## print all databases
cur.execute("SHOW DATABASES")
for x in cur:
    print(x)
    # output should be
    # ('information_schema',)
    # ('mysql',)
    # ('performance_schema',)
    # ('rosendb',)
    # ('sys',)
print("\n")
print("Test #2: Test if the table 'image' exists ")
cur.execute("SHOW TABLES")
for x in cur:
    print(x)
    # output should be
    # ('image',)
print("\n")
print("Test #3: Test if records can be inserted into 'image'")
rows_affected = 0
for i in range(0, 4):
    query = "INSERT INTO image (dir, name) VALUES (%s, %s)"
    val = ("Users/mp/Desktop", "image"+str(i))
    cur.execute(query, val)
    mydb.commit()
    rows_affected+= cur.rowcount
print("Insertion finished.", rows_affected, "rows were affected.")
# output should be "Insertion finished. 4 rows were affected."
print("\n")