import sys
from stats import book_text_amount
from stats import character_count
from stats import sorted_list

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
		return file_contents

def main():
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    word_count = book_text_amount(text)
    letter_count = character_count(text)
    char_list = sorted_list(letter_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in char_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
