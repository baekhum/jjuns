class Solution(object):
    def isValid(self, s):
        parenthesis = {
            "(" : ")",
            "{" : "}",
            "[" : "]",
        }
        # reversed_parenthesis = {v: k for k, v in parenthesis.items()}
        
        # check_point = {"(": 0 , "{": 0, "[": 0}
        check_list = []
        
        if not s:
            return True
        
        for item in s:
            if item in {"(", "{", "["}:
                check_list.append(parenthesis[item])
            
            if item in {")", "}", "]"}:
                try:
                    if item != check_list.pop():
                        return False
                except IndexError:
                    return False
    
        return len(check_list) == 0