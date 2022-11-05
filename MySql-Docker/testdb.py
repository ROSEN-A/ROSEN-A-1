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