#!/usr/bin/env python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2023 Aryaman Raina
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
Subsititution cipher frequency analysis
"""
ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
#ETAOIN = "etaoinshrdlcumwfgypbvkjxqz"

from sys import flags
from collections import Counter # Helpful class, see documentation or help(Counter)

def freqDict(ciphertext: str) -> dict:
    """
    Analyze the frequency of the letters
    """
    # Count the occurrence of each character in the ciphertext
    cipher_freq = Counter([char for char in ciphertext if char.isalpha()])  # Only consider alphabets
    
    # Sort the keys first by frequency (descending) then alphabetically (ascending)
    sorted_keys = sorted(cipher_freq.keys(), key=lambda x: (-cipher_freq[x], x))
    
    # Generate a mapping from the sorted keys to the ETAOIN string
    mapping = {}
    for i, key in enumerate(sorted_keys):
        mapping[key] = ETAOIN[i]
    
    return mapping

    #pass

def freqDecrypt(mapping: dict, ciphertext: str) -> str:
    """
    Apply the mapping to ciphertext
    """
    plaintext = ""
    
    for char in ciphertext:
        if char in mapping:
            plaintext += mapping[char]
        else:
            plaintext += char  # Preserve any characters not in the mapping
    
    return plaintext

   # pass

def test():
    "Run tests"
    assert type(freqDict("A")) is dict
    assert freqDict("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")["A"] == "E"
    assert freqDict("AABBA")['B'] == "T"
    assert freqDict("-: AB CD AH")['A'] == "E"
    assert freqDecrypt({"A": "E", "Z": "L", "T": "H", "F": "O", "U": "W", "I": "R", "Q": "D"}, "TAZZF UFIZQ!") == "HELLO WORLD!"


# Invoke test() if called via `python3 a5p1.py`
# but not if `python3 -i a5p1.py` or `from a5p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()
