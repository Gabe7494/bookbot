def book_text_amount(main):
        return len(main.split())

def character_count(file_contents):
	characters = file_contents.lower()
	new_characters = {}

	for c in characters:
		if c not in new_characters:
			new_characters[c] = 1
		else:
			new_characters[c] += 1
	return new_characters

def sorted_list(letter_count):
    # build up the_list here
    the_list = []
    for letter, count in letter_count.items():
        the_list.append({"char": letter, "num": count})

    # sort the_list here
    def sort_on(item):
        return item["num"]
    the_list.sort(reverse=True, key=sort_on)

    # return the sorted list
    return the_list
