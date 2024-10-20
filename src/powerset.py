def powerset(A: list[int]) -> list[list[int]]:
    P = [ [] ]
    for a in A:
        added_elements = []
        for B in P:
            added_elements.append(B + [a])
        P += added_elements
    return P

def powerset_under_k(A: list[int], k: int) -> list[list[int]]:
    P = [ [] ]
    for a in A:
        added_elements = []
        for B in P:
            if len(B) < k:
                added_elements.append(B + [a])
        P += added_elements
    return P