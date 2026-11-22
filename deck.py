def make_deck():
    """Create and return a standard deck of 52 cards."""
    deck = {}
    suits = ["♥", "♦", "♣", "♠"]
    values = {
        "A": 11, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
        "J": 10, "Q": 10, "K": 10
    }

    for suit in suits:
        for card, points in values.items():
            deck[card + suit] = points

    return deck
