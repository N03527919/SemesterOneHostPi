#!/usr/bin/python

import os
import sqlite3 as mydb
import sys

def testFunc():

  con = mydb.connect('/home/pi/SeniorDesign/WebCode/test.db')
  with con:
    try:
      msg = 'hello'
      print(msg)
      cur = con.cursor()
      #print(msg)
      cur.execute('insert into TempData values(?,?)',(msg,msg))
      print("Logged")
    except:
      print("Error")
   
  con.close()

testFunc()
