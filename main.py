import sys
from stats import number_of_words, count_characters, sorted_character_count

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = number_of_words(book_text)
    count_dict = count_characters(book_text)
    char_count = sorted_character_count(count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words.")
    print("-------- Character Count -------")
    for item in char_count:
        if item['char'].isalpha():
          print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()