from abc import ABC, abstractmethod


class Dosya(ABC):
    @abstractmethod
    def oku(self) -> str:
        pass

    @abstractmethod
    def yaz(self, veri: str):
        pass

class TemelDosya(Dosya):
    def __init__(self, ad: str):
        self.ad = ad

    def oku(self) -> str:
        with open(self.ad, 'r') as f:
            return f.read()

    def yaz(self, veri: str):
        with open(self.ad, 'w') as f:
            f.write(veri)

class DosyaDecorator(Dosya):
    def __init__(self, dosya: Dosya):
        self._dosya = dosya

    def oku(self) -> str:
        return self._dosya.oku()

    def yaz(self, veri: str):
        self._dosya.yaz(veri)

import zlib
import base64

class SifrelemeDecorator(DosyaDecorator):
    def yaz(self, veri: str):
        sifreli_veri = base64.b64encode(veri.encode()).decode()
        super().yaz(sifreli_veri)

    def oku(self) -> str:
        sifreli_veri = super().oku()
        return base64.b64decode(sifreli_veri.encode()).decode()

class SikistirmaDecorator(DosyaDecorator):
    def yaz(self, veri: str):
        sikistirilmis_veri = zlib.compress(veri.encode())
        super().yaz(sikistirilmis_veri.decode('latin1'))

    def oku(self) -> str:
        sikistirilmis_veri = super().oku()
        return zlib.decompress(sikistirilmis_veri.encode('latin1')).decode()

# Kullanım
temel_dosya = TemelDosya("ornek.txt")
sifreli_dosya = SifrelemeDecorator(temel_dosya)
sikistirma_sifreli_dosya = SikistirmaDecorator(sifreli_dosya)

sikistirma_sifreli_dosya.yaz("Bu bir test verisidir.")
print(sikistirma_sifreli_dosya.oku())
