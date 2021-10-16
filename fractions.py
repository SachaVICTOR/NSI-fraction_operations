#GROUPE 2


def meme_denominateur(fraction1,fraction2):
  """ 
  Cette fonction verifie que les dénominateurs sont les mêmes 
  et si ce n'est pas le cas, les met au même dénominaeur

  >>> meme_denominateur([2,4],[2,2])
  ([4, 8], [8, 8])
  >>> meme_denominateur([1,2],[3,2])
  ([1, 2], [3, 2])
  """
  if fraction1[1]!=fraction2[1]:

    multiplicateur1 = fraction2[1]
    multiplicateur2 = fraction1[1]

    #Cette boucle bornée multiplie chaque fraction par le dénominateur de l'autre fraction
    for i in range(0,2):

      fraction1[i] *= multiplicateur1
      fraction2[i] *= multiplicateur2

  return fraction1,fraction2


def reduire(fraction):
  """
  Cette fonction permet de réduire, si possible, une fraction.

  >>> reduire([4, 8])
  [1, 2]

  >>> reduire([3, 5])
  [3, 5]
  """
  #Cette boucle bornée parcours dans l'ordre décroissant les nombres inférieurs au dénominateur de la fraction
  for i in range(fraction[1],1,-1):

    if fraction[1]%i + fraction[0]%i == 0:

      fraction[0]=int(fraction[0]/i)
      fraction[1]=int(fraction[1]/i)
      break

  return fraction
    

def produit(fraction1,fraction2):
  """
  Cette fonction permet d'obtenir le produit de deux fractions.

  >>> produit([1, 1], [2, 1])
  [2, 1]
  >>> produit([1, 320], [2, 2])
  [1, 320]
  """

  #On multiplie les numérateurs entre eux et les dénominateurs entre eux.
  resultat = [fraction1[0]*fraction2[0],fraction1[1]*fraction2[1]]

  return reduire(resultat)


def division(fraction1,fraction2):
  """
  Cette fonction permet d'obtenir le produit de deux fractions.

  >>> division([1, 1], [2, 1])
  [1, 2]
  >>> division([1, 320], [2, 2])
  [1, 320]
  """

  #On inverse la seconde fraction
  fraction2.reverse()

  #On récupere le produit des deux fractions
  resultat = produit(fraction1,fraction2)

  return reduire(resultat)


def somme(fraction1,fraction2):
  """
  Cette fonction permet d'obtenir la somme de deux fractions.

  >>> somme([1, 1], [2, 1])
  [3, 1]
  >>> somme([1, 320], [2, 2])
  [321, 320]
  """

  #On s'assure que les fractions soit au même dénominateur
  fraction1,fraction2 = meme_denominateur(fraction1,fraction2)

  #On récupere le dénominateur commun
  denominateur = fraction1[1]

  #On crée une liste resultat contenant la somme des numérateurs ainsi que le dénominateur de nos deux fractions.
  resultat = [fraction1[0] + fraction2[0], denominateur] 

  return reduire(resultat)


def soustraction(fraction1,fraction2):
  """
  Cette fonction permet de soustraire une fraction à une autre.

  >>> soustraction([1, 1], [2, 1])
  [-1, 1]
  >>> soustraction([1, 320], [2, 2])
  [-319, 320]
  """
  #On s'assure que les fractions soit au même dénominateur
  fraction1,fraction2 = meme_denominateur(fraction1,fraction2)

  #On récupere le dénominateur commun
  denominateur = fraction1[1]

  #On crée une liste resultat contenant la somme des numérateurs ainsi que le dénominateur de nos deux fractions.
  resultat = [fraction1[0] - fraction2[0], denominateur]

  return reduire(resultat)


if __name__ == "__main__":
  """
  Cette expression conditionnelle permet de vérifier que ce fichier est éxécuté en tant que 
  script et pas simplement appelé en tant que librairie externe. 
  Si c'est le cas doctest est importé et est éxécuté.
  """
  import doctest
  doctest.testmod()
