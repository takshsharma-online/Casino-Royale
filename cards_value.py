"""This file defines the card types and their values."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from idlelib.macosx import preferTabsPreferenceWarning
from typing import Iterable

# Following class defines the 4 Suits in a deck of cards.
class Suit(str, Enum):
    SPADES = "S"
    HEARTS = "H"
    DIAMONDS = "D"
    CLUBS = "C"

    @property
    def symbol(self) -> str:
        return {
            Suit.SPADES: "♠",
            Suit.HEARTS: "♥",
            Suit.DIAMONDS: "♦",
            Suit.CLUBS: "♣",
        }[self]
    @property
    def display_name(self) -> str:
        return self.name.title()


# Following class defines rank of all the cards in different suits.

class Rank(str, Enum):
    ACE = "A"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"

@property
def display_name(self) -> str:
    if self is Rank.ACE:
        return "Ace"
    if self in (Rank.JACK, Rank.QUEEN, Rank.KING):
        return self.name.title()
    return self.value

@property
def image_name(self) -> str:
    return self.display_name.lower()




