def isPalindrome(self, x: int) -> bool:
    x = str(x)
    list_X = [i for i in x]
    reversedList_X = list(reversed(list_X))
    if list_X == reversedList_X:
        return True
    else:
        return False