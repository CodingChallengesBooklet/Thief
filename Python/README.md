# Thief
In this code challenge we write a program that displays every possible combination of a 4 digit PIN.

## Problem
A thief has managed to find out the four digits for an online PIN code, but doesn't know the correct sequence needed to hack into the account.<br>

Design and write a program that displays all the possible combinations for any four numerical digits entered by the user. The program should avoid displaying the same combination more than once.

## Solution
In the solution (found in `solution.py`) we are going to try and produce every possible combination including duplicates.
I find this solution will be easier for a beginner to follow as it focuses on looping, and less on recursion and generators.

```python
# Function gets every pattern made from a string's characters.
def permutations(string, idx=0):
    # We check if the length-1 is the same as the index.
    if idx == len(string) - 1:
        # This indicates a cycle has been completed and a new pattern has been created.
        # We output the new pattern to the user.
        print("".join(string))

    # Here we simply loop through every character of the string
    # NOTE: idx does not change from 0 in this scope only in the recursive scopes
    for j in range(idx, len(string)):
        letters = list(string)
        # Python magic, we are swapping the elements at letters[idx] and letters[j]
        letters[idx], letters[j] = letters[j], letters[idx]
        # We make a recursive call and increase idx
        # Remember once idx is the same as length-1 we will exit back into the original scope.
        # Once in the original scope, idx is still 0, and j will increment.
        permutations(letters, idx + 1)
```
To see why this solution works, it's best to unravel the loops and function calls. 
This allows us to see exactly what's happening without all the hidden parts.
Since unravelling everything can make our code very long, we will swap out a 4 digit PIN with a set of two letters.
```python
# Original scope of the function
permutations(string, idx=0):
    string = "ab"
    idx = 0
    if idx == len(string) - 1:  # This is false
        print("".join(string)) 
        
    # First cycle of for loop
    j = 0
    letters = list(string)
    letters[idx], letters[j] = letters[j], letters[idx]  # swap "a" with "a" (does nothing)

    # Recursive function call (increment idx by 1)
    permutations(letters, idx + 1):
        idx = 1
        if idx == len(letters) - 1:  # This is true 
            print("".join(letters))  # print "ab"
        j = 1
        letters[idx], letters[j] = letters[j], letters[idx]  # swap "b" with "b" (does nothing)
        
        # Recursive function call (increment idx by 1)
        permutations(letters, idx + 1):
            idx = 2 
            if idx == len(string) - 1:  # This is false
                print("".join(string))  
            j = 2
            # Loop does not occur as j and idx are the same.
        
        # Loop finishes because j is equal to len(string).
    
    # Next cycle of the for loop
    j = 1
    letters[idx], letters[j] = letters[j], letters[idx]  # swap "a" with "b" (letters is now "ba")
    
    # Recursive function call (increment idx by 1)
    permutations(letters, idx + 1):
        idx = 1
        if idx == len(letters) - 1:  # This is true 
            print("".join(letters))  # print "ab"
        j = 1
        letters[idx], letters[j] = letters[j], letters[idx]  # swap "b" with "b" (does nothing)
        
        # Recursive function call (increment idx by 1)
        permutations(letters, idx + 1):
            idx = 2 
            if idx == len(string) - 1:  # This is false
                print("".join(string))  
            j = 2
            # Loop does not occur as j and idx are the same.
        
        # Loop finishes because j is equal to len(string).
    
    # Loop finishes
    # Function exits
    # We have printed both "ab" and "ba", all possible combinations.
```

## Extension
In the extension, our goal is to ensure none of the combinations are duplicates. 

### Extension Solution 
In our extension solution, we make use of Python's generators, and recursion to make a generator that calls itself and yields back along calls until the user of the generator receives the calls.
The solution below can be found in `solution_advanced.py`.
```python
# Our new function is a generator.
# This means it yields values every cycle of a loop.
def permutations(string):
    if len(string) <= 1:
        yield string
    else:
        # The recursive function calls yield values backwards until they reach the
        # original function scope, in which they are yielded back to the user.
        for i in range(len(string)):
            for p in permutations(string[:i] + string[i + 1:]):
                yield string[i] + p
```
We would then draw yielded values from the generator using our own loop.
```python
for pattern in permutations("ABC"):
    print(pattern)
```
This will print every possible combination from the string "ABC". 
However, we must still filter out the duplicates. 
To do this, we would create another list and append all values from patterns that is not already in our list.
This means when we first come across a value we append it, if we find a value that is the same we will not append it as it is already in the list.
```python
# Here we loop through the generator's yields to get every pattern possible.
patterns = [pattern for pattern in permutations(PIN)]

# Here we filter out repeated values
unique_patterns = []
for pattern in patterns:
    # If a pattern is already in unique_patterns then it is a duplicate.
    # We do not print or append the duplicate pattern.
    if pattern not in unique_patterns:
        unique_patterns.append(pattern)
        print(pattern)
```

### Extension Solution 2 (Real world solution)
Python is a language with "batteries included" a phrase meaning the language has lots of built-in ways of handling tasks we may want to do.
In some programming languages, writing our own `permutation` function is required as the language does not have a built-in way of getting the permutations of a string or list.
However, in Python, there is a library called `itertools` already available to us. 
`itertools` has a function called `permutations` that allows us to get every possible combination of a string or list very quickly.

An example of `itertools.permutations` can be found in `solution_advanced2.py`. 
```python
# itertools.permutations(PIN) is a generator that yields every pattern.
patterns = [pattern for pattern in itertools.permutations(PIN)]
```
The `itertools` library is part of Python's standard library.
This means, whenever you are using Python, you will always have access to `itertools` and `itertools` is written in the C programming language. 
This makes `itertools` much faster than our Python versions.

