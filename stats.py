def wordcount(fulltext):
    wordcount = str(len(fulltext.split()))
    print("Found " + wordcount + " total words")

def charactercount(fulltext):
    char_dict = {}
    for char in fulltext.lower():
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(count):
    return count["num"]

# Turns the dictionary counts into a list
def countlist(char_dict):
    report = []
    for char, count in char_dict.items():
        new_entry = {"char": char, "num": count}
        report.append(new_entry)
    report.sort(reverse=True, key=sort_on)
    return report