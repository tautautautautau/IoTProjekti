# IoT-ohjelmointi projekti

## Pelihallin koripallopeli

Arduinolla ja Raspberry Pi:lla toteutettu "koripallopeli", jossa pelaaja heittää palloa koriin ja kerää pisteitä.
Pisteet näkyy LCD-näytöllä ja graafisessa käyttöliittymässä.
Käyttöliittymässä on myöskin pistetilasto ja napit pelin ohjaamiseen.

[Suuntaa antava TinkerCAD virtapiiri](https://www.tinkercad.com/things/4R87mIRfiRz-iot-projekti?sharecode=Ea1lM735HB9TrEcFXiUK6mqv-xxSH20Ct1si783S-Xo)

![Kuva virtapiiristä](https://github.com/tautautautautau/IoTProjekti/blob/main/Circuit.png)

### Komponentit
1. Raspberry Pi 3B+
2. Arduino Uno (SparkFun RedBoard)
3. HC-SR04 ultraäänianturi
4. RGB Ledi
5. Nappi
6. 3x 330 ohm vastus
7. 1x 10k ohm vastus
8. LCD (2x16)
9. Pietsosummeri

***

## Tiedostojen kuvaus
**[KoripalloGUI.py](KoripalloGUI.py):**
Python skripti koripallopelin käyttöliittymälle, joka käyttää "tkinter" ja "serial" -kirjastoja käyttöliittymän näyttämiseen ja Arduinon kanssa kommunikointiin. Käyttöliittymä näyttää nykyisen pistemäärän, korkeimman pistemäärän ja tämän ajon aiempien pelien pistemäärät.
Käyttöliittymässä on painikkeet pistemäärän kasvattamiseen ja nollaamiseen. Nollauksen yhteydessä käyttäjältä kysytään hänen nimeään pistelistaan, päivitetään korkein pistemäärä ja nollataan nykyinen pistemäärä. Korkein pistemäärä tallennetaan tiedostoon, josta se myös ladataan käynnistyksen yhteydessä.
Käyttöliittymä keskustelee Arduinon kanssa sarjayhteyden avulla. Jos skripti havaitsee pistemäärän päivittyvän nollaan, suoritetaan nollaus-funktio. Muussa tapauksessa se jatkaa pistemäärän kasvattamista, kun Arduinolta tulee uusi pistemäärä.
Skripti myöskin lähettää Arduinolle päivitettyä pistemäärää, kun painetaan pisteen lisäys nappia käyttöliittymästä.

**[IoTKoripallo.ino](IoTKoripallo/IoTKoripallo.ino):**
Arduino skripti, joka ohjaa ultraääni anturia, nappia, RGB lediä, pietsosummeria ja LCD-näyttöä.
Skripti lukee sarjayhteydestä komentoja, joilla voidaan kasvattaa tai nollata pistemäärä.
Jos ultraääni anturi havaitsee esineen, tässä tapauksessa pallon, kasvatetaan pistemäärää yhdellä ja soitetaan pietsosummeria. Pallon havaitsemisen jälkeen odotetaan kaksi sekuntia, jotta vältytään pistetilanteen muuttamiselta useasti yhdellä heitto kerralla.
Pistetilanteen muuttuessa päivitetään pistemäärä LCD-näytölle.
RGB ledi näyttää skriptin tilan. Oranssina pallo ei ole korissa. Vihreänä pallo on korissa. Pistetilanteen nollautuessa valo on punainen.

**[hiscore](hiscore):**
Tekstitiedosto joka pitää sisällään korkeimman pistetilanteen ja pelaajan nimen.
***
