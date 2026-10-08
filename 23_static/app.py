# Lucas Ou
# Software Development
# Sep 2026

# DEMO
# basics of /static folder
from flask import Flask
app = Flask(__name__)

@app.route("/")             # bind the root route to this function. Ie serve this function's return value when the root route is requested.
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    # UNCOMMENT NEXT LINE TO SEE PSOD
    # 10/0 # ZeroDivisionError
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported 
    app.debug = True        # enable auto-restart of web server upon code change
    # Will also be able to display any errors from the code on the website page instead of displaying as "Internal Server Error"
    app.run()

