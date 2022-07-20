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

In this solution, we will produce every combination possible and then filter out the duplicant combinations. This isn't necessarily the most efficient method but will be the easiest to understand. First, we will write a function that takes a string and an index, and produces a list of strings where each letter is replaced by the letter at the index provided. We will then write another function that loops through every index of a string, applies the function previously stated, and stores the combinations. After all that we will filter the list of combinations for duplicants, then finally display the list of combinations to the user.<br>

First let's write a function that produces a list of string where each letter is replaced by the letter at the index provided.
