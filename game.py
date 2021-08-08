from random import randint
from time import sleep
from player import Player

class Game:
    def __init__(self):
        #ゲーム回数を設定
        self.max_game_count = 3
        self.print_message("邪権　開始（{}回勝負）".format(self.max_game_count), 1)
        #自分を設定
        name1 = input("プレーヤー1　名前: ")
        self.p1 = Player(name1)
        self.print_remaining_card(self.p1)
        #相手を設定
        self.p2 = Player("ライバル", randint(1, 3))

    def print_message(self, message, format=0, sleep_time=0, end_newline_number=None, start_newline_number=None):
        sleep(sleep_time)
        if format == 1:
            f = "{}-----【{}】------------------------------------------------------------{}"
            f_start_newline_number = 1
            f_end_newline_number = 1
        elif format == 2:
            f = """{}■■■■■■■■■■■■■■
     {}
■■■■■■■■■■■■■■{}"""
            f_start_newline_number = 0
            f_end_newline_number = 1
        elif format == 3:
            f = "{}「{}」{}"
            f_start_newline_number = 0
            f_end_newline_number = 1
        else:
            f = "{}{}{}"
            f_start_newline_number = 0
            f_end_newline_number = 0

        if start_newline_number is not None:
            f_start_newline_number = start_newline_number
        start_newline = "\n" * f_start_newline_number

        if end_newline_number is not None:
            f_end_newline_number = end_newline_number
        end_newline = "\n" * f_end_newline_number

        print(f.format(start_newline, message, end_newline))

    def print_decided_card(self, p1, p2):
        d = "{} は {}、 {} は {} を出しました"
        self.print_message(d.format(p1.name, p1.card.name, p2.name, p2.card.name), 0, 1)

    def print_winner(self, winner=None):
        if winner is None:
            message = "このターンは 引き分け です"
        else:
            message = "このターンは {} の勝ちです".format(winner.name)
        self.print_message(message, 0, 1.5)

    def print_remaining_card(self, p):
        cards_str_list = []
        for i, card in enumerate(p.deck.cards):
            cards_str_list.append( "{}: {}".format(i, card.name))
        d = "{} のカードは【 {} 】です"
        self.print_message(d.format(p.name, ",　".join(cards_str_list)))

    def print_results(self, p1, p2):
        results = ""
        results_game = ""
        w = "{} の勝利です！"
        if p1.wins > p2.wins:
            results = w.format(p1.name)
            results_game = "WIN"
        elif p1.wins < p2.wins:
            results = w.format(p2.name)
            results_game = "LOSE"
        else:
            results = "引き分け！"
        if results_game != "":
            self.print_message(results_game, 2, 2)
        self.print_message(results, 0)

    def play(self):
        game_count = 1
        game_count_print_sleep_time = 1
        while game_count <= self.max_game_count:
            if 1 < game_count:
                game_count_print_sleep_time = 2
            self.print_message("{}回戦".format(game_count), 1, game_count_print_sleep_time)

            """[カードを決める]
            ライバルはプレイヤーの現在の手持ちカードを確認し、出すカードを決める
            プレイヤーはライバルの後にカードを決める（先に決めると、decideメソッドで自分のカードが減った状態を確認し、ライバルがカードを決める事になる為）
            """
            self.p2.card = self.p2.deck.decide(self.p2.get_number_decided_p2(self.p1.deck.cards))
            self.print_message("ライバルがカードを決めました", 0, 1, 1)
            self.p1.card = self.p1.deck.decide()

            #勝負
            self.print_message("勝負", 1)
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
                self.print_message("残りカード", 1, 1.5)
                self.print_remaining_card(self.p1)
                self.print_remaining_card(self.p2)
                game_count += 1
        self.print_message("結果", 1)
        self.print_results(self.p1, self.p2)
        self.print_message("邪権　終了", 1)
