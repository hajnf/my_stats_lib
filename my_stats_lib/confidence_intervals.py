import pandas as pd
import numpy as np
import math
from scipy import stats

def ci_2dependant_proportions(sample1, sample2, alpha=0.05):
    """
    Calcule l'intervalle de confiance pour la différence de proportions dans un échantillon apparié.

    Parameters:
        sample1 (array-like): Résultats du premier échantillon (par exemple, succès=1, échec=0)
        sample2 (array-like): Résultats du second échantillon apparié
        alpha (float): Niveau de confiance (par défaut 0.05 pour un intervalle à 95%)

    Returns:
        dict: Contenant la table de contingence, la différence estimée, et l'intervalle de confiance
    """

    # Convertir en pandas Series
    s1 = pd.Series(sample1)
    s2 = pd.Series(sample2)

    # Créer le tableau de contingence 2x2
    tab = pd.crosstab(s1, s2)

    # Vérifier que le tableau est 2x2
    if tab.shape != (2, 2):
        raise ValueError("Les données doivent former une table 2x2 avec des catégories binaires (0/1).")

    # Nombre total d'observations
    N = len(s1)

    # Nombre de succès dans chaque échantillon
    n1 = sum(s1)
    n2 = sum(s2)

    # Proportions
    P1 = n1 / N
    P2 = n2 / N

    # Quantile Z pour l'intervalle de confiance
    z = stats.norm.ppf(1 - alpha/2)

    # Proportions observées dans la table
    Pij = tab / N
    P11 = Pij.iloc[0, 0]
    P12 = Pij.iloc[0, 1]
    P21 = Pij.iloc[1, 0]
    P22 = Pij.iloc[1, 1]

    # Différence estimée
    diff = P1 - P2

    # Calcul de la marge d'erreur
    marg_error = z * math.sqrt((P1*(1 - P1) + P2*(1 - P2) - 2*(P11*P22 - P12*P21)) / N)

    # Intervalle de confiance
    ci_lower = diff - marg_error
    ci_upper = diff + marg_error

    return {
        'contingency_table': tab,
        'difference': diff,
        'ci_lower': ci_lower,
        'ci_upper': ci_upper
    }