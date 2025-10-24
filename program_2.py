# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):
    words = []
    current_word = sentence[0]

    for char in sentence[1:]:
        if char.isupper():
            words.append(current_word)
            current_word = char
        else:
            current_word += char
    words.append(current_word)
    
    words[0] = words[0].capitalize()
    return ' '.join(words) + '.'
# Example usage

sentence = "StopAndSmellTheRoses"

new_sentence = word_separator(sentence)

print(new_sentence)