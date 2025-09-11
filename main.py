from stats import get_num_words, get_char_count, sort_char_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_book_report(book, word_count, char_stats):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for stat in char_stats:
        char = stat['char']
        if(char.isalpha()):
            print(f"{char}: {stat['num']}")
    print("============= END ===============")

def main():
    sys_args = sys.argv
    if(len(sys_args) != 2):
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        book = sys_args[1]
        book_text = get_book_text(book) 
        word_count = get_num_words(book_text)
        char_count = get_char_count(book_text)
        print_book_report(book, word_count, sort_char_count(char_count))
        return 0
    
main()