"""
Example to show how doctests work.
Use 'python -m doctest -v doctest-example.py' to see the results.
"""

def hello(name):
    """
    Function that returns a greeting for whatever name you enter.
    
    Usage:
    >>> hello('Emiel')
    'Hello, Emiel!'
    """
    return ''.join(["Hello, ", name, '!'])
