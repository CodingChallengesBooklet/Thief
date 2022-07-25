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


PIN = input("Please enter the PIN: ")
permutations(PIN)
