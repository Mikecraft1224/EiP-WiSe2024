def translateToHeavyMetalTogether(s: str):
    counter = 0
    translated = False

    out = ""

    translation = {
        "a": "ä",
        "o": "ö",
        "u": "ü",
    }

    for c in s:
        # if there has been a space and the current character is in the translation
        if not translated and c.lower() in translation:
            counter += 1

            # if there has been two characters in this word
            if counter == 2:
                # add the tranlated character to the output in the correct case
                out += translation[c.lower()] if c.islower() \
                    else translation[c.lower()].upper()
                translated = True
            else:
                out += c
        else:
            # reset the counter if there is a space
            if c == " ":
                translated = False
                counter = 0
            
            out += c
        
    return out

if __name__ == '__main__':
    tests = {
        "Motorhead": "Motörhead",
        "Heavy Metal Umlaute": "Heavy Metal Umläute",
        "aaauuu oooo iii kukukuku": "aäauuu oöoo iii kukükuku",
        "Python super Programmiersprache": "Python super Progrämmiersprache"
    }

    results = [None for _ in range(len(tests))]

    for i, test in enumerate(tests):
        res = translateToHeavyMetalTogether(test)
        results[i] = res == tests[test]

        print(
            f"Test:     {test}\n" + 
            f"Erwartet: {tests[test]}\n" + 
            f"Ergebnis: {res}\n" + 
            f"{'OK' if res == tests[test] else 'FAIL'}\n"
        )

    print(f"Ergebnis: {sum(results)}/{len(results)}")