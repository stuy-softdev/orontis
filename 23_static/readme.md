**Name:** Lucas Ou

**Team:** GOD BLESS AMERICA

**Roster:** Lucas Ou (me), Leon Wong

## DISCOVERIES
**The "Purple Screen of Death":** If we specify `app.debug = True` before we run the Flask App, the page would reload with each new change in the app file. It will also display any code errors on the webpage itself instead of just showing an "Internal Server Error". This is the so-called "Purple Screen of Death".

**static directory:** Going to the `[root route]/static/[file name]` when a file is stored in the static directory under the root directory of your Flask App, you will be able to view that file on the webpage if it is a `.html` file. Plaintext files seem to not display on the webpage, and will instead trigger a dowload of that file onto the user/client's machine.