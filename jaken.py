from random import shuffle

class Deck:
    def __init__(self):
        self.cards = {
            "rock": "グー",
            "scissors": "チョキ",
            "paper": "パー",
        }

    def decide(self, card=""):
        #cardの指定がある時には、指定されたカードを選択
        if card:
            while card not in self.cards:
                card = input("カードが存在しません。再度、決めてください。: ")
            return self.cards.pop(card)
        else:
            #コンピューターの時には、ランダムに修正していく（今はカード指定にしている）
            return self.cards.pop("scissors")

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
        print(d.format(p1.name, p1.card, p2.name, p2.card))

    def print_remaining_card(self, p):
        d = "{} のカードは {} です"
        print(d.format(p.name, p.deck.cards))

    def play_game(self):
        print("\n-----【邪権　開始】------------------------------------------------------------\n")

        #カードを決める
        decided_card = input("カードを決めてください: ")
        self.p1.card = self.p1.deck.decide(decided_card)
        self.p2.card = self.p2.deck.decide()

        #勝負
        print("\n-----【勝負】-----------------------------------------------------------------\n")
        self.print_decided_card(self.p1, self.p2)

        #お互いのカード確認
        print("\n-----【残りカード】------------------------------------------------------------\n")
        self.print_remaining_card(self.p1)
        self.print_remaining_card(self.p2)

game = Game()
game.play_game()
