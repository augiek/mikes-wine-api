# function that takes a list of strings and returns the longest palindrome

# ['ata', 'abc', 'abba']

# assume lowercase letters only

# determine whether each string is a palindrome
#     isolate each string from the list via loop
#         reverse string, compare with original
#             if equal, then palindrome
#             not not, then not palindrome
# determine the length of each palindrome
#     variable that holds the longest one so far
# return the longest one


def palindrome(lst):
    longest_pal = ""
    for word in lst:
        if word[::-1] == word:
            if len(word) > len(longest_pal):
                longest_pal = word
    if len(longest_pal) > 0:
        return longest_pal
    else: 
        return ("No palindromes here.")


print(palindrome(['atac', 'abc', 'abbac', 'racecarc']))