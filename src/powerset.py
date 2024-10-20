def powerset(A: list[int]):
    P: list[set[int]] = [ set() ]
    for a in A:
        added_elements = []
        for B in P:
            new_set: set[int] = B.union({ a })
            yield new_set
            added_elements.append(new_set)
        P += added_elements

def powerset_under_k(A: list[int], k: int):
    P: list[set[int]] = [ set() ]
    for a in A:
        added_elements = []
        for B in P:
            if len(B) < k:
                new_set: set[int] = B.union({ a })
                yield new_set
                added_elements.append(new_set)
        P += added_elements