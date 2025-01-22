class Kahve:
    def __init__(self):
        self.tanim = "Sade Kahve"
        self.fiyat = 10.0

    def bilgileri_al(self):
        return f"{self.tanim} -> Fiyat: {self.fiyat} TL"


class KahveDecorator:
    def __init__(self, kahve: Kahve):
        self._kahve = kahve

    def bilgileri_al(self):
        return self._kahve.bilgileri_al()


class Sut(KahveDecorator):
    def __init__(self, kahve: Kahve):
        super().__init__(kahve)
        self.tanim = self._kahve.tanim + " + Süt"
        self.fiyat = self._kahve.fiyat + 2.5

    def bilgileri_al(self):
        return f"{self.tanim} -> Fiyat: {self.fiyat} TL"


class Seker(KahveDecorator):
    def __init__(self, kahve: Kahve):
        super().__init__(kahve)
        self.tanim = self._kahve.tanim + " + Şeker"
        self.fiyat = self._kahve.fiyat + 1.5

    def bilgileri_al(self):
        return f"{self.tanim} -> Fiyat: {self.fiyat} TL"

-
class Cikolata(KahveDecorator):
    def __init__(self, kahve: Kahve):
        super().__init__(kahve)
        self.tanim = self._kahve.tanim + " + Çikolata"
        self.fiyat = self._kahve.fiyat + 3.0

    def bilgileri_al(self):
        return f"{self.tanim} -> Fiyat: {self.fiyat} TL"

kahve = Kahve()
print(kahve.bilgileri_al())

kahve_sutlu = Sut(kahve)
print(kahve_sutlu.bilgileri_al())

kahve_sutlu_sekerli = Seker(kahve_sutlu)
print(kahve_sutlu_sekerli.bilgileri_al())

kahve_sutlu_sekerli_cikolatali = Cikolata(kahve_sutlu_sekerli)
print(kahve_sutlu_sekerli_cikolatali.bilgileri_al())
