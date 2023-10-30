import unittest
import random


class Card:
    def __init__(self, suit, value):
        if not isinstance(suit, str):
            raise TypeError("Suit must be a string")
        if not isinstance(value, str):
            raise TypeError("Vlue must be a string")
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        self.Cards = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.Cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.Cards)

    def draw(self):
        if self.Cards:
            drawn_card = self.Cards.pop()
            print(f"Drawn card: {drawn_card.value} of {drawn_card.suit}")
        else:
            print("The deck is empty.")


class Test_Deck(unittest.TestCase):

    def test_deck_creation(self):
        # Test deck creation and check if it has 52 cards
        deck = Deck()
        self.assertEqual(len(deck.Cards), 52)

    def test_shuffle_deck(self):
        # Test shuffling the deck
        deck = Deck()
        original_order = deck.Cards[:]
        deck.shuffle()
        self.assertNotEqual(original_order, deck.Cards)  # Check that after shuffling, the deck is not in the original order

    def test_draw_card(self):
        # Test drawing a card from the deck
        deck = Deck()
        drawn_card = deck.draw()
        self.assertIsNotNone(drawn_card)  # Check that a card is drawn
        self.assertEqual(len(deck.Cards), 51)  # Check that after drawing, the deck has one less card

    def test_draw_all_cards(self):
        # Test drawing all cards from the deck
        deck = Deck()
        while deck.Cards:
            deck.draw()
        self.assertIsNone(deck.draw())  # Drawing from an empty deck should return None

    def test_draw_until_empty_deck(self):
        # Test drawing all cards and verify the last drawn card
        deck = Deck()
        all_drawn_cards = []
        while deck.Cards:
            drawn_card = deck.draw()
            all_drawn_cards.append(drawn_card)
        
        # Check the number of drawn cards matches the total cards in a deck
        self.assertEqual(len(all_drawn_cards), 52)
        
        # Verify the last drawn card is a random card after drawing all cards
        last_drawn_card = all_drawn_cards[-1]

        # Ensure the last drawn card is within the range of a standard deck
        self.assertIn(last_drawn_card.suit, ["Hearts", "Diamonds", "Clubs", "Spades"])
        self.assertIn(last_drawn_card.value, ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"])

    def test_draw_from_empty_deck(self):
        # Test drawing from an empty deck
        deck = Deck()
        while deck.Cards:
            deck.draw()
        self.assertIsNone(deck.draw())  # Drawing from an empty deck should return None

    def test_multiple_deck_creation(self):
        # Test creating multiple decks and verify the number of cards
        multiple_decks = [Deck() for _ in range(5)]
        total_cards = sum(len(deck.Cards) for deck in multiple_decks)
        self.assertEqual(total_cards, 52 * 5)  # Check the total cards across multiple decks

if __name__ == '__main__':
    unittest.main()