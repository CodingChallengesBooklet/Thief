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


PIN = input("Please enter your PIN: ")
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
