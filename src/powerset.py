def powerset(A: list[int]) -> list[list[int]]:
    P = [ [] ]
    for a in A:
        added_elements = []
        for B in P:
            added_elements.append(B + [a])
        P += added_elements
    return P