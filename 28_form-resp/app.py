# Leon Wong
# GOD BLESS AMERICA
# Roster: Lucas Ou, Leon Wong (me)
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
    return render_template( 'login.html' )


@app.route( "/auth", methods=['GET', 'POST'] )
def authenticate():
    if request.method == "POST":
        return render_template( 'response.html', name=request.form.get('username'), req=request.method)
    elif request.method == "GET":
        return render_template( 'response.html', name=request.args.get('username'), req=request.method)
    else:
        return render_template( 'response.html', name="Anon", req="neither a GET nor a POST")


if __name__ == "__main__": #false if this file imported as module
    app.debug = True  #enable PSOD, auto-server-restart on code chg
    app.run()