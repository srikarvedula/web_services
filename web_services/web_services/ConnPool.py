import mysql.connector


from mysql.connector import errors
import time
db = mysql.connector.connect(user='root',
                                 password='Dirtydula1$',
                                 host='127.0.0.1',
                                 database='data_gen',
                                 pool_name='DBGenConnPool',
                                 pool_size=10)

db2 = mysql.connector.connect(pool_name='DBGenConnPool')
db3 = mysql.connector.connect(pool_name='DBGenConnPool')
db4 = mysql.connector.connect(pool_name='DBGenConnPool')
db5 = mysql.connector.connect(pool_name='DBGenConnPool')