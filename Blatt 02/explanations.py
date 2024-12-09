## For loop
testList = [x*2 for x in range(10)] # Füllt die Liste mit x*2 für x von 0 bis exklusiv 10

for i in range(0, len(testList), 2):    # Iteriert von 0 bis exklusiv 10 in 2er Schritten
    print(i)

for e in testList:  # Iteriert über alle Elemente aus der Liste
    print(e)

# Wir können ein Paar im for loop mit zwei Variablen direkt einlesen
# Genau wie zB.: a, b = (1, 2)
for i, e in enumerate(testList):    # Iteriert über alle index, value Paare der Liste
    print(f"{i}, {e}")
    # z.B. (0, 0), (1, 2), etc.

for i, e in zip(range(len(testList)), testList):    # Ist das gleiche wie enumerate nur ausgeschrieben
    print(f"{i}, {e}")
# zip verbindet 2 Listen in eine Liste, sodass in jedem Wert ein Tupel der jeweiligen Werte steht


## Funktionen
# Generelle Form einer Funktion
def add(a, b):
    print(f"{a=}, {b=}")
    return a + b

print(add(2, 3))

## f-string
# Normale Ausgabe
print("Eins ist " + str(1) + " und zwei ist " + str(2))
print("Eins ist", 1, "und zwei ist", 2)
print(1, 2)

# Ein f string mit a= gibt aus 'a=[Wert von a]'
a = 2
b = 3
print(f"a ist {a=} und b ist {b=}")

# Ein f string mit einem float und hier :.5 gibt den float Wert auf 5 Nachkommastellen gerundet aus
f = 0.12312312312412512545
print(f"{f:.5}")

# Hier füllen wir den gegebenen String bis zu einer Länge 10 mit # auf
# Dabei gibt ^, dass der String zentriert sein soll
# < ist linksbündig und > rechtsbündig
# Für auffüllen mit spaces kann das Symbol hier # weggelassen werden.
print(f"{'test':#<10}")