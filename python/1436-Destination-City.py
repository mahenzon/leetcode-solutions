class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = set()
        for city_from, _ in paths:
            outgoing.add(city_from)

        for _, city_to in paths:
            if city_to not in outgoing:
                return city_to
