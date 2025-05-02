class Wallet:
    def __init__(self, balance, cards, photo):
        self.balance = balance    
        self._cards = cards      
        self.__photo = photo  

    @property
    def g_cards(self):
        return self._cards

    @g_cards.setter
    def g_cards(self, cards):
        if cards >= 1:
            self._cards = cards
        else:
            print("no cards")

    @property
    def g_photo(self):
        return self.__photo

    @g_photo.setter
    def g_photo(self, photo):
        if photo >= 1:
            self.__photo = photo
        else:
            print("no photo")

w = Wallet(2000, 3, 1)

print(w.balance)   
print(w.g_cards)    
print(w.g_photo) 