# -*-coding:utf-8 -*

# Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
# Si elle est multiple de 4, on regarde si elle est multiple de 100.
# Si c'est le cas, on regarde si elle est multiple de 400.
# Si c'est le cas, l'année est bissextile.
# Sinon, elle n'est pas bissextile.
# Sinon, elle est bissextile.

annee = input("Saisissez une année : ")
annee = int(annee)
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")
