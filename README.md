# PSET 4: Web Application (Version 2)

### Due Friday April 21 11:59 PM NHT (New Haven Time)

Group members: Sophia Kang (yk575), Phuc Duong (phd24), both enrolled in CPSC 419.

### Contributions
Sophia Kang contribution:
- Writing Jinja statements in luxdetails.html
- Writing HTML for error.html, luxdetails.html
- Creating /search and /obj/<object_id> routes and adding functionality to search database and parse/return the hmtl table to be displayed in index.html.
- Exception handling for no search results, adding 404 handler
- Error Handling: Bad Server, Bad Client, Invalid Search Parameters, Missing "obj_id" and adding the error pages
- Adding CSS Styling to the results in luxdetails.html
- Writing README.md

Phuc Duong contribution:
- Writing HTML for error.html, index.html
- Utilized JQuery to dynamically update the results table based on user's input
- Error Handling: Catching exception for unable to open data base
- Adding CSS Styling to the table results in index.html
- Writing README.md

### A description of help from other people & sources of information from not people
- ULA office hours, Google searches

### Time spent doing assignment
- 3 hours

### Assessment of the assignment
- What we learned: how to use HTML, JavaScript with AJAX and jQuery; styling table elements with CSS, opening a new tab by including target="_blank" in the a href HTML tag
- Suggestions for improvement: None in particular.

### Pylint information to graders
- luxapp.py: We are getting "Access to a protected member _exit of a client class" which is the result of using the os._exit function to exit out of our Flask application if there is a sqlite3 OperationalError with the given database filename. Using sys.exit(1) does not work in this case, so this was an unavoidable pylint error.
- query.py: we have a pylint error that says too many local variables, but we only exceeded the limit by at most 4 and have tried to eliminate local variables without making the code unreadable. There is an error with the number of arguments from LuxDetailsQuery, because we inherit from the Query class, but we think this is negligible for the most part. 
- runserver.py: We get 2 broad-exception-caught errors. However, this is extended behavior as we are trying to exit the program safely we want to try to catch a general exception just in case. We have specific exception already where neccessary.

