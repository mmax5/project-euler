__author__ = 'mikemax'
"""
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

How many hands does Player 1 win?

"""

class Card():
    r_lookup = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    }

    def __init__(self, suit, rank):
        self.suit = suit
        if rank in self.r_lookup:
            rank = self.r_lookup[rank]
        else:
            rank = int(rank)
        self.rank = rank

    def __repr__(self):
        return '%s%d' % (self.suit, self.rank)

class Hand():
    def __init__(self, cards):
        self.cards = cards

    def high_card(self):
        return max([c.rank for c in self.cards])

    def one_pair(self):
        s = self._cards_as_set()
        for c, count in s.iteritems():
            if count == 2:
                return c
        return 0

    def two_pair(self):
        s = self._cards_as_set()
        pairs = set()
        for c, count in s.iteritems():
            if count == 2:
                pairs.add(c)
        if len(pairs) == 2:
            return max(pairs)
        return 0

    def three_of_kind(self):
        s = self._cards_as_set()
        for c, count in s.iteritems():
            if count == 3:
                return c
        return 0

    def straight(self):
        ranks = [c.rank for c in self.cards]
        sorted(ranks)
        for i in range(ranks[0], ranks[0] + 5):
            if i not in ranks:
                return 0
        return ranks[4]

    def flush(self):
        suits = [c.suit for c in self.cards]
        if len(set(suits)) == 1:
            return self.high_card()
        return 0

    def full_house(self):
        if self.three_of_kind() and self.one_pair():
            # pack full house output into one number that can be compared
            return self.three_of_kind() << 4 + self.one_pair()
        return 0

    def four_of_kind(self):
        s = self._cards_as_set()
        for c, count in s.iteritems():
            if count == 4:
                return c
        return 0

    def straight_flush(self):
        if self.straight() and self.flush():
            return self.straight()
        return 0

    def _cards_as_set(self):
        s = {}
        for c in self.cards:
            if c.rank in s:
                s[c.rank] += 1
            else:
                s[c.rank] = 1
        return s

    def compare(self, hand2):
        s_f = self.straight_flush() - hand2.straight_flush()
        if s_f:
            return s_f

        f_of_kind = self.four_of_kind() - hand2.four_of_kind()
        if f_of_kind:
            return f_of_kind

        f_house = self.full_house() - hand2.full_house()
        if f_house:
            return f_house

        flush = self.flush() - hand2.flush()
        if flush:
            return flush
        if self.flush():
            print 'tie'

        straight = self.straight() - hand2.straight()
        if straight:
            return straight
        if self.straight():
            print 'tie'

        three_of_kind = self.three_of_kind() - hand2.three_of_kind()

        if three_of_kind:
            return three_of_kind
        if self.three_of_kind():
            print 'tie'

        two_pair = self.two_pair() - hand2.two_pair()
        if two_pair:
            return two_pair
        if self.two_pair():
            print 'tie'



        one_pair = self.one_pair() - hand2.one_pair()
        if one_pair:
            return one_pair
        if self.one_pair():
            print 'Tie one_pair'

        h = self.high_card() - hand2.high_card()
        if h:
            return h
        else:
            raise Exception(
                "Something went wrong %r, %r"
                % (
                    ','.join('%r' % c for c in self.cards),
                    ','.join('%r' % c for c in hand2.cards)
                )
            )



def main():
    hand_data = open('p054_poker.txt').read(-1)

    wins = 0
    for row in hand_data.split('\n'):
        print row
        if len(row) < 1:
            continue
        cards_text = row.split(" ")
        cards = []
        for c_text in cards_text:
            suit = c_text[1]
            rank = c_text[0]
            c = Card(suit, rank)
            cards.append(c)
        print cards[:5], cards[5:]
        p1_hand = Hand(cards[:5])
        p2_hand = Hand(cards[5:])
        if p1_hand.compare(p2_hand) >= 0:
            print 'p1 wins'
            wins += 1
        else:
            print 'p2 wins'
    print wins

if __name__ == "__main__":
    main()