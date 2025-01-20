def check_pin(pin: str):
    """Checks if a pin is correct. Returns a bool.
    Takes a pin given as a string as input.
    """
    assert isinstance(pin, str), "Pin needs to be a string"
    assert len(pin) == 10, f"Pin needs exactly 10 digits"
    return pin == "1234543210"

# 4a
def checkPinList(pinList):
    for pin in pinList:
        if check_pin(pin):
            return pin
        
    return False

# 4b
# Die Funktion checkAllPins() ist normalerweise nicht sinnvoll, da sie eine sehr lange Laufzeit hat.
def checkAllPins():
    for i in range(10000000000):
        if (i % 1000000) == 0:
            print(f"{i:_}")

        if check_pin(f"{i:010d}"):
            return i
        
    return False

print(checkAllPins())