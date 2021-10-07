def is_two(x):
    return x in[2, '2']

def is_vowel(l):
    return l.lower() in 'aeiou' 

def is_consonant(l):
    return not is_vowel(l)

def calculate_tip(percent, total):
    return (percent * total)

def get_letter_grade(num_grade):
    if num_grade >=90:
        return('A')
    elif num_grade >=80:
        return('B')
    elif num_grade >=70:
        return('C')
    elif num_grade >=60:
        return('D')
    else:
        return('F')