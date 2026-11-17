# Five Days in Debt

## Description

This is a text-based blackjack game written in Python. The player has seven days to manage their money, play blackjack against a dealer, and pay a daily debt installment. The goal is to survive all seven days without running out of money or missing a payment.

## How to Run the Game

1. Make sure Python 3 is installed on your computer.  
2. Save both python files in the same folder.
3. Open a terminal in the folder containing both files.  
4. Run the following command in bash:
   python blackjack.py
5. Make sure that both files remain in the same folder so Python can properly locate and import called functions

## How to Play

* Enter your name when the game starts.  
* You begin with $500 in your wallet.  
* Each day, you can play up to three hands of blackjack.  
* Enter a whole number for your bet. You cannot bet more money than you have.  
* Enter ‘h’ to hit and receive another card, or ‘s’ to stay with your current hand.  
* The dealer draws cards until reaching a score of at least 17.  
* The player with the higher score wins, unless they go over 21.  
* Winning adds the amount of your bet to your wallet. Losing subtracts the bet, and a tie returns your bet.  
* Enter 0 when asked for a bet if you want the option to skip the rest of the day.  
* At the end of each day, you must pay a debt installment. The payment starts at $250 and increases by 25% each day.

You win by completing all 5 days with money remaining. You lose if your wallet reaches zero or you cannot afford the required daily payment (finishing the final day with $0 is still a win).

## How the Program Tracks the Player's State

The program uses a variable named wallet to represent the player's current money. It starts at $500 and changes after every blackjack hand and daily payment. This is a simple way to track the player's progress because money determines whether they can continue playing and afford their debt payments.  
The program also uses a day variable to track progress through the week and a hands\_played\_today variable to limit the number of hands per day.  
The check\_game\_status() function checks the wallet and current day to determine whether the player has lost, won, or should continue playing. This keeps the game's win/loss logic in one place.

## Randomness and Game Logic

The built-in Python random module selects cards from the deck, making each hand different. Dictionaries store card values, while lists store the cards in the player's and dealer's hands. A scoring function adjusts aces from 11 points to 1 when necessary to prevent a hand from exceeding 21 when possible.  
The game uses while loops to repeat hands and days, and if/elif/else statements to handle player choices and compare blackjack scores. Input validation prevents invalid bets from crashing the program.

## Requirements

* Python 3  
* No external libraries required

