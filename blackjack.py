"""
A day in the life of a blackjack player who has to pay off debt over the course 
of a week.
"""

import random
from deck import make_deck

STARTING_MONEY = 500
wallet = STARTING_MONEY

day = 1
TOTAL_DAYS = 5
HANDS_PER_DAY = 3
hands_played_today = (0)

def deal_card(remaining_deck, used_deck, hand):
    """Deal one random card into a hand and record it as used.
    
    This function selects a random card from the deck made before this, removes
    it from the deck, and appends it to one a hand.
    """
    if not remaining_deck:
        remaining_deck.update(used_deck)
        used_deck.clear()

    selected_card = random.choice(list(remaining_deck))
    card_value = remaining_deck.pop(selected_card)
    used_deck[selected_card] = card_value
    hand.append(selected_card)

def score_hand(hand, used_deck):
    """Calculate a hand's score, counting aces as 1 when necessary."""
    score = sum(used_deck[card] for card in hand)
    aces = sum(1 for card in hand if card.startswith("A"))

    while score > 21 and aces > 0:
        score -= 10
        aces -= 1

    return score

def starting_cards(remaining_deck, used_deck):
    """Deal two cards to the player and two to the dealer."""
    player_hand = []
    dealer_hand = []

    deal_card(remaining_deck, used_deck, player_hand)
    deal_card(remaining_deck, used_deck, dealer_hand)
    deal_card(remaining_deck, used_deck, player_hand)
    deal_card(remaining_deck, used_deck, dealer_hand)

    return player_hand, dealer_hand

def show_hands(player_hand, dealer_hand, used_deck, reveal=False):
    """Display the player's hand and the dealer's visible cards."""
    print("\nYour hand:", player_hand)
    print("Your score:", score_hand(player_hand, used_deck))

    if reveal:
        print("Dealer's hand:", dealer_hand)
        print("Dealer's score:", score_hand(dealer_hand, used_deck))
    else:
        print("Dealer's visible card:", dealer_hand[0])

def hit_or_stay(player_hand, dealer_hand, remaining_deck, used_deck):
    """Let the player hit or stay until they stay or bust.
    
    Takes user inputs to see if they draw more cards until they are at/over 21, keep 
    their current cards, and manages improper inputs.

    Inputs:
      choice: the choice the player makes on if they want to hit or stay.

    Returns:
      What score the player has after their choice.
    """
    while score_hand(player_hand, used_deck) < 21:
        show_hands(player_hand, dealer_hand, used_deck)
        choice = input("Would you like to hit or stay? (h/s): ")
        choice = choice.lower().strip()

        if choice == "h":
            deal_card(remaining_deck, used_deck, player_hand)
        elif choice == "s":
            break
        else:
            second_chance = input("Invalid choice. Please pick h or s. ")
            if second_chance == "h":
                deal_card(remaining_deck, used_deck, player_hand)
            else:
                break

    if score_hand(player_hand, used_deck) > 21:
        print("You busted!")

    return score_hand(player_hand, used_deck)

def dealer_turn(dealer_hand, remaining_deck, used_deck):
    """Make the dealer draw cards until reaching at least 17."""
    while score_hand(dealer_hand, used_deck) < 17:
        deal_card(remaining_deck, used_deck, dealer_hand)

def compare_scores(player_hand, dealer_hand, used_deck, bet, wallet):
    """Compare both scores and return the updated wallet."""
    player_score = score_hand(player_hand, used_deck)
    dealer_score = score_hand(dealer_hand, used_deck)

    print("\nFinal player score:", player_score)
    print("Final dealer score:", dealer_score)

    if player_score > 21:
        print("You busted. You lose.")
        wallet -= bet
    elif dealer_score > 21:
        print("The dealer busted. You win!")
        wallet += bet
    elif player_score > dealer_score:
        print("You got a higher score. You win!")
        wallet += bet
    elif player_score < dealer_score:
        print("You got a lower score. You lose.")
        wallet -= bet
    else:
        print("You and the dealer tied. Your bet is returned.")

    print(f"Your wallet now contains ${wallet}.")
    return wallet

