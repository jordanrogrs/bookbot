def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_chars(char_dict):
    chars = []
    for char in char_dict:
        dict = {"char": char, "num": char_dict[char]}
        chars.append(dict)
    
    def sort_on(chars):
        return chars["num"]
    
    chars.sort(reverse=True, key=sort_on)

    return chars