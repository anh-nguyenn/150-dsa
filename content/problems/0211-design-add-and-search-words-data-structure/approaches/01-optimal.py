class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["#"] = True

    def search(self, word: str) -> bool:
        def dfs(node: dict, index: int) -> bool:
            if index == len(word):
                return "#" in node
            ch = word[index]
            if ch == ".":
                return any(
                    key != "#" and dfs(child, index + 1)
                    for key, child in node.items()
                )
            child = node.get(ch)
            return child is not None and dfs(child, index + 1)

        return dfs(self.root, 0)
