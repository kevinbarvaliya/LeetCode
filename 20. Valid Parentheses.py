class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')','{':'}','[':']'}
        stack = []

        
        for char in s:
            if char in dic.keys():
                stack.append(char)
            else:
                if not stack or char != dic[stack.pop()]:
                    return False

        return not stack
