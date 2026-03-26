# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:09:21 2026

@author: mikej
"""

def word_filter(sentence, bad_words):
    words = sentence.split()
    filtered_words = []

    for word in words:
        clean_word = word.lower().strip(".,!?")

        if clean_word in bad_words:
            filtered_words.append("*" * len(word))
        else:
            filtered_words.append(word)
    return " ".join(filtered_words)

if __name__ == "__main__":
    sentence = "This is a bad and ugly example."
    bad_words = ["bad", "ugly"]

    result = word_filter(sentence, bad_words)
    print(result)