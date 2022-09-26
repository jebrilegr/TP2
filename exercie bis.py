jour = int(input("saisir le jour : "))
mois = int(input("saisir le mois : "))
annee = int(input("saisir l'annee : "))

print(f"La date choisie est {jour}/{mois}/{annee}")

if(annee%4==0 and annee%100!=0 or annee%400==0):
    print(f"L'année {annee} est bissextile. ")
    isbissxtile=True
else :
    print(f"L'année {annee} n'est pas bissextile. ")
    isbissxtile=False

