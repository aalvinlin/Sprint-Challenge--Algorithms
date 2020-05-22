'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # word is less than 2 characters: not possible to find "th" inside
    if len(word) < 2:
        return 0

    else:
        # if the first two letters are "th", add one to the count.
        # count the remaining letters
        if word[0:2] == "th":
            return 1 + count_th(word[2:])

        # remove the first letter and repeat with the remaining letters
        else:
            return count_th(word[1:])
