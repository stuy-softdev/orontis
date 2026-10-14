**Name:** Leon Wong

**Team:** GOD BLESS AMERICA

**Roster:** Lucas Ou, Leon Wong (me)

## DISCOVERIES
**Using Dictionaries in Jinja:** is the same as in python. In the HTML file, you can use `{{ dict['key'] }}` if you pass in the dictionary through `render_template()` in `app.py`.

**Using Jinja Variables as Links in HTML:** This was not completely apparent at first. To insert a link in HTML we can use the `<a href="put link here">put display text here</a>` tags. However, if we want to use a Jinja variable as a link as we have done so in `tablified.html`, you put the variable in quotes in addition to the two curly braces like this: `<a href="{{ Jinja variable here }}">put display text here</a>`. If we ommit the double quotes like this: `<a href={{ Jinja variable here }}>put display text here</a>` it will not work. This is the first time we've played around with using Jinja to as an HTML tag attribute. I'm curious as to how Jinja knows when and when not to interact with its code between the two `{{  }}`. 

## QCC

None for now.