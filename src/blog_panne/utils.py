import pandas as pd

def lire_fichier_excel(chemin_fichier):
    df = pd.read_excel(chemin_fichier)
    return df