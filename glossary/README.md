## Glossary
In Glossary I learned how to do a basic search in a dictionary with regex and python

``import re`` is the package for regex in Python 

``re.match(r"^"+search_word+"\w+", word)`` will match every word that begins with the inputted pattern. 
It will search the pattern at the beginning of each word and take the rest of the letter. 
For example, if I type "mu" as a seach, I will have "music".

``words_found.append(result.group(0))`` the printed output of re.match is ugly. So in order to take only the matched words, you need to make a result.match as result is a "Match Object". 

``dict(sorted(glossary_file.items()))`` is to sort a dictionary. `glossary_file` is dictionary, so I can perform a `items()` that provide a sort of list of tuples. So `sorted()` sort this list of tuples and output a list object, so I need to convert that to have a dictionary at the end