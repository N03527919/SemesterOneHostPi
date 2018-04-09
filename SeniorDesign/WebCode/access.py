#!/usr/bin/python

import sqlite3 as mydb

def getInfo():
  con = mydb.connect('/home/pi/SeniorDesign/WebCode/test.db')
  with con:
    try:
      cur = con.cursor()
      cur.execute("select * from TempData")
      output = cur.fetchall()
      print output
    except:
      print "Error!"

