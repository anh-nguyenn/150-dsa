class Codec:
    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(word)}:{word}" for word in strs)

    def decode(self, s: str) -> list[str]:
        result: list[str] = []
        index = 0
        while index < len(s):
            delimiter = s.index(":", index)
            length = int(s[index:delimiter])
            start = delimiter + 1
            result.append(s[start:start + length])
            index = start + length
        return result
