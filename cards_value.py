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



