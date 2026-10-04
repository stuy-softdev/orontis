# Leon Wong
# Software Development
# September 2026
# COLLABORATORS: Darren Lin, Saxon Rassner

from flask import Flask
app = Flask(__name__)                 #create instance of class Flask

@app.route("/")                       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)                   #where will this go?
    return "No hablo queso!"

app.debug = True
app.run()
