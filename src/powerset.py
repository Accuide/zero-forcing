from itertools import chain, combinations

def powerset(iterable: set[int]) -> list[set[int]]:
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))