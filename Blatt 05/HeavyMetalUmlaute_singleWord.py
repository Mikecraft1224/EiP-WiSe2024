def translateToHeavyMetalUmlaute(s: str):
    translation = {
        "a": "ä",
        "o": "ö",
        "u": "ü",
    }

    def translateWord(s: str):
        sl = s.lower()
        for c in translation:
            if sl.count(c) >= 2:
                index = sl.index(c, sl.index(c) + 1)
                sub = translation[c]
                if s[index].isupper():
                    sub = sub.upper()
                return s[:index] + sub + s[index + 1:]
        return s
    
    return " ".join(translateWord(word) for word in s.split())