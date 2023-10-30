import unittest

class Card:
    def __init__(self, suit, value):
        if not isinstance(suit, str):
            raise TypeError("Suit must be a string")
        if not isinstance(value, str):
            raise TypeError("Vlue must be a string")
        self.suit = suit
        self.value = value


"""Test for Card class"""
import unittest

class test_Card(unittest.TestCase):

    def test_card_creation(self):
        # Test creating a card with valid suit and value
        card = Card("Hearts", "Ace")
        self.assertEqual(card.suit, "Hearts")
        self.assertEqual(card.value, "Ace")

    def test_invalid_suit(self):
        # Test creating a card with an invalid suit
        with self.assertRaises(TypeError):
            Card(123, "Ace")  # Trying to create a card with an integer as the suit

    def test_invalid_value(self):
        # Test creating a card with an invalid value
        with self.assertRaises(TypeError):
            Card("Spades", 5)  # Trying to create a card with an integer as the value

    def test_suit_and_value_types(self):
        # Test creating a card with different suit and value types
        with self.assertRaises(TypeError):
            Card(5, 5)  # Trying to create a card with integer suit and value

    def test_suit_value_no_string(self):
        # Test creating a card with empty string suit and value
        with self.assertRaises(ValueError):
            Card("", "Ace")  # Trying to create a card with an empty string as the suit
    
    def test_suit_no_value_strings(self):
        # Test creating a card with suit and empty value
        with self.assertRaises(ValueError):
            Card("Spades", )  # Trying to create a card with an empty value a

if __name__ == '__main__':
    unittest.main()
