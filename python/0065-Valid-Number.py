class Solution:
    def isNumber(self, s: str) -> bool:
        is_num = False
        seen_exp = False
        seen_dot = False
        seen_sign = False

        for c in s:
            if c in "+-":
                if seen_exp and not is_num:
                    pass
                elif seen_sign or is_num or seen_dot:
                    return False
                seen_sign = True
                is_num = False
            elif c == ".":
                if seen_dot:
                    return False
                if seen_exp:
                    return False
                seen_dot = True
            elif c in "eE":
                if not is_num:
                    return False
                if seen_exp:
                    return False
                seen_exp = True
                seen_sign = False
                is_num = False
            elif c.isdigit():
                is_num = True
            else:
                return False

        return is_num
