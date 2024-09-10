"""
Import the text_utils module you created and calculate the average number of
words per line in a given text file. The text file that will be used to test
this is the text file called "sample.txt" (located in the same directory as
this exercise). The average number of words per line should be rounded down to
the nearest integer.

Print the average number of words per line in the text file in the following
format:

"Average words per line: [average]"
"""

def average():
    import math  #import math funcitons
    import text_utils  # import my functions to use for this function

    #F for file      L for lines 
    F = open("sample.txt", 'r') #opens file.txt to be read
    L = F.readlines() 
    t = len(L) #t = lines count
    L = "".join(L)  # joins line together to be read by count words if not wont work right
      
    a = text_utils.count_words(L)   # counts word in file
    e = math.floor(a/t)    # divides and rounds down to get average lines per line

    F.close #closes file 
    return print(f"Average words per line: {e}")

average()