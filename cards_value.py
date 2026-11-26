"""This file defines the card types and their values."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
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
    """A standard playing card.

    Rank and suit may be enum values or short codes such as Card("A", "S").
    The stored values are always Rank and Suit.
    """

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


@dataclass(frozen=True)
class HandValue:
    """The best blackjack total for a hand, with ace softness information."""

    total: int
    is_soft: bool
    is_blackjack: bool

    @property
    def is_bust(self) -> bool:
        return self.total > 21


def rank_value(rank: Rank) -> int:
    """Return a rank's blackjack value (ace is initially counted as 11)."""
    if not isinstance(rank, Rank):
        try:
            rank = Rank(rank)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Unknown card rank: {rank!r}") from exc

    if rank is Rank.ACE:
        return 11
    if rank in (Rank.JACK, Rank.QUEEN, Rank.KING, Rank.TEN):
        return 10
    return int(rank.value)


def card_value(card: Card) -> int:
    """Return a card's value before adjusting aces in a hand."""
    if not isinstance(card, Card):
        raise TypeError("card_value expects a Card")
    return rank_value(card.rank)


def hand_value(cards: Iterable[Card]) -> HandValue:
    """Calculate a hand total, treating aces as 1 when 11 would bust.

    ``is_soft`` is true when at least one ace still counts as 11 in the best
    total. A natural blackjack is exactly two cards totaling 21.
    """
    card_list = tuple(cards)
    if any(not isinstance(card, Card) for card in card_list):
        raise TypeError("hand_value expects an iterable of Card objects")

    total = sum(card_value(card) for card in card_list)
    aces = sum(card.rank is Rank.ACE for card in card_list)

    while total > 21 and aces:
        total -= 10
        aces -= 1

    return HandValue(
        total=total,
        is_soft=aces > 0,
        is_blackjack=len(card_list) == 2 and total == 21,
    )


__all__ = [
    "Card",
    "HandValue",
    "Rank",
    "Suit",
    "card_value",
    "hand_value",
    "rank_value",
]