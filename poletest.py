zbozi = {
    1: "3060",
    2: "3070",
    3: "3080",
    4: "3080ti",
    5: "3090",
    6: "3090ti",
    7: "4060ti",
    8: "4060"
}


kosik = []


def vyber_zbozi():
    print("Vyberte zbozi podle čisla:")
    for cislo, zbozi_nazev in zbozi.items():
        print(f"{cislo}: {zbozi_nazev}")
    

    while True:
        vyber = input("Zadejte číslo zboží (nebo 'konec' pro ukončení nákupu): ")
        if vyber.lower() == "konec":
            break
        elif vyber.isdigit() and int(vyber) in zbozi:
            kosik.append(zbozi[int(vyber)])
        else:
            print("Prosím, zadejte platné číslo z nabídky.")


def zobraz_kosik():
    print("Stav vašeho košíku:")
    if kosik:
        for zbozi_v_kosiku in kosik:
            print("-", zbozi_v_kosiku)
    else:
        print("Košík je prázdný.")


vyber_zbozi()

# Zobrazit stav košíku
zobraz_kosik()