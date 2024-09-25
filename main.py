#proměnná s jménem
print("Patrik")

#proměnná s příjmením
print("Fikacek")

#vstup pro uživatele
def ziskat_vek():
    while True:

            vek = int(input("Zadejte svůj věk: "))
            if vek > 0:
                return vek
            else:
                print("Neplatný Údaj, číslo musí být větší než nula!")
        
vek = ziskat_vek()
print(f"Váš věk je: {vek}")

#délka dvou proměných
string1 = "Patrik"
string2 = string1 + "Fikacek"
delka2 = len(string2)
print ("Délka prvního stringu:", len(string1))
print ("Délka obou stringu:", delka2)
print (string2)

#proměnná s hodnotou 6.
cislo=6
print("6")

     #cyklus (v úkolu nebylo specifikováno o jaký cyklus se jedná..., takže jsem si vybral cyklus for)
hodnota = 0

for i in range(5):
    hodnota += 3
    print(f"Opakování {i+1}: hodnota = {hodnota}")

     #konzole
print(f"Výsledná hodnota po 5 cyklech je: {hodnota}")

#podmínka pro uživatele
vek = input("Zadejte svůj věk: ")

     # Kontrola
if vek.isdigit():   #vek.isdigit je metoda v pythonu, která kontroluje zda je řetězec (vek) tvořen pouze číslicemi 0-9 např. vek obsahuje "25", vek.isdigit vrátí true, ale pokud se u číslo "25a" napíše to false.
    print("Děkuji")
else:
    print("Zadej jen celočíselnou hodnotu.")

#proměnná s náhodnou hodnotou od 1-10
import random

# generování náhodné hodnoty od 1 do 10
nahodna_hodnota = random.randint(1, 10)

# výpis náhodné hodnoty do konzole
print(f"Náhodná hodnota je: {nahodna_hodnota}")
