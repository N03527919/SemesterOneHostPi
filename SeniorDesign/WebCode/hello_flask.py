#!/usr/bin/python

from flask import Flask, render_template, g
import datetime
import sqlite3 as mydb
DATABASE = '/home/pi/SeniorDesign/WebCode/test.db'

app = Flask(__name__)

@app.route('/')
def hello():
  #now = datetime.datetime.now()
  #timeString = now.strftime("%Y-%m-%d %H:%M")
  #templateData = {
  #  'title' : 'HELLO!',
  #  'time' : timeString
  #}
  cur = get_db().cursor()
  cur.execute("select * from TempData")
  records = cur.fetchall()
  info1 = []
  info2 = []
  for record in records:
    info1.append(record[0])
    info2.append(record[1])
  info = info2[0]
  templateData = {
    'data' : info
  }
  #return render_template('top.html',**templateData)
  return render_template('top1.html',**templateData)

def get_db():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = mydb.connect(DATABASE)
  return db

if __name__ == "__main__":
  app.run(host='0.0.0.0', port = 8081, debug = True)
