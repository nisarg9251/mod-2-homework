import unittest
from Cards import Card, Deck, Hand

class TestCard(unittest.TestCase):
    def testCard(self):
        c1 = Card(1, "clubs")
        # tests repr
        self.assertEqual(repr(c1), "Card(1 of clubs)")
        c2 = Card(3, "spades")
        # tests ln
        self.assertEqual(c1 < c2, True)
        self.assertEqual(c2 < c1, False)
        c3 = Card(4, "clubs")
        # tests ln
        self.assertEqual(c3 < c2, True)
        self.assertEqual(c2 < c3, False)
        c4 = Card(1, "clubs")
        # tests eq
        self.assertEqual(c1 == c4, True)
        self.assertEqual(c1 == c2, False)

class TestDeck(unittest.TestCase):
    def testDeck(self):
        d1 = Deck()
        # tests len
        self.assertEqual(len(d1), 52)
        d2 = Deck([2,1],['triangles','dots'])
        # tests repr
        self.assertEqual(repr(d2), 'Deck: [Card(1 of dots), Card(2 of dots), Card(1 of triangles), Card(2 of triangles)]')

        self.assertEqual(len(d2), 4)
        x = Card(2, "triangles")
        # tests draw_top
        self.assertEqual(d2.draw_top(), x)
        x = Card(1, "triangles")
        self.assertEqual(d2.draw_top(), x)
        x = Card(2, "dots")
        self.assertEqual(d2.draw_top(), x)
        x = Card(1, "dots")
        with self.assertRaises(RuntimeError): # tests draw_top Runtime Error
            d2.draw_top()
        d3 = Deck([2,1],['triangles','dots'])
        y = repr(d3)
        d3.shuffle()
        z = repr(d3)
        self.assertEqual(y == z, False) # compare shuffled and unshuffled deck
        self.assertEqual(d3.sort(), [Card(1, "dots"), Card(2, "dots"), Card(1, "triangles"), Card(2, "triangles")])

class TestHand(unittest.TestCase):
    def testHand(self):
        h_clubs = Hand([Card(value, 'clubs') for value in range(5, 0, -1)])
        # test repr, printable representation of deck backwards
        self.assertEqual(repr(h_clubs), 'Hand: [Card(5 of clubs), Card(4 of clubs), Card(3 of clubs), Card(2 of clubs), Card(1 of clubs)]')
        # test sort, sorts deck from backwards to numeric
        self.assertEqual(h_clubs.sort(), [Card(1, "clubs"), Card(2, "clubs"), Card(3, "clubs"), Card(4, "clubs"), Card(5, "clubs")])
        # test len
        self.assertEqual(len(h_clubs), 5)
        # tests play Runtime Error if card not in hand
        self.assertEqual(str(h_clubs.play(Card(1, 'clubs'))), "Card(1 of clubs)")
        with self.assertRaises(RuntimeError):
            h_clubs.play(Card(1, 'clubs'))

if __name__ == "__main__":
    unittest.main()