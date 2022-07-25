# Thief
In this code challenge we write a program that displays every possible combination of a 4 digit PIN.

![GitHub followers](https://img.shields.io/github/followers/hrszpuk?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/hrszpuk?style=social)
<br>
![GitHub language count](https://img.shields.io/github/languages/count/CodingChallengesBooklet/Thief?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/CodingChallengesBooklet/Thief?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/CodingChallengesBooklet/Thief?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/CodingChallengesBooklet/Thief?style=for-the-badge)
![GitHub branch checks state](https://img.shields.io/github/checks-status/CodingChallengesBooklet/Thief/main?style=for-the-badge)

## Problem
A thief has managed to find out the four digits for an online PIN code, but doesn’t know the correct sequence needed to hack into the account.<br>

Design and write a program that displays all the possible combinations for any four numerical digits entered by the user. The program should avoid displaying the same combination more than once.

## Solution
*NOTE: The solution explained here is a generalised solution. If you want a language-specific solution read the explanation in the language folder of your choice.*<br>

The solution to this problem is to get the `permutations` of the list. `permutations` are a mathematical construct in which we get every possible combination of items within a `set`. 
An example of this is shown below. 
```
The permutation of set A={a,b} is 2, such as {a,b}, {b,a}.
```
In our first solution, we will try to brute force the PIN combinations. 
We can do this by looping through every single possible combination of numbers made with the numbers of the PIN,
and then filtering out all duplicate letters.
``` 
pin = INPUT
LOOP FOR EVERY LETTER IN pin
    LOOP FOR EVERY LETTER IN pin
        LOOP FOR EVERY LETTER IN pin
            LOOP FOR EVERY LETTER IN pin
                IF NO LETTERS ARE THE SAME
                    OUTPUT LETTERS COMBINED
```
We can also write this solution in Python to see how we would handle this in actual code.
```python
PIN = input() 
for h in PIN:
    for j in PIN:
        for k in PIN:
            for l in PIN:
                if h != j and h != k and h != l and j != k and j != l and k != l:
                    print(h + j + k + l)
```
This method has the most disadvantages. 
Firstly, we are looping through every possible combination that can be made with the numbers of the PIN. 
This is extremely inefficient. Secondly, our solution only works if every number of the PIN is unique. 
So, PINs such as 1292, 0011, 2474, would not work as they have duplicates already.



