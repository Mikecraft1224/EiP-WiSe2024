# Import
from jguvc_eip import basic_io


# Funktionen
def main() -> int:
    "Startet das Hauptprogramm"

    a = 42
    b = 420

    print(f"a ist {a} und b ist {b} und a+b ist {a+b}")

    return a+b


# Mainguard
if __name__ == '__main__':
    main()