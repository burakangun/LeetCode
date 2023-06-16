def isIsomorphic(self, s: str, t: str) -> bool:
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