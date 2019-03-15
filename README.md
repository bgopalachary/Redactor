Bhavana Gopalachary
Bhavana.Gopalachary-1@ou.edu
Project1: Redactor

In this project the main aim was to read data from multiple text files present in the directory as well as another directory named otherfiles. After reading the data our main job is to redact i.e black out all the data corresponding to the input tags. They are --names,--dates,--phone,--address,--genders along with another tag named --concept that gives us just a word whose context we have to redact.All this data is considered to be sensitive data and hence the redaction is needed.After the redaction is done,all the redacted text data is put in a new output file. Different kinds of statistics are also found from the redacted text.

Function 1:
In the first function, we read the data from different files using the f.read() command as we use a for loop to read each and every file. All the read data is returned and passed in to the next function.

Function 2:
In the next function we take the extracted data and by using regular expressions we try to find the dates. Once the dates are found by using the re.sub we replace the dates with █ in the original text. This replaced text is returned and passed in to the next function.

Function 3:
In this function, by unsing the same regular expressions concept and re.sub we replace all the phone numbers with the same character █. Again the redacted original text is returned and passed in to the next function.

Function :
In this function the addresses are found by using the Pyap package and replaced using the replace() function.

Function 4:
In this function,we have to replace all the names in the data. This is done by using nltk and its packages. We do chunking on the data and by using the chunk_lable() we find the label for each word . If the label is == PERSON , then the word corresponding to the label is replaced using the replace() function.This replaced data is returned and passed to the next function.

Function 5:
In this function, our aim is to replace the gender related words such as him,her,she etc. I took a list named genders and placed all possible gender related words . Then i'm taking each word from the text and checking if it is there in genders. If yes then that word is replaced . Again the new data is returned and passed to the next function.

Function 6:
In this function, we have to replace sentences in which words similar to the given context word are present.For this we use wordnet. I first found the synonymns of the context word and checked for this word in the text.If it is present, the whole sentence was replaced using a for loop, replace function and sent_tokenizing. The replaced text was returned.

Function 7:
In this function, all the redacted data is passed in to a newly created created directory which will contain all the output files.

Function 8:
By using count and len() different stats regarding the redacted data such as number of redactions per tag are recorded and printed here.

Assumptions:

In the Function 4, some names ae being redated and some are not and some extra names that have a capital also return redacted.
In Function 2, dates are redacted only for three format types, the same is with phone numbers.

Refrences:
https://stackabuse.com/python-check-if-a-file-or-directory-exists/
https://www.w3schools.com/python/python_regex.asp
https://www.geeksforgeeks.org/python-stemming-words-with-nltk/
https://www.guru99.com/reading-and-writing-files-in-python.html
https://pypi.org/project/pyap/
https://kite.com/python/docs/nltk.Tree.leaf_treeposition
https://streamhacker.com/2009/02/23/chunk-extraction-with-nltk/


Command to run the project1:
pipenv run python project1/redactor.py --input '*.txt' \--inpu
t 'otherfiles/*.txt' \--names --dates --addresses --phones \--concept 'kids' \--output 'files/' \--stats stderr

Command to run the test cases:
pipenv run python -m pytest
