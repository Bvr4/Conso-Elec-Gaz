"""Caution : work in progress"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from dataloaders.initial_consumptions_import import initial_consumptions_import

# df_conso_dep = pd.read_csv('datas/conso-elec-gaz-annuelle-par-secteur-dactivite-agregee-departement.csv', sep=";")

# del df_conso_dep['operateur']
# # On fait un group by pour avoir une seule ligne par filière
# df_conso_dep = df_conso_dep.groupby(['annee', 'filiere', 'code_departement','libelle_departement', 'code_region', 'libelle_region']).sum() 
# # On fait un reset index pour pouvoir accéder aux colonnes du group by comme avant
# df_conso_dep = df_conso_dep.reset_index()


initial_consumptions_import()