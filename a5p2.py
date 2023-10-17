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
Problem 2
"""

from sys import flags
import numpy as np
def evalDecipherment(text1: str, text2: str) -> [float, float]:
    """
    docstring
    """
    # Convert both texts to uppercase for case-insensitive comparison
    text1 = text1.upper()
    text2 = text2.upper()

    # Filter out non-alphabet characters
    text1_alpha = ''.join([char for char in text1 if char.isalpha()])
    text2_alpha = ''.join([char for char in text2 if char.isalpha()])

    # Key Accuracy
    unique_chars_text1 = set(text1_alpha)
    correct_keys = sum(1 for char in unique_chars_text1 if text1_alpha.find(char) != -1 and text1_alpha[text1_alpha.find(char)] == text2_alpha[text1_alpha.find(char)])
    key_accuracy = correct_keys / len(unique_chars_text1)

    # Decipherment Accuracy
    correct_decipher = sum(1 for c1, c2 in zip(text1_alpha, text2_alpha) if c1 == c2)
    decipherment_accuracy = correct_decipher / len(text1_alpha)

    return [key_accuracy, decipherment_accuracy]


    #raise NotImplementedError()


def test():
    "Run tests"
    np.testing.assert_array_almost_equal(evalDecipherment("this is an example", "tsih ih an ezample") , [0.7272727272727273, 0.7333333333333333])
    np.testing.assert_almost_equal(evalDecipherment("the most beautiful course is 331!", "tpq munt bqautiful cuurnq in 331!") , [0.7142857142857143, 0.625])
if __name__ == '__main__' and not flags.interactive:
    test()
