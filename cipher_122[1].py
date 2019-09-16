import sys

def sorter(t):
    return t[-1]

def get_shift_value(alphanum, most_common_letter):
    if alphanum.index(most_common_letter) <= alphanum.index("E"):
        shift_value = alphanum.index("E") - alphanum.index(most_common_letter)
        return shift_value
    else:
        shift_value = (alphanum.index("E") + 36) - alphanum.index(most_common_letter)
        return shift_value

def get_most_common_letter(lines):
    letter_occurences = {}
    for char in lines:   
        if char not in letter_occurences and char.isalnum():
            letter_occurences[char] = 1       
        elif char in letter_occurences:
            letter_occurences[char] += 1
    sorted_dict = sorted(letter_occurences.items(), key=sorter, reverse=True)
    most_common_letter = sorted_dict[0][0]
    return most_common_letter

def caesar(text, shift_value, alphanum): 
    shifted_alphanum = alphanum[shift_value:] + alphanum[:shift_value]
    table = str.maketrans(alphanum, shifted_alphanum)
    return text.translate(table)

def main(): 
    alphanum = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    encrypted_text = "".join([w for w in sys.stdin])
    most_common_letter = get_most_common_letter(encrypted_text)
    shift_number = get_shift_value(alphanum, most_common_letter)
    characters = [char for char in encrypted_text]
    decrypted_text = caesar("".join(characters), shift_number, alphanum)
    print(decrypted_text.strip())

if __name__ == "__main__":
    main()
