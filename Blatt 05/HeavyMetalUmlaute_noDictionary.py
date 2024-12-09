def translateToHeavyMetalSplitted(s: str):
    counterA = 0
    counterO = 0
    counterU = 0  
    translated = False

    out = ""

    for c in s:
        if not translated and c in "aA":
            counterA += 1
            if counterA == 2:
                c = "ä" if c == "a" else "Ä"
                translated = True
        elif not translated and c in "oO":
            counterO += 1
            if counterO == 2:
                c = "ö" if c == "o" else "Ö"
                translated = True
        elif not translated and c in "uU":
            counterU += 1
            if counterU == 2:
                c = "ü" if c == "u" else "Ü"
                translated = True
        else:
            if c == " ":
                translated = False
                counterA = 0
                counterO = 0
                counterU = 0
            
        out += c
        
    return out


if __name__ == '__main__':
    tests = {
        "Motorhead": "Motörhead",
        "Heavy Metal Umlaute": "Heavy Metal Umlaüte",
        "aaauuu oooo iii kukukuku": "aäauuu oöoo iii kukükuku",
        "Python super Programmiersprache": "Python super Programmierspräche"
    }

    results = [None for _ in range(len(tests))]

    for i, test in enumerate(tests):
        res = translateToHeavyMetalSplitted(test)
        results[i] = res == tests[test]

        print(
            f"Test:     {test}\n" + 
            f"Erwartet: {tests[test]}\n" + 
            f"Ergebnis: {res}\n" + 
            f"{'OK' if res == tests[test] else 'FAIL'}\n"
        )

    print(f"Ergebnis: {sum(results)}/{len(results)}")