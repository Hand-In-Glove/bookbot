def number_of_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    characters = {}
    for char in text:
        if char not in characters:
            characters[char] = 0
        characters[char] += 1
    return characters

def sort_on_count(items):
    return items["count"]

def sorted_character_count(character_count):
    list_of_counts = []

    for char, count in character_count.items():
        list_of_counts.append({'char': char, 'count': count})

    print(list_of_counts)
    return sorted(list_of_counts, key=sort_on_count, reverse=True)
