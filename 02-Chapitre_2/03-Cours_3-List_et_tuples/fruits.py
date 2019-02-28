# -*-coding:utf-8 -*
inventaire = [("pommes", 22), ("melons", 4), ("poires", 18), ("fraises", 76), ("prunes", 51)]

# for elmt in inventaire:
#   print(elmt[1])
inventaire_inverse = [(b,a) for (a,b) in inventaire ]
inventaire_inverse.sort()
print(inventaire_inverse)
