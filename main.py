roboty = {
    "R2D2": "opravář",
    "C3PO": "překladatel",
    "WALL-E": "sběrač odpadu",
    "T-800": "ochránce",
    "Baymax": "lékařský asistent"
}

while True:
    jmeno = input("Zadej jméno robota (nebo 'konec' pro ukončení): ")
    if jmeno.lower() == "konec":
        break

    if not jmeno:
        print("Jméno robota nemůže být prázdné. Zkuste to znovu.")
        continue

    if jmeno in roboty:
        print("Funkce robota:", roboty[jmeno])
    else:
        funkce = input("Robot neexistuje. Zadej jeho funkci: ")
        if funkce:
            roboty[jmeno] = funkce
            print(f"Robot {jmeno} byl přidán s funkcí: {funkce}")
        else:
            print("Funkce nemůže být prázdná. Robot nebyl přidán.")

print("Seznam robotů:")
for jmeno, funkce in roboty.items():
    print(f"{jmeno}: {funkce}")
