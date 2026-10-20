# Lucas Ou
# GOD BLESS AMERICA
# Roster: Lucas Ou (me), Leon Wong
# Software Development
# October 2026

# CONVENTIONS FOR IMPORTS:
# list most general first (ie standard python library, no pip install req'd)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (eg today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

@app.route( "/", methods=['GET', 'POST'] )
def disp_loginpage():
    return render_template( 'index.html', style="../static/style.css")

@app.route( "/decolores")
def decolores():
    return render_template( 'index.html', style="../static/decolores.css")

if __name__ == "__main__": #false if this file imported as module
    app.debug = True  #enable PSOD, auto-server-restart on code chg
    app.run()
