from random import randint
from player import Player

class Game:
    def __init__(self):
        #自分を設定
        name1 = input("プレーヤー1　名前: ")
        self.p1 = Player(name1)
        self.print_remaining_card(self.p1)
        #相手を設定
        self.p2 = Player("ライバル")
        #ゲーム回数を設定
        self.max_game_count = 2

    def print_decided_card(self, p1, p2):
        d = "{} は {}、 {} は {} を出しました"
        print(d.format(p1.name, p1.card.name, p2.name, p2.card.name))

    def print_winner(self, winner=None):
        if winner is None:
            print("このターンは 引き分け です")
        else:
            w = "このターンは {} の勝ちです"
            print(w.format(winner.name))

    def print_remaining_card(self, p):
        cards_str_list = []
        for i, card in enumerate(p.deck.cards):
            cards_str_list.append( "{}: {}".format(i, card.name))
        d = "{} のカードは【 {} 】です"
        print(d.format(p.name, ",　".join(cards_str_list)))

    def print_results(self, p1, p2):
        results = ''
        w = "{} の勝利です！"
        if p1.wins > p2.wins:
            results = w.format(p1.name)
        elif p1.wins < p2.wins:
            results = w.format(p2.name)
        else:
            results = "引き分け！"
        print(results)

    def play_game(self):
        print("\n-----【邪権　開始】------------------------------------------------------------\n")
        game_count = 1
        while game_count <= self.max_game_count:
            print("\n-----【" + str(game_count) + "回戦】-----------------------------------------------------------------\n")

            #カードを決める
            self.p1.card = self.p1.deck.decide()
            self.p2.card = self.p2.deck.decide(randint(0, len(self.p2.deck.cards)))

            #勝負
            print("\n-----【勝負】-----------------------------------------------------------------\n")
            self.print_decided_card(self.p1, self.p2)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.print_winner(self.p1)
            elif self.p1.card < self.p2.card:
                self.p2.wins += 1
                self.print_winner(self.p2)
            else:
                self.print_winner()

            if game_count == self.max_game_count:
                break
            else:
                #お互いのカード確認
                print("\n-----【残りカード】------------------------------------------------------------\n")
                self.print_remaining_card(self.p1)
                self.print_remaining_card(self.p2)
                game_count += 1
        print("\n-----【結果】------------------------------------------------------------\n")
        self.print_results(self.p1, self.p2)
        print("\n-----【邪権　終了】------------------------------------------------------------\n")