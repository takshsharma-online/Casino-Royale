**Casino Royale- Project Description**

Casino Royale is a graphical Blackjack game developed with Python using PyQt6 to create the game window and controls. The program is managed through Anaconda, which provides environment for installing and organizing the project' python packages. The game recreates the basic experience of playing Blackjack against a computer-controlled dealer, while giving the player a simple interface to view their cards, track their total, and choose what to do next.

At beginning of each round, the player and dealer are each dealt two cards. The player’s goal is to get a hand value as close to 21 as possible without going over. Number cards are worth their face value, while Kings, Queens, and Jacks are worth 10 points. An Ace can count as either 1 or 11, depending on which value is more helpful for the hand.

After receiving their cards, the player can choose to Hit to take another card or Stand to keep their current total. The player may continue hitting until they stand or their total goes over 21. Going over 21 is called a bust, and means the player loses the round. If the player stands without busting, the dealer takes their turn. The dealer reveals their hidden card and draws additional cards until reaching at least 17.

Once the dealer has finished, the game compares the two hand totals. The player wins if their total is higher than the dealer’s without exceeding 21. The dealer wins if the player busts or the dealer has a higher total. If both totals are equal, the round is a tie. A hand with an Ace and a 10-point card as the player’s first two cards is called Blackjack and is the strongest starting hand.

The project brings together card-game rules, decision-making logic, and desktop interface design. It provides a practical way to explore Python programming while creating an interactive game with PyQt6.