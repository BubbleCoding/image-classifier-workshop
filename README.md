# Bouw je eigen beeldclassifier

*English version: [README.en.md](README.en.md)*

Een les van 2,5 uur: kies je eigen klassen, verzamel je eigen
trainingsafbeeldingen, en train een echte beeldclassifier met transfer
learning — dezelfde techniek die Teachable Machine achter de schermen
gebruikt, alleen zie je deze keer elke stap.

## Als je geen Google-account hebt

Colab heeft een **Google-account** nodig om iets uit te voeren, maar dat
betekent niet per se een nieuw Gmail-adres — tijdens het aanmaken van een
Google-account is er een optie "gebruik in plaats daarvan mijn huidige
e-mailadres", waarmee je een Google-account koppelt aan een bestaand
e-mailadres, ook een schoolaccount via Microsoft.

1. Ga naar [accounts.google.com](https://accounts.google.com) → Account
   aanmaken.
2. Kies "gebruik in plaats daarvan mijn huidige e-mailadres" en vul je
   schoolmail in.
3. Verifieer het (er wordt een code naar dat adres gemaild) en stel een
   wachtwoord in.
4. Check of het werkt: open
   [colab.research.google.com](https://colab.research.google.com) en
   controleer of je bent ingelogd.

## Aan de slag

1. Open `image_classifier_workshop_nl.ipynb` in
   [Google Colab](https://colab.research.google.com) (Bestand → Notebook
   uploaden, of open het direct vanaf GitHub als je instructeur een link
   deelde).
2. Voer de cellen van boven naar beneden uit. Markdown-cellen leggen uit wat
   er gebeurt en waarom bij elke stap — lees ze, niet alleen klikken en
   overslaan. Sommige codecellen hebben een `___` of een `TODO`-commentaar
   waar je zelf iets moet invullen voordat die cel werkt — dat is expres,
   geen typefout.
3. Je past vroeg in het notebook precies één ding zelf aan: de
   `CLASSES`-dictionary in Stap 1, waarin je kiest wat het model moet leren
   herkennen.
4. Stap 9 is een opdracht, geen leesstuk: je bedenkt je eigen idee, bouwt het
   notebook daarvoor om, en laat het aan de klas zien.

Geen installaties op je eigen laptop nodig — alles draait in de browser.

**Let op:** de afbeeldingenzoekopdracht geeft soms minder resultaten terug
dan je vraagt (het hangt af van hoe veelvoorkomend je zoekterm is) — 30-40
afbeeldingen per klasse in plaats van 100 is normaal en nog steeds ruim
genoeg om op te trainen.
