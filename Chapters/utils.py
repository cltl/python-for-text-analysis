def count_words(list_of_strings):
    """
    count the words in a list
    
    :param list list_of_strings: a list containing strings
    
    :rtype: dict
    :return: mapping from string to how often the string occurs in the list
    """
    word2freq = dict()
    
    for string in list_of_strings:
        
        if string not in word2freq:
            word2freq[string] = 0
           
        word2freq[string] += 1
    
    return word2freq
           
            
x=1
python = 'awesome'