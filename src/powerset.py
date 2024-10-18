def powerset(A: list[int]) -> list[set[int]]:
    P = { {} }
    for a in A:
        for B in P:
            P.add(B + a)
    return P