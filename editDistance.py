"""This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other.
For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them."""

class stringEdition:

    def editDistance(self, original, target):

        result = (len(original) - len(target)) * ((len(original) > len(target))-(len(original) < len(target)))

        for s, s2 in zip(original, target):
            if s != s2:
                result += 1
        return result

solved = stringEdition()


print(solved.editDistance("kitten", "sitting") == 3)
print(solved.editDistance("three", "tree") == 1)

