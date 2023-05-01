import random


class Cards:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value}{self.suit}")


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["♠", "♥", "♦", "♣"]:
            for v in ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]:
                self.cards.append(Cards(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()


class ThreeCardPoker(Deck, Player):
    def __init__(self):
        super().__init__()
        self.cards = []
        self.build()
        self.shuffle()
        self.dealer_hand = []
        self.player_hand = []

    def get_dealer_hand(self):
        for _ in range(3):
            self.dealer_hand.append(self.draw_card())
        return self.dealer_hand

    def get_player_hand(self):
        for _ in range(3):
            self.player_hand.append(self.draw_card())
        return self.player_hand

    def convert_card_value(self):
        for card in self.hand:
            if card.value == "A":
                card.value = 14
            elif card.value == "K":
                card.value = 13
            elif card.value == "Q":
                card.value = 12
            elif card.value == "J":
                card.value = 11
            else:
                card.value = int(card.value)

    def revert_card_value(self):
        for card in self.hand:
            if card.value == 14:
                card.value = "A"
            elif card.value == 13:
                card.value = "K"
            elif card.value == 12:
                card.value = "Q"
            elif card.value == 11:
                card.value = "J"
            else:
                card.value = str(card.value)

    def rank_three_card_poker_hand(self):
        hand_rank = ""
        # Show the cards in the player's hand

        # for card in self.player_hand:
        #     card.show()

        # Convert the card values to integers

        for card in self.player_hand:
            if card.value == "A":
                card.value = 14
            elif card.value == "K":
                card.value = 13
            elif card.value == "Q":
                card.value = 12
            elif card.value == "J":
                card.value = 11
            else:
                card.value = int(card.value)

        # Initialize variables to count the number of each suit and rank
        suits = {}
        ranks = {}

        # Iterate over the cards and count the number of each suit and rank
        for card in self.player_hand:
            suit = card.suit
            rank = card.value
            suits[suit] = suits.get(suit, 0) + 1
            ranks[rank] = ranks.get(rank, 0) + 1

        # Check for a flush (all cards have the same suit)
        if len(suits) == 1:
            # Check for a straight flush (cards are in sequence)
            if len(ranks) == 3 and max(ranks.keys()) - min(ranks.keys()) == 2:
                hand_rank = "Straight flush"
            else:
                hand_rank = "Flush"

        # Check for a straight (cards are in sequence)
        elif len(ranks) == 3 and max(ranks.keys()) - min(ranks.keys()) == 2:
            hand_rank = "Straight"

        # Check for three of a kind
        elif len(ranks) == 1:
            hand_rank = "Three of a kind"

        # Check for a pair
        elif len(ranks) == 2:
            hand_rank = "Pair"

        # If no other ranking was found, the hand is a high card
        else:
            hand_rank = "High card"

        return [hand_rank, self.player_hand]



    def rank_three_card_poker_dealer_hand(self):
        dealer_hand_rank = ""
        # Show the cards in the player's hand

        for card in self.dealer_hand:
            card.show()

        # Convert the card values to integers

        for card in self.dealer_hand:
            if card.value == "A":
                card.value = 14
            elif card.value == "K":
                card.value = 13
            elif card.value == "Q":
                card.value = 12
            elif card.value == "J":
                card.value = 11
            else:
                card.value = int(card.value)

        # Initialize variables to count the number of each suit and rank
        suits = {}
        ranks = {}

        # Iterate over the cards and count the number of each suit and rank
        for card in self.dealer_hand:
            suit = card.suit
            rank = card.value
            suits[suit] = suits.get(suit, 0) + 1
            ranks[rank] = ranks.get(rank, 0) + 1

        # Check for a flush (all cards have the same suit)
        if len(suits) == 1:
            # Check for a straight flush (cards are in sequence)
            if len(ranks) == 3 and max(ranks.keys()) - min(ranks.keys()) == 2:
                dealer_hand_rank = "Straight flush"
            else:
                dealer_hand_rank = "Flush"

        # Check for a straight (cards are in sequence)
        elif len(ranks) == 3 and max(ranks.keys()) - min(ranks.keys()) == 2:
            dealer_hand_rank = "Straight"

        # Check for three of a kind
        elif len(ranks) == 1:
            dealer_hand_rank = "Three of a kind"

        # Check for a pair
        elif len(ranks) == 2:
            dealer_hand_rank = "Pair"

        # If no other ranking was found, the hand is a high card
        else:
            dealer_hand_rank = "High card"

        return [dealer_hand_rank, self.dealer_hand]

    def compare_hands(self):
        self.rank_three_card_poker_hand()
        self.rank_three_card_poker_dealer_hand()

        # Check for straight flush
        if self.rank_three_card_poker_hand()[0] == "Straight flush" and self.rank_three_card_poker_dealer_hand()[0] == "Straight flush":
            if max(self.rank_three_card_poker_hand()[1]) > max(self.rank_three_card_poker_dealer_hand()[1]) and min(self.rank_three_card_poker_hand()[1]) > min(self.rank_three_card_poker_dealer_hand()[1]):
                return f"Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]} beats Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]}"
            elif max(self.rank_three_card_poker_hand()[1]) < max(self.rank_three_card_poker_dealer_hand()[1]) and min(self.rank_three_card_poker_hand()[1]) < min(self.rank_three_card_poker_dealer_hand()[1]):
                return f"Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]} beats Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]}"
            else:
                return "Push"
        elif self.rank_three_card_poker_hand()[0] == "Straight flush" and self.rank_three_card_poker_dealer_hand() != "Straight flush":
            return f"Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]} beats Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]}"
        elif self.rank_three_card_poker_hand()[0] != "Straight flush" and self.rank_three_card_poker_dealer_hand() == "Straight flush":
            return f"Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]} beats Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]}"

        # Check for three of a kind
        elif self.rank_three_card_poker_hand()[0] == "Three of a kind" and self.rank_three_card_poker_dealer_hand()[0] == "Three of a kind":
            if max(self.rank_three_card_poker_hand()[1]) > max(self.rank_three_card_poker_dealer_hand()[1]) and min(self.rank_three_card_poker_hand()[1]) > min(self.rank_three_card_poker_dealer_hand()[1]):
                return f"Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]} beats Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]}"
            elif max(self.rank_three_card_poker_hand()[1]) < max(self.rank_three_card_poker_dealer_hand()[1]) and min(self.rank_three_card_poker_hand()[1]) < min(self.rank_three_card_poker_dealer_hand()[1]):
                return f"Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]} beats Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]}"
            else:
                return "Push"
        elif self.rank_three_card_poker_hand()[0] == "Three of a kind" and self.rank_three_card_poker_dealer_hand() != "Three of a kind" and self.rank_three_card_poker_dealer_hand()[0] != "Straight flush":
            return f"Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]} beats Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]}"
        elif self.rank_three_card_poker_hand()[0] != "Three of a kind" and self.rank_three_card_poker_hand() != "Straight flush" and self.rank_three_card_poker_dealer_hand() == "Three of a kind":
            return f"Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]} beats Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]}"

        # Check for straight
        elif self.rank_three_card_poker_hand()[0] == "Straight" and self.rank_three_card_poker_dealer_hand()[0] == "Straight":
            if max(self.rank_three_card_poker_hand()[1]) > max(self.rank_three_card_poker_dealer_hand()[1]) and min(self.rank_three_card_poker_hand()[1]) > min(self.rank_three_card_poker_dealer_hand()[1]):
                return f"Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]} beats Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]}"
            elif max(self.rank_three_card_poker_hand()[1]) < max(self.rank_three_card_poker_dealer_hand()[1]) and min(self.rank_three_card_poker_hand()[1]) < min(self.rank_three_card_poker_dealer_hand()[1]):
                return f"Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]} beats Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]}"
            else:
                return "Push"
        elif self.rank_three_card_poker_hand()[0] == "Straight" and self.rank_three_card_poker_dealer_hand() != "Straight" and self.rank_three_card_poker_dealer_hand()[0] != "Three of a kind" and self.rank_three_card_poker_dealer_hand()[0] != "Straight flush":
            return f"Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]} beats Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]}"
        elif self.rank_three_card_poker_hand()[0] != "Straight" and self.rank_three_card_poker_dealer_hand() == "Straight" and self.rank_three_card_poker_hand()[0] != "Three of a kind" and self.rank_three_card_poker_hand()[0] != "Straight flush":
            return f"Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]} beats Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]}"

        # Check for flush
        elif self.rank_three_card_poker_hand()[0] == "Flush" and self.rank_three_card_poker_dealer_hand()[0] == "Flush":
            if max(self.rank_three_card_poker_hand()[1]) > max(self.rank_three_card_poker_dealer_hand()[1]):
                return f"Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]} beats Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]}"
            elif max(self.rank_three_card_poker_hand()[1]) < max(self.rank_three_card_poker_dealer_hand()[1]):
                return f"Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]} beats Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]}"
            elif max(self.rank_three_card_poker_hand()[1]) == max(self.rank_three_card_poker_dealer_hand()[1]):
                if sorted(self.rank_three_card_poker_hand()[1])[1] > sorted(self.rank_three_card_poker_dealer_hand()[1])[1]:
                    return f"Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]} beats Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]}"
                elif sorted(self.rank_three_card_poker_hand()[1])[1] < sorted(self.rank_three_card_poker_dealer_hand()[1])[1]:
                    return f"Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]} beats Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]}"
                elif sorted(self.rank_three_card_poker_hand()[1])[1] == sorted(self.rank_three_card_poker_dealer_hand()[1])[1]:
                    if min(self.rank_three_card_poker_hand()[1]) > min(self.rank_three_card_poker_dealer_hand()[1]):
                        return f"Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]} beats Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]}"
                    elif min(self.rank_three_card_poker_hand()[1]) < min(self.rank_three_card_poker_dealer_hand()[1]):
                        return f"Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]} beats Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]}"
                    else:
                        return "Push"
        elif self.rank_three_card_poker_hand()[0] == "Flush" and self.rank_three_card_poker_dealer_hand()[0] != "Flush" and self.rank_three_card_poker_dealer_hand()[0] != "Straight flush" and self.rank_three_card_poker_dealer_hand()[0] != "Three of a kind" and self.rank_three_card_poker_dealer_hand()[0] != "Straight":
            return f"Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]} beats Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]}"
        elif self.rank_three_card_poker_hand()[0] != "Flush" and self.rank_three_card_poker_dealer_hand()[0] == "Flush" and self.rank_three_card_poker_hand()[0] != "Straight flush" and self.rank_three_card_poker_hand()[0] != "Three of a kind" and self.rank_three_card_poker_hand()[0] != "Straight":
            return f"Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]} beats Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]}"

        # Check for pair
        elif self.rank_three_card_poker_hand()[0] == "Pair" and self.rank_three_card_poker_dealer_hand()[0] == "Pair":
            pass

        # Check for high card
        elif self.rank_three_card_poker_hand()[0] == "High card" and self.rank_three_card_poker_dealer_hand()[0] == "High card":
            if max(self.rank_three_card_poker_hand()[1]) > max(self.rank_three_card_poker_dealer_hand()[1]):
                return f"Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]} beats Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]}"
            elif max(self.rank_three_card_poker_hand()[1]) < max(self.rank_three_card_poker_dealer_hand()[1]):
                return f"Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]} beats Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]}"
            elif max(self.rank_three_card_poker_hand()[1]) == max(self.rank_three_card_poker_dealer_hand()[1]):
                if sorted(self.rank_three_card_poker_hand()[1])[1] > sorted(self.rank_three_card_poker_dealer_hand()[1])[1]:
                    return f"Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]} beats Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]}"
                elif sorted(self.rank_three_card_poker_hand()[1])[1] < sorted(self.rank_three_card_poker_dealer_hand()[1])[1]:
                    return f"Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]} beats Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]}"
                elif sorted(self.rank_three_card_poker_hand()[1])[1] == sorted(self.rank_three_card_poker_dealer_hand()[1])[1]:
                    if min(self.rank_three_card_poker_hand()[1]) > min(self.rank_three_card_poker_dealer_hand()[1]):
                        return f"Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]} beats Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]}"
                    elif min(self.rank_three_card_poker_hand()[1]) < min(self.rank_three_card_poker_dealer_hand()[1]):
                        return f"Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]} beats Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]}"
                    else:
                        return "Push"
        elif self.rank_three_card_poker_hand()[0] == "High card" and self.rank_three_card_poker_dealer_hand()[0] != "High card" and self.rank_three_card_poker_dealer_hand()[0] != "Pair" and self.rank_three_card_poker_dealer_hand()[0] != "Flush" and self.rank_three_card_poker_dealer_hand()[0] != "Straight flush" and self.rank_three_card_poker_dealer_hand()[0] != "Three of a kind" and self.rank_three_card_poker_dealer_hand()[0] != "Straight":
            return f"Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]} beats Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]}"
        elif self.rank_three_card_poker_hand()[0] != "High card" and self.rank_three_card_poker_dealer_hand()[0] == "High card" and self.rank_three_card_poker_hand()[0] != "Pair" and self.rank_three_card_poker_hand()[0] != "Flush" and self.rank_three_card_poker_hand()[0] != "Straight flush" and self.rank_three_card_poker_hand()[0] != "Three of a kind" and self.rank_three_card_poker_hand()[0] != "Straight":
            return f"Dealer hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_dealer_hand()[1]} beats Player hand: {self.rank_three_card_poker_dealer_hand()[0]}{self.rank_three_card_poker_hand()[1]}"




if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()

    bob = Player("Bob")
    bob.draw(deck)
    print()
    game = ThreeCardPoker()
    print("-----------------")
    game.get_player_hand()
    print("-----------------")
    game.get_dealer_hand()
    print("-----------------")
    print(game.compare_hands())




