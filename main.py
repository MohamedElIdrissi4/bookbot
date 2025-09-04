import sys

from stats import get_word_count
from stats import get_char_count
from stats import sort_list

def get_book_text(filepath):
    print(filepath)
    with open(filepath) as f:
        content = f.read()
    return content

def print_list(list):
    for dict in list:
            print(f"{dict["char"]}: {dict["num"]}")

def analyze(filepath):
    text = get_book_text(filepath)
    num = get_word_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
        
    print("----------- Word Count ----------")
    print(f"Found {num} total words")

    print("--------- Character Count -------")
    char_count = get_char_count(text)
    list = sort_list(char_count)
    print_list(list)

def get_filepath(list):
     if len(list) < 2:
          raise Exception("Usage: python3 main.py <path_to_book>")
     elif len(list) == 2:
        analyze(sys.argv[1])

def main():
    try:
        get_filepath(sys.argv)
    except Exception as e:
        print(e)
        sys.exit(1)
         
         

if __name__ == "__main__":
    main()