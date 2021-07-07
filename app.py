from os import stat
from flask import Flask, render_template, request, redirect, url_for, flash, Request
import textwrap
import pyodbc
import time

app = Flask(__name__)
app.secret_key="ABCDEF"



server = 'mysqlserveradb.database.windows.net'
database = 'archana'
username = 'archanat'
password = 'Dheeraj92'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};PORT=1433;SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


@app.route('/', methods=["POST","GET"])
def start():
    return render_template('index.html',part1=1)

@app.route('/displayname', methods=["POST","GET"])
def q1():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};PORT=1433;SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    p2name = request.form.get("p2name")
    redstone = request.form.get("redstone")
    greenstone = request.form.get("greenstone")
    cursor.execute("INSERT INTO [dbo].[quiz6] (player, redstones, greenstones) VALUES ('"+p2name+"', "+redstone+", "+greenstone+") ")
    cursor.commit()
    return render_template('p2home.html', p2name=p2name, redstone=redstone, greenstone=greenstone)


@app.route('/playgame', methods=["POST","GET"])
def five():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};PORT=1433;SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    color = request.form.get("color")
    p1name = request.form.get("p1name")
    if (color == 'r'):
        color = 'redstones'
    else:
        color = 'greenstones'
    howmany = request.form.get("howmany")
    if int(howmany) > 2:
        print("Please enter a value less than or equal to 2 and refresh page")
    elif int(howmany) < 1:
        print("Please enter either 1 or 2 refreshpage")    
    cursor.execute("UPDATE [dbo].[quiz6]  SET [dbo].[quiz6].["+color+"] = "+howmany+" WHERE [dbo].[quiz6].[player] = '"+p1name+"'  ")
    cursor.commit()
    return render_template('p2home.html',p1name=p1name,redstone=redstone,greenstone=greenstone)

if __name__ == '__main__':
    
  app.run(host='127.0.0.1', port=8081, debug=True)
  app.config['JSON_SORT_KEYS']=False