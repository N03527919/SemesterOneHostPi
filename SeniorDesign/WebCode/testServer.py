#!/usr/bin/python

import os
import sqlite3 as mydb
import sys

from socket import *
serverPort = 12001
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
msg = ''

while True:
  con = mydb.connect('/home/pi/SeniorDesign/WebCode/test.db')
  with con:
    try:
      cur = con.cursor()
      #cur.execute('insert into TempData values(?,?)',(msg,msg))
      sql = ''' UPDATE TempData
                SET data1 = ?,
                    data2 = ?
                WHERE id = ?'''
      cur.execute(sql, (msg,msg,1))
      print('Data Logged!')
    except:
      print('Error')
  message, clientAddress = serverSocket.recvfrom(2048)
  print(clientAddress)
  msg = message.decode().upper()
  print(msg)
  serverSocket.sendto(msg.encode(), clientAddress)

  con.close()
