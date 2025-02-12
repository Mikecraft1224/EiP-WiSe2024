# **Aufgabe Verständnisfragen**

### Zum besseren Verständnis, zunächst eine paar Theoriefragen. Antworten Sie mit ja/nein und begründen Sie ihre Antwort.

## **1a)** Im schlimmsten Fall muss ein backtracking Algorithmus alle gültigen Kombinationen / alle mögliche Lösungen im Problemraum aufzählen und hat somit eine exponentielle (also sehr langsame) Laufzeit.
```
Ja, wenn die richtige Lösung die allerletzte Möglichkeit ist und alle anderen Möglichkeiten ausprobiert werden müssen, ist die Laufzeit exponentiell.
```

## **1b)** Ein backtracking Algorithmus kann nicht iterativ geschrieben werden.
```
Nein, ein backtracking Algorithmus kann auch iterativ geschrieben werden, ist aber rekursiv einfacher zu schreiben.
```

## **1c)** Ein backtracking Algorithmus eignet sich besonders für schwere Probleme, also Probleme bei denen sich die Menge aller möglichen Lösungen als baumartige Struktur darstellen lässt.
```
Ja, da er alle möglichen Lösungen rekursiv wie einen Baum durchgeht.
```

## **1d)** Backtracking ist ein rekursiver Algorithmus, deswegen ist es unsinnig darin for-Schleifen zu verwenden.
```
Nein, for Schleifen können in einem rekursiven Algorithmus ebenfalls verwendet werden, zum Beispiel um alle möglichen nächsten Schritte in jedem Schritt durchzugehen.
```

## **1e)** Backtracking und branch and bound Algorithmen unterscheiden sich fundamental nur durch einer zusätzliche if-Abfrage.
```
Im Prinzip ja, da branch and bound Algorithmen eine zusätzliche Bedingung haben, die erfüllt sein muss, damit ein Pfad weiter verfolgt wird, in der Regel eine Abfrage, ob bereits eine bessere Lösung gefunden wurde.
```
<br>

# **Aufgabe Labyrinth: Branch and Bound**

## **2b)** Was passiert durch die in 2a) vorgenommene Modifikation mit dem Baum aller möglichen Lösungen, den wir mithilfe unseres Algorithmus durchlaufen?
```
Dadurch, dass wir den Baum nicht mehr vollständig durchlaufen, sondern nur bis zu einer bestimmten Tiefe, wird der Baum kleiner und die Laufzeit kürzer.
```
<br>

# **Aufgabe Subset Sum**

## **1b)** Messen Sie die Laufzeit ihres Algorithmus.
```
Die Funktion benötigt ungefähr 0.0002s.
```

## **2b)** Messen Sie die Laufzeit ihres Algorithmus. Welche Funktionsaufrufe haben Sie eingespart?
```
Die Funktion benötigt ungefähr 0.00015s. Dabei werden alle Funktionsaufrufe eingespart, die zu einer Summe führen, die größer als das maximale Gewicht ist.
```

## **3b)** Messen Sie die Laufzeit ihres Algorithmus und vergleichen Sie diese mit den vorherigen Laufzeiten. Verändern Sie den Wert max_weight auf 1000 und messen Sie erneut alle drei Laufzeiten. Was fällt Ihnen auf? Erklären Sie ihre Beobachtungen.
```
Die Funktion benötigt ungefähr 0.00011s.
Im Vergleich zu den vorherigen Funktionen ist die Laufzeit deutlich kürzer, da hier nicht alle möglichen Kombinationen ausprobiert werden, sondern nur die, die in die Tabelle passen.
Bei einem max_weight von 1000 ist dies allerdings anders herum.
1a) benötigt 0.00023s, 2a) benötigt 0.00027s und 3a) benötigt 0.0013s.
Das liegt daran, dass die Tabelle größer ist und somit mehr Berechnungen durchgeführt werden müssen.
```