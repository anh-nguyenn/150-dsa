def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = {}
    for word in strs:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())
