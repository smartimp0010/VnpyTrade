import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.0.5;DATABASE=msdb;UID=sa;PWD=9685')
cursor = cnxn.cursor()

cursor.execute("select * from TXFTickData")
row = cursor.fetchone()

if row:
    print row