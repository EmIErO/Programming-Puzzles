import passphrases


def compare_if_anagrams(word1, word2):
    
    n = len(word1)
    same_letters = 0
    
    for letter in word1:
        if letter in word2 and word1.count(letter) == word2.count(letter):
            same_letters += 1
    
    if same_letters == n:
        return True


def find_anagrams(row):
    
    for i in range(len(row) - 1):
        for j in range(i+1, len(row)):
            if len(row[i]) == len(row(j)) and compare_if_anagrams(row[i], row[j])
                return True

