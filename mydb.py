# Install mysql on your connector
# pip install pymysql
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "goodluck",
    auth_plugin="mysql_native_password"
    
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE db_dcrm")

print("All Done!")