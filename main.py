from stats import wordcount
from stats import charactercount
from stats import countlist
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else: 
    filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)


def main ():
    fulltext = get_book_text(filepath)
    return (fulltext)

def printreport(filepath):
    print("============ BOOKBOT ============") 
    print("Analyzing book found at " + filepath + "...") 
    print("----------- Word Count ----------")
    with open(filepath, 'r') as f:
        fulltext = f.read()
    wordcount(fulltext) 
    print("--------- Character Count -------")
    rawcounts = charactercount(fulltext)
    sortedcounts = countlist(rawcounts)
    for counts in sortedcounts:
        print(str(counts["char"]) + ": " + str(counts["num"]))
    print("============= END ===============")

main()
fulltext = main()
charactercount(fulltext)
fullreport = countlist(charactercount(fulltext))
wordcount(fulltext)
printreport(filepath)
