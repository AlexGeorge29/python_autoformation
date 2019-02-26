# -*-coding:utf-8 -*
import random
# 0 Fonctions
def miser():
  numero = input("jouer un numéro entre 0 et 49: ")
  parie = input("mise sur ce numero: ")
  return [numero, parie]
def tourner_roue():
  return random.randrange(50)
# 1 - Joueur mise un numero
mise = miser()
if mise[0] >= 49 or mise[0] < 0:
  mise = miser()
else:
  print("numero joué: ")
  print(mise[0])
  print("Mise est de :")
  print(mise[1])
# 2 - La roue tourne
numero_gagnant = tourner_roue()
print("numero gagnat est: ")
print(numero_gagnant)
# 3 - Resultat
if numero_gagnant == mise[0]:
  result = 3 * mise[1]
elif (numero_gagnant % 2 == 0 and mise[0] % 2 == 0) or (numero_gagnant % 2 == 1 and mise[0] % 2 == 1):
  result = mise[1] / 2
else:
    result = 0
print("les gains sont de: ")
print(result)
