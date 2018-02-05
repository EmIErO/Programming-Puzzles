import passphrases


def compare_if_anagrams(word1, word2):
    
    if len(word1) == len(word2):
        
        n = len(word1)
        same_letters = 0
        
        for letter in word1:
            if letter in word2 and word1.count(letter) == word2.count(letter):
                same_letters += 1
        
        if same_letters == n:
            return True


def find_anagrams(list_of_words):
    
    for i in range(len(list_of_words) - 1):
        for j in range(i+1, len(list_of_words)):
            if compare_if_anagrams(list_of_words[i], list_of_words[j])
                return True

def count_valid_passphrases(table):

    all_passphrases = len(table)
    valid_passphrases = all_passphrases

    for row in table:
        if find_anagrams(row):
            valid_passphrases -= 1

    return valid_passphrases

