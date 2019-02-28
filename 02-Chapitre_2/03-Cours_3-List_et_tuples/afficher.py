# -*-coding:utf-8 -*
def afficher(*values, sep=' ',fin='\n'):
  values = list(values)
  for i, value in enumerate(values):
    values[i] = str(value)
    i += 1
  chaine = sep.join(values) + fin
  print(chaine)


afficher(' ', '\n', "hello", "je", "test", 3)
