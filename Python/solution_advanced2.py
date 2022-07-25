# Python has built-in tools for what we want to do
import itertools

PIN = input("Please enter the PIN: ")

# itertools.permutations(PIN) is a generator that yields every pattern.
patterns = [pattern for pattern in itertools.permutations(PIN)]

# Here we filter out the repeated patterns.
unique_patterns = []
for pattern in patterns:
    # if a pattern is already in unique_patterns then it is a duplicate
    if pattern not in unique_patterns:
        unique_patterns.append(pattern)
        print(pattern)


