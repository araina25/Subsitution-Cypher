# CMPUT 331, Fall 2023, Assignment 5

**The Three files in the submission are**:

- **a5p1.py** for problem 1
- **a5p2.py** for problem 2
- **README** 

## Problem 1:

The task is to create a Python module named **a5p1.py**. This module should contain two primary functions:

- **freqDict(ciphertext)**
- **freqDecrypt(mapping, ciphertext)**

Detailed specifications for these functions can be found in the assignment prompt.

**Important Note:** The frequency analysis method used in this problem is not perfect and may not always return the correct key for decipherment.

### Sample Tests:

```
>> freqDict("AABBA")[’B’]
"T"
>> freqDict("-: AB CD AH")[’A’]
"E"
>> freqDict("MKLAKAALK")
{’A’: ’E’, ’K’: ’T’, ’L’: ’A’, ’M’: ’O’}
>> freqDecrypt({"A":"E","Z":"L","T":"H","F":"O","U":"W","I":"R","Q":"D"}, "TAZZF UFIZQ!")
HELLO WORLD!
```

## Problem 2:

This problem discusses two primary ways of evaluating a solution to a simple substitution cipher:

1. **Key Accuracy**
2. **Decipherment Accuracy**

You are to create a Python module named **a5p2.py**. This module should contain a function called **evalDecipherment(text1, text2)**. This function will compute the key and decipherment accuracies.

### Sample Tests:

```
>> evalDecipherment("this is an example", "tsih ih an ezample")
[0.7272727272727273, 0.7333333333333333]
>> evalDecipherment("the most beautiful course is 331!", "tpq munt bqautiful cuurnq in 331!")
[0.7142857142857143, 0.625]
```

## References:

When working on this assignment, various resources might be utilized, whether it's official documentation, textbooks, online forums, or other means. It's vital to give proper attribution to these sources to maintain academic integrity and give credit to the original authors. Below are some references used for this assignment:

1. **The Code Book -- Simon Singh** -- Downloaded copy
   
2. **Python Official Documentation**: Often referred to for understanding the intricacies of specific functions and methods. Available at [Python's official website](https://docs.python.org/3/).

3. **Class Notes** -- Subsitution Cipher

