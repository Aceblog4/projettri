import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import time


# Couche application (graphique)

# Selection des fonctions
def Menu():
    print("Bienvenue dans ce programme de tri. Dans ce programme, nous allons"
          "trier une liste choisie par l'utilisateur.\nIl y a 3 type de liste :"
          "une non-triée(correspondant au pire cas), une choisie aléatoirement"
          "(cas moyen), et une déjà triée (meilleur cas).")
    input("Appuyez sur une touche pour continuer.............\n")


# Programme principal

MAX_LENGTH = 1_000_000

STEP = 1000
# Experimentation

"""
Procedure : 
    1 - Création d'un tableau variable pour évaluer la fiabilité temporelle des fonctions de tri de numpy
    2 - trier le tableau de variables pour de nombreuses longueurs, et voir comment le temps de traitement évolue avec la longueur
    3 - créer des résultats de sortie pour chaque méthode {'quicksort', 'mergesort', 'heapsort'}
"""

# DATA CREATION
KINDS = ['quicksort', 'mergesort', 'heapsort']

TIME_RESULT = []
length_array = []


def meilleur_cas():
    for kind in KINDS:
        kind_time_result = []
        if not length_array:
            fill_array = True
        else:
            fill_array = False

        for i in range(1, MAX_LENGTH + 2, STEP):
            if fill_array:
                length_array.append(i)
            X = np.arange(1, i + 2)
            start_time = time.time()
            a = np.sort(X, kind=kind)
            kind_time_result.append(time.time() - start_time)

        TIME_RESULT.append(kind_time_result)


def cas_moyen():
    for kind in KINDS:
        kind_time_result = []
        if not length_array:
            fill_array = True
        else:
            fill_array = False

        for i in range(1, MAX_LENGTH + 2, STEP):
            if fill_array:
                length_array.append(i)
            X = np.random.randint(1, i * 10, i)  # cas moyen
            start_time = time.time()
            a = np.sort(X, kind=kind)
            kind_time_result.append(time.time() - start_time)

        TIME_RESULT.append(kind_time_result)


def pire_cas():
    for kind in KINDS:
        kind_time_result = []
        if not length_array:
            fill_array = True
        else:
            fill_array = False

        for i in range(1, MAX_LENGTH + 2, STEP):
            if fill_array:
                length_array.append(i)
            X = np.arange(i + 1, 0, -1)  # cas moyen
            start_time = time.time()
            a = np.sort(X, kind=kind)
            kind_time_result.append(time.time() - start_time)

        TIME_RESULT.append(kind_time_result)


# SORTING CHOICE

Menu()
quest = str(input("Quel cas souhaitez-vous traiter ?\nRappel : il y a 3 "
                  "choix possibles, le meilleur, le pire ou "
                  "l'intermédiaire\n"))
if quest == 'Meilleur':
    meilleur_cas()
elif quest == 'Moyen' or 'intermédiaire':
    cas_moyen()
elif quest == 'Pire':
    pire_cas()

# DATA SET
data = np.array(TIME_RESULT)
data = data.transpose()
df = pd.DataFrame(data, columns=KINDS)
df.index = length_array

# AFFICHAGE de la DATAFRAME
print(df)

# PLOTTING RESULTS
"""
    
    =========== ======= ============= ============ ========
       kind      speed   worst case    work space   stable
    =========== ======= ============= ============ ========
    'quicksort'    1     O(n^2)            0          no
    'heapsort'     3     O(n*log(n))       0          no
    'mergesort'    2     O(n*log(n))      ~n/2        yes
    =========== ======= ============= ============ ========
    
"""

# Affichage des résultat sur MATPLOTLIB
plt.plot(length_array, df[KINDS[0]], length_array, df[KINDS[1]], length_array,
         df[KINDS[2]])
plt.legend(KINDS)
plt.title("Comparaison entre les methodes numpy")
plt.xlabel("Longueur de la serie utilisée")
plt.ylabel("Temps de traitement (s)")
plt.show()
