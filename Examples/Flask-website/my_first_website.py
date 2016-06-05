"""
Flask example website.

Run 'python my_first_website.py' and go to http://127.0.0.1:5000/ in your browser
to see a basic text message. Then go to http://127.0.0.1:5000/hello/yourname to see
a custom generated page, generated using a template.
"""


from flask import Flask, render_template

app = Flask(__name__)

# This is what Python will do if you go to http://127.0.0.1:5000/ in your browser.
@app.route('/')
def hello_world():
    """
    This function just returns a page with the words 'Index page.' Pretty boring!
    """
    return "Index page."

# This is what Python will do if you go to http://127.0.0.1:5000/hello in your browser.
@app.route('/hello/')
# But also what Python will do if you go to http://127.0.0.1:5000/hello/Emiel in your browser.
# In that case, the string value 'Emiel' will be assigned to the variable `name`.
@app.route('/hello/<name>')
def hello(name=None):
    """
    This function renders the template 'hello.html', which presents a personalized
    greeting if the name is not None.
    """
    return render_template('hello.html', name=name)

# This enables you to type "python my_first_website.py" in the command line, and
# have a running website at http://127.0.0.1:5000/. Note that the debug mode is
# set to true. Never use debug mode for a website that is exposed to the outside
# world! (I.e. the internet.)
if __name__ == '__main__':
    app.debug = True
    app.run()
