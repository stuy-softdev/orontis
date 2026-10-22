**Name:** Lucas Ou

**Team:** GOD BLESS AMERICA

**Roster:** Lucas Ou (me), Leon Wong

**PLAN**
* Map out Flowchart (as shown below)
* Create HTML for each page
* Write a Python function for each page
* Going down the flow chart, connect each page together editing the HTML and Python
* Add the cookies check in the beginning

**LOGIN FLOWCHART**
```mermaid
flowchart TD
    A[Home Pg] -->|User wants to check profile| B{Logged In?}
    B -->|Yes| C[Display User Profile / Response]
    C -->|User wants to logout| A
    B -->|No| D{Login or Create Account?}
    D -->|Login| E[Ask for Username and Password]
    E --> F{Username Password Correct?}
    F -->|Yes| C
    F -->|No| D
    D -->|Create Account| G[Ask for new Username and Password]
    G --> H{Username and Password Valid?}
    H -->|Yes| I[Show Account Created Successfully, ask to login]
    I --> D
    H -->|No| G
```

**DISCO:**
* **Notes In Class:** 
    ```
    session[KEY] = value
    session.pop(key)
    ```
* **Something** 
    text
-----------------------------------------------------------------------


**Q/C/C:**
* None for now
-----------------------------------------------------------------------


**OTHER?**
* []()
*
-----------------------------------------------------------------------