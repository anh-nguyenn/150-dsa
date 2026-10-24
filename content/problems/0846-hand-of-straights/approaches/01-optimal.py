from collections import Counter


def is_n_straight_hand(hand: list[int], group_size: int) -> bool:
    if len(hand) % group_size != 0:
        return False

    counts = Counter(hand)
    for card in sorted(counts):
        amount = counts[card]
        if amount == 0:
            continue
        for step in range(group_size):
            if counts[card + step] < amount:
                return False
            counts[card + step] -= amount
    return True
