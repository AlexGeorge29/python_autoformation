# -*-coding:utf-8 -*
def afficher(*values):
  values = list(values)
  for i, value in enumerate(values):
    values[i] = str(value)
    i += 1
  chaine = ' '.join(values)
  print(chaine)


afficher("hello", "je", "test", 3)
