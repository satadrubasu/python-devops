"""
 Module level docstring()


"""
import sys
from urllib.request import urlopen


## URL to use for runnin ghe example : 'https://raw.githubusercontent.com/satadrubasu/Unix-PythonReference/master/resources/sample.txt'
def fetch_words(url):
    """ Fetchs list of words , read from a passed URL.
        Args:
            url: The URL of a UTF-8 text Document

        Returns:
            List of strings containing the words from the document.
    """
    mystory = urlopen(url)
    story_words = []
    for theline in mystory:
        the_line_words = theline.decode('utf-8').split()
        for theword in the_line_words:
            story_words.append(theword)
    mystory.close()
    return(story_words)


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    ## run this program with sample.py https://raw.githubusercontent.com/satadrubasu/Unix-PythonReference/master/resources/sample.txt
    ## From SHELL : python sample.py
    ## From REPL : import sample
    ## From REPL : main('https://raw.githubusercontent.com/satadrubasu/Unix-PythonReference/master/resources/sample.txt')
    main(sys.argv[1])

