# my_stats_lib

Un package Python pour le calcul des intervalles de confiance, notamment pour des proportions dépendantes.

## Installation (locale, après avoir cloné ou téléchargé le package)

Dans le dossier racine du projet, exécutez la commande suivante dans le terminal :

```bash```

pip install . 
```
##Utilisation dans Python
Exemple qui montre comment importer et utiliser la fonction ci_2dependant_proportions dans un script Python :

```python```


from my_stats_lib import ci_2dependant_proportions

sample1 = [1, 0, 1, 1, 0, 0, 1]
sample2 = [0, 0, 1, 0, 1, 0, 1]

result = ci_2dependant_proportions(sample1, sample2, alpha=0.05)
print(f"Intervalle : [{result['ci_lower']:.3f}, {result['ci_upper']:.3f}]")

```
