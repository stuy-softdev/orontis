# Leon Wong
# NameTeam: Darren Lin, Ivan Zheng, Leon Wong
# SoftDev
# K27 -- Who Do Forms Work For?
# 2026-10-14w
# time spent: 1.4

# CONVENTIONS FOR IMPORTS:
# list most general first (ie standard python library, no pip install req'd)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (eg today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

import testmod0                     #"home-rolled" module for basic exploration

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
 * Some will work as written;
 *  ...other sections will NOT.

TASK: Predict which .
 1. Devise simple tests to isolate components/behaviors.
 2. Execute your tests.
 3. Process results.
 4. Findings yield new ideas for more tests? Yes: do them.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''


#USAGE: Uncomment one version of the decorator at a time

# @app.route("/") # commenting all 4 out of these causes an error 404
# @app.route( "/", methods=['GET'] ) # GET is the default parameter
# @app.route( "/", methods=['POST'] ) # COMPLETELY BREAKS THE WEBSITE. ERROR 405 METHOD NOT ALLOWED. NEED GET
@app.route( "/", methods=['GET', 'POST'] )
def disp_loginpage():
#     print("\n\n\n")
#     print("***DIAG: this Flask obj ***")
#     print(app)
#     print("***DIAG: request obj ***")
#     print(request)
#     print("***DIAG: request.args ***")
#     print(request.args)
#     print("***DIAG: request.args['username']  ***")
#     print(request.args['username']) #Causes PSOD if there is no username arg
    print("***DIAG: request.headers ***")
    print(request.headers)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # YOUR CODE HERE
    # ...for experimenting with
    # home-rolled module importation
    print(testmod0.goo())
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'login.html' )



#USAGE: Uncomment one version of the decorator at a time

#@app.route("/auth")
#@app.route( "/auth", methods=['GET'] )
#@app.route( "/auth", methods=['POST'] ) #The whole webs
@app.route( "/auth", methods=['GET', 'POST'] )
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # YOUR CODE HERE
    # ...for experimenting with
    # home-rolled module importation
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return request.args['username']

    
if __name__ == "__main__": #false if this file imported as module
    app.debug = True  #enable PSOD, auto-server-restart on code chg
    app.run()


'''
~~~
    the BEEG REWARD
        ...for reading all the way to "The Waybottom."
                                                       ~~~

The Question du Jour is

How do GET & POST requests 
relate to 
request.args and request.headers?

...and the best way to engage with this Q 
is to selectively uncomment targeted regions above,
making a prediction before each successive re-run/re-load, 
and making sense of observations.

(after you have made some sense of things, document this in readme)

'''
