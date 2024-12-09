def translateToHeavyMetalSplitted(s: str):
    counters = [0, 0, 0]
    translated = False

    out = ""

    translation = {
        "a": "ä",
        "o": "ö",
        "u": "ü",
    }

    # [("a", "ä"), ("o", "ö"), ("u", "ü")]

    for c in s:
        # if there has been a space and the current character is in the translation
        if not translated and c.lower() in translation:
            # fancy way of counting the characters
            counters[list(translation.keys()).index(c.lower())] += 1
            # otherwise we would have to do this:
            # if c.lower() == "a":
            #     counters[0] += 1
            # elif c.lower() == "o":
            #     counters[1] += 1
            # elif c.lower() == "u":
            #     counters[2] += 1

            # if there has been two characters of one type in this word
            # we can skip checking which character because if one character was translated
            # this wouldn't be executed because translated is True
            # because of this the current character would be the one that hit the 2
            if 2 in counters:
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
                counters = [0, 0, 0]
            
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