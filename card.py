class Card:
    def __init__(self, m, n):
        """[カード]
        Args:
            m ([int]): [マーク]
            n ([int]): [名前]
        """
        self.mark = m
        self.name = n

    def __lt__(self, c2):
        if self.mark == 'rock' and c2.mark == 'paper':
            return True
        elif self.mark == 'scissors' and c2.mark == 'rock':
            return True
        elif self.mark == 'paper' and c2.mark == 'scissors':
            return True
        else:
            return False

    def __gt__(self, c2):
        if self.mark == 'rock' and c2.mark == 'scissors':
            return True
        elif self.mark == 'scissors' and c2.mark == 'paper':
            return True
        elif self.mark == 'paper' and c2.mark == 'rock':
            return True
        else:
            return False

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

    def decide(self, card_number=''):
        # 数字でカードを指定
        while True:
            try:
                if card_number == '':
                    card_number = input("カードを決めてください（数値選択）: ")
                card_number = int(card_number)
                if 0 <= card_number and card_number < len(self.cards):
                    break
                else:
                    print("カードが存在しません")
                    card_number=''
            except ValueError:
                print("数値で入力してください")
                card_number=''
        return self.cards.pop(card_number)
