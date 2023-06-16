"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
def isIsomorphic(s: str, t: str) -> bool:
    pointer = 0
    holder = {}
    holder[s[0]] = t[0]

    while pointer < len(min(s, t)):

        if s[pointer] in holder:
            if t[pointer] == holder[s[pointer]]:
                pointer += 1
                continue
            else:
                return False
        else:
            if t[pointer] in holder.values():
                return False
            holder[s[pointer]] = t[pointer]

        pointer += 1

    return True