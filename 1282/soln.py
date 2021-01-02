class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups_by_size = {}
        for person, size in enumerate(groupSizes):
            if size not in groups_by_size:
                groups_by_size[size] = [[]]
            if len(groups_by_size[size][-1]) < size:
                groups_by_size[size][-1].append(person)
            else:
                groups_by_size[size].append([person])
        r = []
        for v in groups_by_size.values():
            r.extend(v)
        return r
