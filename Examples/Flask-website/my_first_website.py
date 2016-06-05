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
import csv

################################################################################
# Load data

with open('./static/data/Concreteness_ratings_Brysbaert_et_al_BRM.txt') as f:
    reader = csv.DictReader(f, delimiter='\t')
    concreteness_values = {entry['Word']: float(entry['Conc.M']) for entry in reader}

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

def average_concreteness(text):
    """
    Measures the average concreteness of a text by taking the average concreteness
    of the word forms. Probably not a very good idea!
    """
    words = [word for sentence in sent_tokenize(text.lower())
                  for word in word_tokenize(sentence)
                  if word in concreteness_values]
    value = sum(concreteness_values[w] for w in words)/float(len(words))
    return {'concreteness': value,
            'words': set(words)}
    

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
    return render_template('ttr-results.html', ttr_data= ttr_dict)


@app.route('/concreteness/', methods=['GET'])
def concreteness_form():
    """
    Display webpage with a form.
    """
    return render_template('concreteness.html')


@app.route('/concreteness-results/', methods=['POST'])
def concreteness_results():
    """
    Show the page with submitted information.
    """
    text = request.form['textfield']
    results = average_concreteness(text)
    return render_template('concreteness-results.html', concreteness_data= results)

################################################################################
# Running the website

if __name__ == '__main__':
    app.debug = True
    app.run()
