# Aufgabe Wegbeschreibung

## a)
```
Stehe auf  
Gehe aus dem Raum  
Gehe in die Küche  
Öffne den Kühlschrank  
Wenn Eistee verfügbar:  
    Nimm Eistee  
    Schließe den Kühlschrank  
    Gehe aus der Küche  
Wenn Eistee nicht verfügbar:  
    Schließe den Kühlschrank  
    Gehe aus der Küche  
    Gehe zum Aufzug  
    Ruf den Aufzug  
    Fahr in das Erdgeschoss  
    Steige aus dem Aufzug aus  
    Gehe zum Getränkeautomaten  
    Wenn Eistee verfügbar:  
        Nimm Eistee  
    Wenn Eistee nicht verfügbar:  
        Nimm Cola Zero  
    Gehe zum Aufzug  
    Ruf den Aufzug  
    Fahr in das 4. Obergeschoss  
    Steige aus dem Aufzug aus  
Gehe in die Fachschaft  
Setze dich auf die Couch  
```

## b)	

Bspw. Schritt "Öffne den Kühlschrank":
- Man muss vor dem Kühlschrank stehen
- Der Kühlschrank ist ca. 2m hoch und 1m breit, hat einen Griff und eine Tür
- Ein Kühlschrank wird geöffnet, indem man an dem Griff zieht

Diese Erklärung kann länger sein, wenn man die ursprünglichen Schritte grober beschreibt.  
Z.B.: "Nehme Eistee aus dem Kühlschrank" für:
- Öffne den Kühlschrank
- Nimm Eistee
- Schließe den Kühlschrank  

Da ein Mensch weiß, dass man den Kühlschrank öffnen muss, um etwas herauszunehmen, und der Kühlschrank nach dem Herausnehmen wieder geschlossen werden muss.


# Socken

## 1)

```
Solange der Haufen nicht leer ist:
    Nehme einen Socken aus dem Haufen
    Nehme einen weiteren Socken aus dem Haufen
    Wenn beide Socken die gleiche Farbe und das gleiche Modell sind:
    - Falte beide Socken zusammen
    Ansonsten:
    - Lege beide Socken zurück in den Haufen
```
Der Algorithmus terminiert nicht in jedem Fall, wenn ein Socken keine Paarung hat, der Haufen eine ungerade Anzahl an Socken enthält oder die ausgewählten Socken nicht zusammenpassen.

## 2)

Die Laufzeit des angegebenen Algorithmus beträgt bei 100 Socken im schlimmsten Fall 99 + 97 + 95 + ... + 3 + 1 = 2500 Vergleiche.  
Das lässt sich auch schreiben als die Hälfte der Summe von 1 bis n oder (n*(n+1))/4.

## 3a)

```
Solange der Haufen nicht leer ist:
    Nehme einen Socken
    Lege den Socken auf den Stapel der jeweiligen Farbe

Für jeden Stapel:
    Solange der Stapel nicht leer ist:
        Nehme einen Socken
        Für jeden weiteren Socken auf dem Stapel:
            Wenn die Socken das gleiche Modell sind:
            - Falte beide Socken zusammen
```

## 3b)

Bei diesem Algorithmus haben wir in der Sortierung 100 Vergleiche, wenn wir einen Farbvergleich mit einer Farbe nicht als Vergleich zählen, und 500 Vergleiche, wenn wir jeden Vergleich als Vergleich zählen.  
Dazu kommen nun im schlimmsten Fall 5*(19+17+15+...+1) = 500 Vergleiche.  
Insgesamt hat man also 600 Vergleiche mit nur Sockenvergleichen und 1000 Vergleiche mit allen Vergleichen.


# Quadratwurzel

## 1)

```
Setze n auf 2 (Zahl, von der die Quadratwurzel berechnet werden soll)
Setze x auf 0.2 (Siehe Beispiel)
Setze h auf n / x

Solange |x - h| > 0.00001:
    Setze x auf (x + h) / 2
    Setze h auf n / x

In x steht nun die Quadratwurzel von n auf fünf Nachkommastellen genau
```

## 2)

| Iteration |         x          |         h          |       Differenz       |
|-----------|--------------------|--------------------|-----------------------|
|         1 |                0.2 |               10.0 |                   9.8 |
|         2 |                5.1 | 0.3921568627450981 |     4.707843137254901 |
|         3 |  2.746078431372549 | 0.7283113173866477 |    2.0177671139859013 |
|         4 | 1.7371948743795984 | 1.1512813153528656 |    0.5859135590267328 |
|         5 | 1.4442380948662321 | 1.3848132154312434 |   0.05942487943498875 |
|         6 | 1.4145256551487377 | 1.4139015384558010 | 0.0006241166929368269 |
|         7 | 1.4142135968022693 | 1.4142135279439216 | 6.885834769043697e-08 |