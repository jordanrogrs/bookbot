def count_words(text):
    return len(text.split())

def count_chars(text):
    char_count = {}
    for c in text:
        c = c.lower()
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] += 1
    return char_count

def sort_chars(char_dict):
    items = [{"char": c, "num": n} for c, n in char_dict.items()]

    def sort_on(items):
        return items["num"]
    
    items.sort(reverse=True, key=sort_on)

    return items