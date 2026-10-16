**Name:** Leon Wong

**Team:** GOD BLESS AMERICA

**Roster:** Leon Wong (me), Lucas Ou

DISCO:
* **`.pyc` Files:**
These files are often generated and stored in a `__pychche__` directory and are compiled Python scrpits. (A parallel to how compiled `.java` files are `.class`). `.pyc` files most often appear when we have a "home-rolled" python module, where the module is compiled and placed into `__pychche__`.
* **WHAT TO KNOW about GET/POST + request.args/request.headers:**
   request.args: Returns a multidictionary, or a set of dictionaries, containing the arguments of the form. When we input text into the login, that text is returned as a value for the `username` key. Brackets can be used to achieve a sub-dictionary of a specific key. For instance, `request.args['username']`, which returns the dictionary of the username key and the inputted text value.
    
   However, `request.args['username']` is one of the lines that caused an error with the website because when the login page is being displayed, the multidictionary starts off empty, so a `'username'` index doesn't exist yet and it's referred to as a "bad request."
   
   GET is the default method for route. GET retrieves the data using the url: Whatever comes after "?" goes into request.args. If GET is not an allowed method, the website breaks.
   
   When routing the app, `methods` must contain the one given in the request, as indicated by the brackets. The default is `'GET'`, so writing `methods=['GET']` is equivalent to the regular app.route(). However, writing `methods=['POST']` causes an error. However, `methods=['GET', 'POST']` does work normally since it contains `'GET'`.
   
   POST seems to not relate to the URL. When doing method="post" in <form>, the data is no longer shown in the url.
   request.headers is metadata which is not present in the url. This seems to work regardless of whether the POST method is allowed.
* **HOW TO SEE testmod0 output:**
   your team's clearest explanation of how to elicit each of the
   3 possible outputs from your "home-rolled" python module
   1. One can call print(testmod0.goo()) in the app
   2. One can just import testmod0 to trigger the second message
   3. One must run testmod0.py directly in order to trigger the third message(+ second message)

-----------------------------------------------------------------------


Q/C/C:
* What significance does request.headers have?
* What is the difference between `methods=['GET']` and `methods=['POST']`? Does `methods=['POST']` serve a particular purpose, and on what instances does `'POST'` work?
* POST is still very elusive, abstruse, enigmatic, and perplexing.
-----------------------------------------------------------------------


OTHER?
* https://flask.palletsprojects.com/en/stable/quickstart/#http-methods
* https://www.w3schools.com/tags/ref_httpmethods.asp
*
-----------------------------------------------------------------------


