jour = int(input("saisir le jour : "))
mois = int(input("saisir le mois : "))
annee = int(input("saisir l'annee : "))

print(f"La date choisie est {jour}/{mois}/{annee}")

if annee % 4 == 0 and annee % 100 != 0 or annee % 400 == 0:
    print(f"L'année {annee} est bissextile. ")
    isbissxtile = True
else:
    print(f"L'année {annee} n'est pas bissextile. ")
    isbissxtile = False

if not (1 <= mois <= 12):
    print(f"Numéro de mois incorrect : {mois}")

if (mois == 2):
    if (isbissxtile):
        nbjours = 29
    else:
        nbjours = 28
if (mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12):
    nbjours = 31
if (mois == 4 or mois == 6 or mois == 9 or mois == 11):
    nbjours = 30

print(f"Le mois {mois}/{annee} compte {nbjours} jours.")

if (not(1<=jour and jour<=nbjours )):
    print(f" Numéro de jour incorrect : {jour} ")

if(jour>=21 and mois>=12 or jour<=19 and mois<=3 or mois==2 or mois==1) :
    print("Cette date est en hiver")
elif(jour>=20 and mois==3 or jour<=19 and mois==6 or mois==4 or mois==5 ) :
    print("Cette date est en printemps")
elif(jour>=20 and mois==6 or jour<=21 and mois==9 or mois==7 or mois==8) :
    print("Cette date est en ete")
elif(jour>=22 and mois==9 or jour<=20 and mois==12 or mois==10 or mois==11) :
    print("Cette date est en automne")


annee_1= 1
jours_ecoules=annee_1*annee
if(isbissxtile) :
    print(f"il s'est ecoule {jours_ecoules+1} jours entre le 1/1/1 et le {jour}/{mois}/{annee}")
else :
    print(f"il s'est ecoulé {jours_ecoules} jours entre le 1/1/1 et le {jour}/{mois}/{annee}")
