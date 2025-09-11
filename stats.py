def get_num_words(text_from_book):
    temp = text_from_book.split()
    return len(temp)

def get_char_count(text_from_book):
    char_stats = {}
    words = text_from_book.split()
    for word in words:
        lowercase_word = word.lower()
        for char in lowercase_word:
            if(char in char_stats):
                char_stats[char] += 1
            else:
                char_stats[char] = 1
    return char_stats

def sort_on(items):
    return(items["num"])

def sort_char_count(char_stats):
    sort_char_stat = []
    for char in char_stats:
        sort_char_stat.append({"char": char, "num": int(char_stats[char])})
    sort_char_stat.sort(key=sort_on, reverse=True)
    return sort_char_stat