def end_of_hand(player_hand, dealer_hand):
    """Return used cards to the deck and clear both hands."""
    player_hand.clear()
    dealer_hand.clear()

def check_game_status(wallet, day):
    """Return win, loss, or continue based on the player's state."""
    if wallet < 0:
        return "loss"
    elif day > TOTAL_DAYS:
        return "win"
    elif wallet == 0:
        return "loss"
    else:
        return "continue"

def get_bet(wallet):
    """Ask for a valid bet that the player can afford, or zero to stop."""
    while True:
        try:
            bet = int(input(
                f"How much would you like to bet? "
                f"(1-${wallet}, or 0 to stop): "
            ))

            if 0 <= bet <= wallet:
                return bet
            else:
                print(f"Enter a number between 0 and {wallet}.")
        except ValueError:
            print("Please enter a whole number.")

def end_of_day(wallet, day):
    """Collect the day's payment and return the updated wallet."""
    required_points = int(250 * 1.25 ** (day - 1))

    print(f"\nDay {day} payment due: ${required_points}")

    if wallet < required_points:
        print("You cannot afford the payment. You lose!")
        return 0

    wallet -= required_points
    print(f"You paid ${required_points}.")
    print(f"Money remaining: ${wallet}")

    return wallet

def main():
    """Run the seven-day blackjack game."""
    wallet = STARTING_MONEY
    day = 1
    remaining_deck = make_deck()
    used_deck = {}

    print("Welcome to Blackjack: A Week to Pay Off Your Debt!")
    name = input("What is your name? ").strip()

    if not name:
        name = "Player"

    print(f"\nGood luck, {name}! You start with ${wallet}.")

    while day <= TOTAL_DAYS:
        print(f"\n{'=' * 12} DAY {day} {'=' * 12}")
        print(f"\nYou will owe ${int(250 * 1.25 ** (day - 1))} at the end of the day.")
        hands_played_today = 0

        if hands_played_today == 0:
            remaining_deck.update(used_deck)
            used_deck.clear()

        while hands_played_today < HANDS_PER_DAY:
            status = check_game_status(wallet, day)
            if status != "continue":
                break

            print(
                f"\nHand {hands_played_today + 1} "
                f"of {HANDS_PER_DAY}"
            )
            print(f"Current wallet: ${wallet}")

            player_bet = get_bet(wallet)

            if player_bet == 0:
                skip = input(
                    "Skip the rest of the day? (y to skip): "
                ).lower().strip()

                if skip == "y":
                    break
                else:
                    continue

            player_hand, dealer_hand = starting_cards(
                remaining_deck, used_deck
            )

            show_hands(player_hand, dealer_hand, used_deck)

            player_score = hit_or_stay(
                player_hand, dealer_hand, remaining_deck, used_deck
            )

            if player_score <= 21:
                dealer_turn(dealer_hand, remaining_deck, used_deck)

            show_hands(
                player_hand, dealer_hand, used_deck, reveal=True
            )

            wallet = compare_scores(
                player_hand, dealer_hand, used_deck,
                player_bet, wallet
            )

            end_of_hand(
                player_hand, dealer_hand
            )
            hands_played_today += 1

            status = check_game_status(wallet, day)
            if status == "loss":
                break

        status = check_game_status(wallet, day)
        if status == "loss":
            break

        wallet = end_of_day(wallet, day)

        status = check_game_status(wallet, day)
        if status == "loss":
            break

        day += 1

    status = check_game_status(wallet, day)

    if status == "win":
        print(
            f"\nCongratulations, {name}! You survived all five days "
            f"and paid your daily installments. You have ${wallet} left!"
        )
    else:
        print(
            f"\nGame over, {name}. You ran out of money "
            "or could not pay your debt."
        )

if __name__ == "__main__":
    main()
