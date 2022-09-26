jour = int(input("saisir le jour : "))
mois = int(input("saisir le mois : "))
annee = int(input("saisir l'annee : "))

print(f"La date choisie est {jour}/{mois}/{annee}")

if(annee%4==0 and annee%100!=0 or annee%400==0):
    print(f"L'année {annee} est bissextile. ")
    isbissxtile=True
else:
    print(f"L'année {annee} n'est pas bissextile. ")
    isbissxtile=False

if(not(1<=mois and mois<=12)):
    print(f"Numéro de mois incorrect : {mois}")

if(mois==2):
    if(isbissxtile):
        nbjours= 29
    else:
        nbjours= 28
if(mois==1 or mois==3 or mois==5 or mois==7 or mois==8 or mois==10 or mois==12):
    nbjours=31
if(mois==4 or mois==6 or mois==9 or mois==11 ):
    nbjours=30

