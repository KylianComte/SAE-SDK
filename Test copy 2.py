import numpy as np
import matplotlib.pyplot as plt

# Fréquences et paramètres du filtre
fc = 1e9  # fréquence centrale (1 GHz)
bw_3db = 200e6  # bande passante à -3 dB (200 MHz)
bw_xxdb = 400e6  # bande passante à -XX dB (400 MHz)
insertion_loss = 1  # perte d'insertion en dB

# Fréquences de coupure
f_3db_1 = fc - bw_3db / 2
f_3db_2 = fc + bw_3db / 2
f_xxdb_1 = fc - bw_xxdb / 2
f_xxdb_2 = fc + bw_xxdb / 2

# Définition de la fonction de transfert S21
def s21(f, fc, bw_3db):
    return 1 / np.sqrt(1 + ((f - fc) / (bw_3db / 2))**2)

# Générer un tableau de fréquences
frequencies = np.linspace(fc - 2 * bw_xxdb, fc + 2 * bw_xxdb, 1000)

# Calculer la réponse en dB
s21_values = 20 * np.log10(s21(frequencies, fc, bw_3db)) - insertion_loss

# Création de la figure
plt.figure(figsize=(8, 6))

# Tracer la courbe de réponse du filtre
plt.plot(frequencies, s21_values, label='S21 (dB)', color='red')

# Ajouter les bandes passantes
plt.axvline(f_3db_1, color='black', linestyle='--')
plt.axvline(f_3db_2, color='black', linestyle='--')
plt.axvline(f_xxdb_1, color='gray', linestyle='--')
plt.axvline(f_xxdb_2, color='gray', linestyle='--')

# Annotation des fréquences
plt.text(fc, -3, '-3 dB', verticalalignment='bottom', horizontalalignment='center')
plt.text(fc, -20, '-XX dB', verticalalignment='bottom', horizontalalignment='center')
plt.text(fc, -20, '-7.96dB', verticalalignment='top', horizontalalignment='left')


# Définir les limites et les étiquettes
plt.ylim(-20, 0)
plt.xlim(fc - 2 * bw_xxdb, fc + 2 * bw_xxdb)
plt.xlabel('Fréquence (Hz)')
plt.ylabel('S21 (dB)')
plt.title('Gabarit du filtre')
plt.grid(True)
plt.legend()

# Afficher le graphique
plt.show()
