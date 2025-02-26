import random

class kutya:
    def __init__(self, nev, eletkor, nem):
        self.nev = input("Adja meg a kutya nevét")
        self.eletkor = random.randint(1, 14)
        self.nem = random.choice([Hím, Nőstény])
        
        
    
    def adatok(self):
        return f"Név: {self.nev}, Életkor: {self.eletkor} év, Nem: {self.nem}"
    