# Leon Wong
# Software Development
# September 2026
# COLLABORATORS: Darren Lin, Saxon Rassner
# TEAMNAME: We are the best best best best at Python and Software Development

'''
ERRORS:
<If running this code yielded errors, reproduce them verbatim here.
 ....and if you care to, speculate as to reasons and/or solutions.>
'''


from flask import Flask

app = Flask(__name__)         # Q0: Where have you seen similar syntax in other langs?
                              # It looks like a constructor from Java.
                              
@app.route("/")               # Q1: What points of reference do you have for meaning of '/'?
                              # / is used for paths in the terminal.
def hello_world():
    print(__name__)           # Q2: Where will this print to? Q3: What will it print?
                              # It will print to the terminal. It will print __main__ because it is being ran directly
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?
                              # This might be shown in the website based on an educated guess since I do not know where else it could be shown.
app.run()                     # Q5: Where have you seen similar constructs in other languages?
                              # This is like object oriented programming in Java