# **Aufgabe Konzeptionelle Fragen**
### Im Folgenden sollen eher konzeptionelle Fragen beantwortet werden. Geben Sie kurze Erklärungen im Freitext (typischerweise 1 Satz pro Aussage). Es kann durchaus viele verschiedene richtige Antworten geben, Mehrfachantworten sind aber nicht nötig
<br>

## **1)** Statische Typisierung: In Python können Typen von Variablen mit Typannotationen versehen (und dann mit mypy geprüft werden). Nennen Sie je einen Vor- und einen Nachteil davon, Variablen im Programmcode mit festen Typen zu versehen (für ExpertInnen: wir nutzen keine Generics).
```
Zum einen werden Fehler frühzeitig erkannt, zum anderen ist es aber auch möglich, dass bestimmte Typen erst zur Laufzeit bekannt sind,
was einen deutlich größeren Aufwand bedeutet.
```
<br>

## **2)** Objekte & Referenzen: Lesen Sie den folgenden Programmcode und geben Sie das Ergebniss der Vergleiche (a) und (b) (c) und (d) mit Begründung an.
```py
# This class can be used to store a fraction. The denominator has to be != 0
class Frac:
    def __init__(self, num, denum):
        self.num = num
        if denum != 0:
            self.denum = denum
        else:
            raise ValueError("Denominator has to be != 0")

    def __eq__(self, other):
        return other.num == self.num and other.denum == self.denum

# Create two Instances of Frac
x = Frac(2,3)
y = Frac(2,3)
z = x

# (a)
x == y

# (b)
x is y

# (c)
x == z

# (d)
x is z
```
```
a) True
    Ist über die __eq__ Methode definiert, die beiden Instanzen sind gleich.

b) False
    Die beiden Instanzen sind nicht identisch, da sie sich an unterschiedlichen Speicheradressen befinden.

c) True
    Da z auf x verweist, sind die beiden Instanzen gleich.

d) True
    Da z auf x verweist, sind die beiden Instanzen identisch.
```
<br>

## **3)** Objekte & Referenzen: die Funktion replace_nan soll alle nan-Werte in einer Liste durch den Wert 0 ersetzen. Dies kann z.B. bei einem Experiment mit fehlenden Messwerten notwendig sein. Welche der beiden Funktionen liefert das korrekte Ergebniss und warum?
```py
from copy import deepcopy

x = [None,2,3,None,5]
y = deepcopy(x)

# Replaces nan values with 0
def replace_nan1(arr):
    for val in arr:
        if val is None:
            val = 0

# Replaces nan values with 0
def replace_nan2(arr):
    for i in range(len(arr)):
        if arr[i] is None:
            arr[i] = 0
```
```	
Die Funktion replace_nan2 liefert das korrekte Ergebnis, da die Liste direkt verändert wird, während in replace_nan1 nur eine Kopie der
Liste verändert wird.
Dies liegt daran, dass val in replace_nan1 nur eine Kopie des Wertes ist und eine Änderung von val nicht die Liste verändert.
```