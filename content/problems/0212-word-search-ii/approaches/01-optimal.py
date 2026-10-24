class _TrieNode:
    __slots__ = ("children", "word")

    def __init__(self):
        self.children = {}
        self.word = None


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    root = _TrieNode()
    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = _TrieNode()
            node = node.children[ch]
        node.word = word

    rows, cols = len(board), len(board[0])
    found: list[str] = []

    def dfs(row: int, col: int, parent: _TrieNode) -> None:
        ch = board[row][col]
        node = parent.children.get(ch)
        if node is None:
            return
        if node.word is not None:
            found.append(node.word)
            node.word = None

        board[row][col] = "#"
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                dfs(nr, nc, node)
        board[row][col] = ch

        if not node.children:
            parent.children.pop(ch, None)

    for row in range(rows):
        for col in range(cols):
            dfs(row, col, root)
    return found
