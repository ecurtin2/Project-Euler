from collections import Counter


def split(list):
    N = len(list) // 2
    return list[:N], list[N:]

with open('054.dat') as f:
    games = [split(line.split(' ')) for line in f.read().splitlines()]


class Card(object):
    name_to_val = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    val_to_name = {v: k for k, v in name_to_val.items() if k != 'T'}
    suits = {'H': '♥', 'S': '♠', 'D': '♦', 'C': '♣'}

    def __init__(self, val, suit):
        if val in __class__.name_to_val.keys():
            self.val = __class__.name_to_val[val]
        else:
            self.val = int(val)
        self.suit = suit

    def __lt__(self, other):
        return self.val < other.val

    def __str__(self):
        if self.val in __class__.val_to_name.keys():
            name = __class__.val_to_name[self.val]
        else:
            name = str(self.val)

        return name + __class__.suits[self.suit]


class PokerHand(object):
    hand_vals = {'high': 1,
                 'one pair': 2,
                 'two pair': 3,
                 'three of a kind': 4,
                 'straight': 5,
                 'flush': 6,
                 'full house': 7,
                 'four of a kind': 8,
                 'straight flush': 9,
                 'royal flush': 10}

    def __init__(self, cards):
        self.cards = list(reversed(sorted([Card(c[0], c[1]) for c in cards])))
        self.handtype, self.hand, self.remains = self.assess_hand()

    def assess_hand(self):
        _type = self.type_of_straight_or_flush()
        if _type: # returns none if not any kind of straight or flush
            return _type, self.cards, []
        else:
            c = Counter(c.val for c in self.cards)
            vals, counts = sorted(c), [c[k] for k in sorted(c)]
            include_vals = [val for val, count in c.items() if count > 1]
            hand = [c for c in self.cards if c.val in include_vals]
            if 2 in counts:
                if len([c for c in counts if c == 2]) == 2:
                    _type = 'two pair'
                elif 3 in counts:
                    _type = 'full house'
                    triple_val = max(c, key=lambda k: c[k])
                    self.cards = sorted(self.cards, key=lambda c: abs(c.val - triple_val))
                    hand = self.cards

                else:
                    _type = 'one pair'
            elif 3 in counts:
                _type = 'three of a kind'
            elif 4 in counts:
                _type = 'four of a kind'
            else:
                _type = 'high'
                hand = [max(self.cards)]

            return _type, hand, [c for c in self.cards if c not in hand]

    def type_of_straight_or_flush(self):
        if self.is_straight():
            if self.is_flush():
                if self.cards[0].val_to_name[self.cards[0]] == 'A':
                    _type = 'royal flush'
                else:
                    _type = 'straight flush'
            else:
                _type = 'straight'
        else:
            if self.is_flush():
                _type = 'flush'
            else:
                _type = None
        return _type

    def is_straight(self):
        vals = iter(sorted(c.val for c in self.cards))
        lastval = next(vals)
        for val in vals:
            if abs(val - lastval) != 1:
                return False
            lastval = val
        return True

    def is_flush(self):
        return all(c.suit == self.cards[0].suit for c in self.cards)

    def __gt__(self, other):
        val = __class__.hand_vals[self.handtype]
        otherval = __class__.hand_vals[other.handtype]
        if val != otherval:
            return val > otherval
        else:
            if self.hand != other.hand:
                return self.hand > other.hand
            else:
                return self.remains > other.remains

    def __str__(self):
        l = ['Poker Hand with cards: '] + [' ' + str(c) for c in self.cards]
        l += ['\nHand determined to be: ' + self.handtype]
        l += ['\nWith active cards: '] + [' ' + str(c) for c in self.hand]
        if self.remains:
            l += ['\nAnd remaining: '] + [' ' + str(c) for c in self.remains]
        return ''.join(l) + '\n'


p1_wins = [PokerHand(p1) > PokerHand(p2) for p1, p2 in games]
print(sum(p1_wins))