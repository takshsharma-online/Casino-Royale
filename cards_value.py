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


@dataclass(frozen=True)
class Card:
    """This class represents a standard playing card. Rank  and suit may be enum values such as Card (A,S). The stored values are always Rank and Suit."""
    rank: Rank
    suit: Suit

    def __post_init__(self) -> None:
        try:
            object.__setattr__(self, "rank", Rank(self.rank))
            object.__setattr__(self, "suit", Suit(self.suit))
        except ValueError as exc:
            raise ValueError("Card rank or suit is not recognized") from exc

        @property
        def value(self) -> int:
            """Blackjack value when an ace is initially counted as 11."""
            return rank_value(self.rank)

        @property
        def short_code(self) -> str:
            return f"{self.rank.value}{self.suit.value}"

        @property
        def display_name(self) -> str:
            return f"{self.rank.display_name} of {self.suit.display_name}"

        @property
        def display_text(self) -> str:
            return f"{self.rank.value}{self.suit.symbol}"

        @property
        def image_key(self) -> str:
            return f"{self.rank.image_name}_of_{self.suit.name.lower()}"


