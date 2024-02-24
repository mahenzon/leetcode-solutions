# `defaultdict` is already imported in LeetCode

from collections import defaultdict


class Solution:
    def go_through_graph(
        self,
        already_checked: Set[int],
        knowing: Set[int],
        graph_at_time: Dict[int, Set[int]],
        who: int,
    ):
        if who in already_checked:
            return
        already_checked.add(who)
        knowing.add(who)
        for another in graph_at_time[who]:
            self.go_through_graph(
                already_checked=already_checked,
                knowing=knowing,
                graph_at_time=graph_at_time,
                who=another,
            )

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meet_at_time = defaultdict(lambda: defaultdict(set))
        who_know = {0, firstPerson}

        for p1, p2, t in meetings:
            meet_at_time[t][p1].add(p2)
            meet_at_time[t][p2].add(p1)

        for t, graph in sorted(meet_at_time.items()):
            this_time_checked = set()
            for who, others in graph.items():
                if who in who_know:
                    self.go_through_graph(
                        already_checked=this_time_checked,
                        knowing=who_know,
                        graph_at_time=graph,
                        who=who,
                    )

        return list(who_know)
