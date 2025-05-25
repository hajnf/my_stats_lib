# my_stats_lib

Une bibliothèque Python pour le calcul des intervalles de confiance, notamment pour des proportions dépendantes.

## Installation

Dans le dossier racine du projet, exécutez :

```bash```

pip install . 
```

```python```


from my_stats_lib import ci_2dependant_proportions

sample1 = [1, 0, 1, 1, 0, 0, 1]
sample2 = [0, 0, 1, 0, 1, 0, 1]

result = ci_2dependant_proportions(sample1, sample2, alpha=0.05)
print(f"Intervalle : [{result['ci_lower']:.3f}, {result['ci_upper']:.3f}]")

```