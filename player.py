from random import choice,randint
from card import Deck

class Player:
    def __init__(self, name, personality=0):
        self.wins = 0
        self.deck = Deck()
        self.card = None
        self.name = name
        self.personality = personality

    #相手が自分のカードの状況を把握し、相手が決めたカードの数字を返す
    def get_number_decided_p2(self, p1_deck_cards):
        #自分が社長を持っているか相手が把握
        p1_has_president = False
        for p1_card in p1_deck_cards:
            if p1_card.mark == "president":
                p1_has_president = True
                break

        #相手が選択する数字のリスト作成
        if p1_has_president:
            number_decided_p2 = randint(0, len(self.deck.cards)-1)
        else:
            #自分が社長を持っていない時には、相手は平社員を出さない（勝つことがない為）
            p2_select_number_list = []
            for i, p2_card in enumerate(self.deck.cards):
                if p2_card.mark != "employee":
                    p2_select_number_list.append(i)
            number_decided_p2 = choice(p2_select_number_list)
        return number_decided_p2
