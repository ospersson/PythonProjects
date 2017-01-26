import sys
from Parser import TextToMorseParser

if __name__ == "__main__":
    if len(sys.argv) == 2:
        message = sys.argv[1]
    else:
        message = "Put your text here"

    parser = TextToMorseParser()
    
    parser.parse_word(message)




