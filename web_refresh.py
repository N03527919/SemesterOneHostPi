#!/usr/bin/python

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")

def hello():
  return render_template('js2.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port = 8081, debug = True)

