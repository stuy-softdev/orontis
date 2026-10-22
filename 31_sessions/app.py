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
from flask import session
from flask import redirect
from flask import url_for
import csv

#the conventional way:
#from flask import Flask, render_template, request

USERS_FILE_PATH = "data/users.csv"

def get_users(filepath):
    """Gets the lists of users who have created an account.

    Args:
        filepath: The name of the CSV file that contains all the user info.

    Returns:
        A list of dictionaries each with keys 'Username' and 'Password' for each user.
    """

    li = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            li.append(row)
    return li

def add_user(filepath, username, password):
    """Adds a user to the users CSV file
    
    Args:
        filepath: The path of the CSV file that contains all the user info.
        username: New user's username
        password: New user's password
    """

    # Append 'a' writing mode to the file
    with open(filepath, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username, password])

def username_is_available(username, users):
    """Checks whether or not a username is available in a users list.
    
    Args:
        username: The new username user wants to use
        users: List of dictionaries that represent each user

    Returns:
        True if username is available, False if it username is not available
    """

    # For each user in the global list
    for user in users:
        if username == user["Username"]:
            return False
    return True

def user_pass_is_valid(username, password, users):
    """Checks whether or not a username and password pair is valid in the users list.
        
    Args:
        username: The username the user entered
        password: The password the user entered
        users: List of dictionaries that represent each user
    
    Returns:
        True if username is available, False if it username is not available
    """
    
    # For each user in the global list
    for user in users:
        if username == user["Username"] and password == user["Password"]:
            return True
    return False

app = Flask(__name__)    #create Flask object

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' # Taken from Flask documentation

@app.route( "/", methods=['GET', 'POST'] )
def disp_homepage():
    if 'username' in session:
        return render_template( 'response.html', name=session["username"] )
    return render_template( 'home.html' )

@app.route( "/create-account", methods=['GET', 'POST'] )
def disp_account_creation():
    users = get_users(USERS_FILE_PATH)
    # prevPass and prevUser to make it so that the user doesn't have to retype their user/pass if it's wrong
    # If the user hasn't entered a new username or password yet...
    if (request.form.get('new username') is None) or (request.form.get('new password') is None):
        # Ask them to do so
        return render_template( 'create-account.html', invalidUser=True, invalidPass=True, prevUser="", prevPass="")
    elif not username_is_available(request.form.get('new username'), users):
        # If the username is already taken, say so on the page
        return render_template( 'create-account.html', invalidUser=True, invalidPass=False, prevUser=request.form.get('new username'), prevPass=request.form.get('new password'))
    elif len(request.form.get('new password')) < 8:
        # If the password is too small, say so on the page
        return render_template( 'create-account.html', invalidUser=False, invalidPass=True, prevUser=request.form.get('new username'), prevPass=request.form.get('new password'))
    else:
        # If everything looks good, add data to CSV
        add_user(USERS_FILE_PATH, request.form.get('new username'), request.form.get('new password'))
        # Tell them to go to login page in HTML file
        # Render account-sucess.html to prevent user to reenter their user and pass, which will create duplicate accounts
        return render_template( 'account-sucess.html', invalidUser=False, invalidPass=False, prevUser="", prevPass="")

@app.route( "/login", methods=['GET', 'POST'] )
def disp_loginpage():
    users = get_users(USERS_FILE_PATH)
    if user_pass_is_valid(request.form.get('username'), request.form.get('password'), users):
        session['username'] = request.form['username']
        return redirect(url_for('disp_homepage'))
    else:
        return render_template( 'login.html', invalidUserPass=True)

@app.route( "/logout", methods=['GET', 'POST'] )
def logout():
    session.pop('username')
    return render_template( 'logout.html', name=request.form.get('username'), req=request.method)


if __name__ == "__main__": #false if this file imported as module
    app.debug = True  #enable PSOD, auto-server-restart on code chg
    app.run()
