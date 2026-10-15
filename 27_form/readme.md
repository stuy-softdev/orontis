  Leon Wong
  NameTeam: Darren Lin, Ivan Zheng, Leon Wong
  SoftDev
  K27 -- Who Do Forms Work For?
  2026-10-14w
  time spent: 1.4

DISCO:
* method parameter sets which request method is allowed
* You can just put your own arguments in the url(after "?") and it works perfectly
* 
* WHAT TO KNOW about GET/POST + request.args/request.headers:
  {
   your team's clearest breakdown on which goes with which,
   which "breaks" the other,
   when error handling may be a good idea,
   etc.
   GET is the default method for route. GET retrieves the data using the url: Whatever comes after "?" -> request.args If GET is not an allowed method, the website breaks.
   POST seems to not relate to the URL. When doing method="post" in <form>, the data is no longer shown in the url.
   request.headers is metadata which is not present in the url. This seems to work regardless of whether the POST method is allowed.
  }
* HOW TO SEE testmod0 output:
  {
   your team's clearest explanation of how to elicit each of the
   3 possible outputs from your "home-rolled" python module
   One can call print(testmod0.goo()) in the app
   One can just import testmod0 to trigger the second message
   One must run testmod0.py directly in order to trigger the third message(+ second message)
  }

-----------------------------------------------------------------------


Q/C/C:
* POST is still very elusive, abstruse, enigmatic, and perplexing.
* 
* 
-----------------------------------------------------------------------


OTHER?
* 
* 
* 
-----------------------------------------------------------------------







