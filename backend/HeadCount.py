import mysql.connector
import pytest
import unittest

mydb = mysql.connector.connect(user='root', password='huawei123', host='127.0.0.1', database='pythonDB')
# mydb = mysql.connector.connect(user='chen', password='chen123', host='localhost', database='pythonDB')
cursor = mydb.cursor()
# cursor.execute("CREATE TABLE points (XCoordinate INT(5), YCoordinate INT(5))")


def insert_coordinate(x, y):
    sql = "INSERT INTO points(XCoordinate, YCoordinate) " \
          "VALUES(%s,%s)"
    val = (x, y)
    cursor.execute(sql, val)
    mydb.commit()


def clear_table():
    sql = "TRUNCATE TABLE points"
    cursor.execute(sql)
    mydb.commit()

def get_number_of_heads():

    return cursor.rowcount


class TestDir(unittest.TestCase):

    def test_coordinate(self):

        assert 1 >= 0



if __name__ == "__main__":
    #x = 0
    #y = 0
    #insert_coordinate(x, y)
    #clear_table()
    print("ok")
