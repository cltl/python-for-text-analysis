"""
Example website in Flask, with web forms.

This is a fully working example showing how to use web forms on a Flask-based website.
I've found this basic structure very useful in setting up annotation tools or demos.
"""

# Flask-related imports:
from flask import Flask, request, render_template

# Other imports go here:
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize


################################################################################
# Set up general functions

def type_token_ratio(text):
    "Computes the type-token ratio and returns a dictionary with the results."
    c = Counter()
    for sentence in sent_tokenize(text.lower()):
        c.update([word for word in word_tokenize(sentence) if len(word) > 1])
    num_tokens = sum(c.values())
    num_types = len(c)
    return {'Types': num_types,
            'Tokens': num_tokens,
            'Ratio': float(num_types)/num_tokens}

################################################################################
# Load data



################################################################################
# Set up app:
app = Flask(__name__)

################################################################################
# Webpage-related functions

@app.route('/', methods=['GET'])
def main_page():
    """
    Function to display the main page. This is the first thing you see when you
    load the website.
    """
    return render_template('index.html')


@app.route('/type-token-ratio/', methods=['GET'])
def type_token_ratio_form():
    """
    Display webpage with a form.
    """
    return render_template('ttr.html')


@app.route('/type-token-results/', methods=['POST'])
def type_token_results():
    """
    Show the page with submitted information.
    """
    text = request.form['textfield']
    ttr_dict = type_token_ratio(text)
    return render_template('results.html', ttr_data= ttr_dict)

################################################################################
# Running the website

if __name__ == '__main__':
    app.debug = True
    app.run()
