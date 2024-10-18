def powerset(s: list[int]) -> list[set[int]]:
    all_sets = []
    for i in 2**len(s):
        f = set()
        for k, j in enumerate(s):
            if (i >> k) & 1:
                f.add(j)
        all_sets.append(f)
    return all_sets