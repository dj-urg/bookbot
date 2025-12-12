from stats import get_num_words, chars_dict_to_sorted_list, get_num_characters
import sys

print(sys.argv)

def get_book_text(book_name):
    with open(f"{book_name}", "r") as f:
        return f.read()
    
def main():
    if len(sys.argv) == 2:
        text = get_book_text(sys.argv[1])
    else:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # use stats helpers
    word_count = get_num_words(text)
    chars_dict = get_num_characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    # print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in chars_sorted_list:
        char = item["char"]
        count = item["num"]
        if not char.isalpha():
            continue
        print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()