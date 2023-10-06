class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1
        carry = 1

        while carry:
            if idx >= 0:
                if digits[idx] == 9:
                    # carry = 1
                    digits[idx] = 0
                else:
                    digits[idx] += 1
                    carry = 0
            else:
                # digits.insert(0, carry)
                digits.insert(0, 1)
                # stop loop
                carry = 0

            idx -= 1

        return digits
