# Task Explanation

The input files must be based on the Inverted Index as mentioned in the other repository of creating inverted index. 
 
At first the Input file is read, and all the terms in the inverted index are then used as key values and their corresponding values are the concatenated string value of the list of files having that term along with the term occurrences for that document, to create the dictionary. Once we have the dictionary, it’s values can be processed to generate the document length, which can again be stored in another dictionary, having Document_ID as keys and the document length as its values. The average document length can be calculated then. 
 
The queries are then read from the file and the query dictionary holds the query number as key and the query as the value.  
 
Using the Unigram dictionary then, all the query terms of the query are analyzed to be present in the dictionary. Using that dictionary, term frequency of that particular query term can be found. Using that dictionary, the total number of documents having that query can also be found out. Thus once we have all the parameters, like ni, fi, dl, avdl and the constants(already provided), we just have to implement the formula for calculating the score. 
 
After the calculation of scores has been done, the query files for each query are generated that hold the Ranking, Document_id (Document Title), and the score corresponding the document. The location where these files will be generated must be changed in the code, while running on the testing machine. 