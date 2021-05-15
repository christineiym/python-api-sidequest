"""Running website as package.

To run the website after installing requirements: 
1. export FLASK_APP=draft_product.unc_abbreviations
  - Alternatively, do the following: 
    1) cd draft_product (cd stands for change directory, so this navigates you to the appropriate folder)
    2) export FLASK_APP=unc_abbreviations
2. python -m flask run
3. Click the link!
"""


import os
from flask import Flask
from flask import render_template
import cgi, cgitb  # more info on CGI: https://www.tutorialspoint.com/python/python_cgi_programming.htm


def create_app(test_config=None):
    """Create and configure the app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # A local database shouldn't be needed, but just in case...
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that serves as the homepage
    # @app.route tells Flask the URL that should trigger a call to our function!
    # TODO: explain GET/POST
    @app.route('/', methods=['POST'])
    def home():
        """Utilize the form data to consult the dictionary and return an appropriate result."""
        
        # Get data from fields.
        form = cgi.FieldStorage() 
        first_name = form.getvalue('first_name')
        last_name  = form.getvalue('last_name')

        # TODO: Explain the HTML code below. Is there a better way to do this?
        print("Content-type:text/html\r\n\r\n")
        print("<html>")
        print("<head>")
        print("<title>Hello - Second CGI Program</title>")
        print("</head>")
        print("<body>")
        print("<h2>Hello %s %s</h2>" % (first_name, last_name))
        print("</body>")
        print("</html>")

        result = ""
        return render_template('home.html',result=result)
    
    @app.route('/index')  
    def index():
        """Placeholder function for a potential future use."""
        # TODO: (Christine) Structure this file better...
        return "Hi! This is a work in progress."

    return app