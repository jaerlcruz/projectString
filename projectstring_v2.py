with open(r"C:\Users\justi\OneDrive - CSULB\Documents\fall 2022\cecs\mobysmall.txt") as f: # r before the file bath to specify that it's raw string
    text = f.read()
# print(text)

def mirror(string):  # A
    return string + string[::-1]

def remove(string, letter):  # B
    removed = ''
    for i in string:
        if i != letter:
            removed += i
    return removed

def e_num(string):  # C
    num_e = string.count('e') + string.count('E')
    percent = num_e / len(string)
    return f'Your text contains {len(string)} characters, of which {num_e} ({percent}%) are \'e\'.'

def char_num(string, char):  # D
    num_char = string.count(char)
    percent = num_char / len(string)
    return f'Your text contains {len(string)} characters, of which {num_char} ({percent}%) are \'{char}\'.'

def no_e(string):  # E
    if (string.count('e') and string.count('E')) == 0:
        return True
    else:
        return False

def no_char(string, char):  # F
    if string.count(char) == 0:
        return True
    else:
        return False

def no_e_words(string):  # G
    words = string.split()
    no_e_string = ''
    num_e_words = 0
    for i in words:
        if 'e' in i:
            no_e_string += i
            num_e_words += 1
    percent = num_e_words / len(words)
    return no_e_string, percent

def avoids(string, forbidden): # H
    true_or_false = True
    for i in string:
        if forbidden in i:
            true_or_false = False
    return true_or_false

def avoids1(string, forbidden): # H part 2??/
    words = string.split()
    num_unforbidden = 0
    for i in words:
        if forbidden not in i:
            num_unforbidden += 1
    return num_unforbidden

def uses_only(string, letters): # I 
    for i in string:
        if i in letters:
            return True
        else:
            return False

def uses_all(string, required): # J
    count = 0
    for letter in required:
        if letter in string:
            count += 1
    if count == len(required):
        return True
    else: 
        return False

def is_abecedarian(string): # K
    string = string.lower()
    if len(string) <= 1:
        return True
    for i in range(1, len(string)):
        if ord(string[i-1]) > ord(string[i]):
            return False
        else:
            return True

def find(string, char):  # L
    return string.find(char)

def find_index(string, char, index):  # M
    return string.find(char, index)

def is_sorted(string): # N
    for i in range(1, len(string)):
        if string[i-1] > string[i]:
            return False
        else:
            return True

def is_anagram(string, string1): # O
    count = 0
    for letter in string:
        if letter in string1:
            count += 1
    if count == len(string) == len(string1):
        return True
    else: 
        return False

def has_duplicates(string): # P
    for letter in string:
        if string.count(letter) > 1:
         return True

def remove_duplicates(string): # Q
    newstring = ''
    duplicate = []
    for letter in string:
        if letter not in duplicate:
            newstring += letter
            duplicate.append(letter)
    return newstring


if __name__ == "__main__":
    string = text
    # following variables are just so the functions can run
    string1 = 'dog'
    char = 'o'
    forbidden = 'z'
    letters = ['h', 'i']
    required = ['a', 'e', 'i', 'o', 'u']
    index = 2
    with open(r"C:\Users\justi\OneDrive - CSULB\Documents\fall 2022\cecs\projectstringsv2.txt", 'w') as f:
        print('A', mirror(string), file=f)
        print('B', remove(string, char), file=f)
        print('C', e_num(string), file=f)
        print('D', char_num(string, char), file=f)
        print('E', no_e(string), file=f)
        print('F', no_char(string, char), file=f)
        print('G', no_e_words(string), file=f)
        print('H', avoids(string, forbidden), file=f)
        print('H1', avoids1(string, forbidden), file=f)
        print('I', uses_only(string, letters), file=f)
        print('J', uses_all(string, required), file=f)
        print('K', is_abecedarian(string), file=f)
        print('L', find(string, char), file=f)
        print('M', find_index(string, char, index), file=f)
        print('N', is_sorted(string), file=f)
        print('O', is_anagram(string, string1), file=f)
        print('P', has_duplicates(string), file=f)
        print('Q', remove_duplicates(string), file=f)
