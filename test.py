class Ksiazka:
    tytul = ""
    liczba_stron = 0
    autor = ""
    liczba_rozdzialow = 0

    def opisz(self):
        print(f"To jest {self.tytul}, napisana przez {self.autor}. Ma {self.liczba_stron} stron, które są podzielone na {self.liczba_rozdzialow} rozdzialów")

    def __repr__(self):
        return f'<Książka z tytułem: {self.tytul}>'

pt = Ksiazka()
pt.tytul = "Pan Tadeusz"
pt.autor = "Adam Mickiewicz"
pt.liczba_stron = 600
pt.liczba_rozdzialow = 15

om = Ksiazka()
om.tytul = "Ogniem i Mieczem"
om.autor = "Henryk Sienkiewicz"
om.liczba_stron = 450
om.liczba_rozdzialow = 10

pt.opisz()
om.opisz()

print(pt)
print(om)