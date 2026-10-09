# Leon Wong
# Team: GOD BLESS AMERICA
# Roster: Lucas Ou, Leon Wong
# Software Development
# Sep 2026

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Q0:
The template html (in this case, model_tmplt.html) would not load.
Prediction Correct!

Q1:
localhost:5000/my_foist_template
Prediction Correct!

Q2:
It substitutes each parameter into the html template. So, "fooooo" replaces foo, and the list called coll is subsituted into collection in the html file.
Prediction Correct!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q0: What will happen if you remove
#     render_template from the following statement?
#     Log prediction BEFORE commenting out and reloading...
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Q1: What URL shall you use to load this page?
#     ( Self-assess: Can all of your teammates confidently predict? )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/my_foist_template") 
def test_tmplt():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Q2: What is the significance of each parameter?
    #     ( Simplest, most concise answer best. )
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)


if __name__ == "__main__":
    app.debug = True
    app.run()
