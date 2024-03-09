#!/usr/bin/env python3
import sys

def Anagram_Finder(wordList):
    anagrams = {}

    for word in wordList:
       sorted_word = ''.join(sorted(word))
       
       if sorted_word not in anagrams:
           anagrams[sorted_word] = []
       anagrams[sorted_word].append(word)

    return anagrams


wordList = sys.argv[1:]
word_anagrams = Anagram_Finder(wordList)

for sorted_word, unsorted_word in word_anagrams.items():
    if len(unsorted_word) > 1:
        print(f"{sorted_word} : {unsorted_word}")

