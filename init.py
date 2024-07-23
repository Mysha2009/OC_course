""" print (181*10)
nom = "shamy"
age = 19
print (f"bonjour, je m'appelle {nom} et j'ai {age} ans")
age = 29
print (f"bonjour, je m'appelle {nom} et j'ai {age} ans")
taille = 1.61
est_etudiant = True
type (nom)
print (f"bonjour, je m'appelle {nom}, j'ai {age} ans et ma taille est de {taille}")
if est_etudiant == True: 
    print (f"je suis une etudiante")
else:
    print (f"je ne suis pas une etudiante") """

""" amis = ["jeanne", "jean", "fabruce", "dominique"]
amis[2] = "lyam"
print (amis[0])
amis.remove("dominique")
amis.sort
print (amis)
 """


""" taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2
taux_de_conversion['twitter'] = 2.2

del taux_de_conversion['twitter']
print (taux_de_conversion) """

""" est_etudiant = True
majeure = True
if est_etudiant == True and majeure != True: 
    print (f"je suis une etudiante majeure")
elif majeure:
    print (f"je suis majeure")
else:
    print (f"je ne suis pas une etudiante")

fruit = "pomme"
match fruit:
    case "pomme":
        print("J'aime les pommes !")
    case "banane":
        print("Je n'aime pas les bananes.")
    case "orange":
        print("Les oranges sont bonnes pour la santé.")
    case _:
        print("Je ne connais pas ce fruit.") """


""" nombre_a_gauche = input("Entrez un nombre entier : ")
nombre_a_droite = input("Entrez un nombre entier : ")
operation = input("Entrez l'opération souhaitée ['+', '-', '*' ou '/'] : ")

resultat = 0

# Vérifie si les deux nombres sont valides avec la fonction
# isinstance (soit un integer, soit un float)
if not nombre_a_gauche.isnumeric() or not nombre_a_droite.isnumeric():
    print("Erreur: les deux nombres doivent être des nombres entiers")
else:
    nombre_a_gauche = int(nombre_a_gauche)
    nombre_a_droite = int(nombre_a_droite)
    
    match operation:
        case "+":
            resultat = nombre_a_gauche + nombre_a_droite
        case "-":
            resultat = nombre_a_gauche - nombre_a_droite
        case "*":
            resultat = nombre_a_gauche * nombre_a_droite
        case "/":
            # Vérifie si la variable `nombre_a_droite` n'est pas nulle pour la division
            if nombre_a_droite == 0:
                print("Erreur: impossible de diviser par zéro.")
            else:
                resultat = nombre_a_gauche / nombre_a_droite
        # Si on est dans le cas par défaut, c'est que le symbole est incorrect.
        case _:
            print("Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'.")

    # Affiche le résultat
    print(f"Le résultat de l'opération est: {resultat}")

if __name__ == "__main__": """

""" races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
for chien in races_de_chien:
print(chien)


for x in range(3,9):
print(f"{x} bouteilles de bières au mur !")

capacite_maximale = 10
capacite_actuelle = 3

while capacite_actuelle < capacite_maximale:
capacite_actuelle = capacite_actuelle + 1
print (capacite_actuelle) """

""" liste = [1, 2, 3, 4, 5]
# Boucle for sur la liste
for element in liste:
if element == 3:
    # Si l'élément vaut 3, on passe à l'itération suivante sans exécuter le reste du code
    break
# Dans tous les autres cas, on exécute le reste du code
print(element)

liste = input (f"entrez une liste de nombre")

somme = 0
liste = liste.split(",")
for i in liste:
somme += int(i)
print (somme)

moyenne = somme / len(liste)
print(moyenne)

x = 0
for i in liste:
if int(i) > moyenne:
    x = x + 1
print (x)

y = 0
for i in liste:
if int(i)% 2 == 0:
    y = y + 1
print (x) """

""" def afficher_message():
print("Bonjour, comment ça va ?")

afficher_message()

def somme(a,b):
resultat = a + b
return resultat
somm = somme(2,5)
print(somm)


def salaire_mensuel(salaire_annuel):
answer = salaire_annuel/12
return answer
ans = salaire_mensuel(12000)
print(ans)

def salaire_hor(hebdo, heure):
sal_horr = hebdo/heure
return sal_horr
sal = salaire_hor(1200, 8)
print(sal)

while True:
try:
    x = int(input("Entrez un nombre
      entier : "))
    break
except ValueError:
    print("Oops ! Ce n'est pas un nombre entier. Essayez encore...") """

