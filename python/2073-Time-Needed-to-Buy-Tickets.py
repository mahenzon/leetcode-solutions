class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ref_val = tickets[k]
        for idx, num in enumerate(tickets):
            tickets[idx] = min(ref_val - (idx > k), num)
        return sum(tickets)
