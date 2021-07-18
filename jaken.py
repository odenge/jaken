from random import randint

class Card:
    def __init__(self, m, n):
        """[カード]
        Args:
            m ([int]): [マーク]
            n ([int]): [名前]
        """
        self.mark = m
        self.name = n

class Deck:
    def __init__(self):
        self.cards = []
        cards_setting = {
            "rock": "グー",
            "scissors": "チョキ",
            "paper": "パー",
        }
        for mark, name in cards_setting.items():
            self.cards.append(Card(mark, name))

    def decide(self, input_card_number=0):
        card_number = int(input_card_number)
        while card_number < 0 or len(self.cards) <= card_number:
            input_card_number = input("カードが存在しません。再度、決めてください。: ")
            card_number = int(input_card_number)
        return self.cards.pop(card_number)

class Player:
    def __init__(self, name):
        self.wins = 0
        self.deck = Deck()
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        #自分を設定
        name1 = input("プレーヤー1　名前: ")
        self.p1 = Player(name1)
        self.print_remaining_card(self.p1)
        #相手を設定
        self.p2 = Player("ライバル")

    def print_decided_card(self, p1, p2):
        d = "{} は {}、 {} は {} を出しました"
        print(d.format(p1.name, p1.card.name, p2.name, p2.card.name))

    def print_remaining_card(self, p):
        cards_str_list = []
        for i, card in enumerate(p.deck.cards):
            cards_str_list.append( "{}: {}".format(i, card.name))
        d = "{} のカードは【 {} 】です"
        print(d.format(p.name, ",　".join(cards_str_list)))

    def play_game(self):
        print("\n-----【邪権　開始】------------------------------------------------------------\n")

        #カードを決める
        card_number = input("カードを決めてください（数値選択）: ")
        self.p1.card = self.p1.deck.decide(card_number)
        self.p2.card = self.p2.deck.decide(randint(0, len(self.p2.deck.cards)))

        #勝負
        print("\n-----【勝負】-----------------------------------------------------------------\n")
        self.print_decided_card(self.p1, self.p2)

        #お互いのカード確認
        print("\n-----【残りカード】------------------------------------------------------------\n")
        self.print_remaining_card(self.p1)
        self.print_remaining_card(self.p2)

game = Game()
game.play_game()
