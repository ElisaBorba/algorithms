def is_palindrome_iterative(word):

    if word == "":
        return False

    for i in range(len(word)):
        if word[i] != word[len(word) - 1 - i]:
            return False
    return True
