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

def evalDecipherment(txt_1: str, txt_2: str) -> [float, float]:
    """
    docstring
    """
    # Converting the given texts to uppercase 
    txt_1 = txt_1.upper()
    txt_2 = txt_2.upper()

    # Filteing out non alphabetical charactors
    txt_1_alpha = ''.join([i for i in txt_1 if i.isalpha()])
    txt_2_alpha = ''.join([i for i in txt_2 if i.isalpha()])

    # Checking for key accuracy 
    unique_chars_txt_1 = set(txt_1_alpha)
    accuracy = sum(1 for i in unique_chars_txt_1 if txt_1_alpha.find(i) != -1 and txt_1_alpha[txt_1_alpha.find(i)] == txt_2_alpha[txt_1_alpha.find(i)])
    key_accuracy = accuracy / len(unique_chars_txt_1)

    # Checking for key accuracy while deciphering the cipher
    decipher = sum(1 for c1, c2 in zip(txt_1_alpha, txt_2_alpha) if c1 == c2)
    decipherment_accuracy = decipher / len(txt_1_alpha)

    return [key_accuracy, decipherment_accuracy]


    #raise NotImplementedError()


def test():
    "Run tests"
    np.testing.assert_array_almost_equal(evalDecipherment("this is an example", "tsih ih an ezample") , [0.7272727272727273, 0.7333333333333333])
    np.testing.assert_almost_equal(evalDecipherment("the most beautiful course is 331!", "tpq munt bqautiful cuurnq in 331!") , [0.7142857142857143, 0.625])
if __name__ == '__main__' and not flags.interactive:
    test()
