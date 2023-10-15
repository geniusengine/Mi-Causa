"""
 _______       _            _     _          ______        _                 _ 
(_______)     (_)       _  (_)   | |        (____  \      (_)               | |
 _______  ____ _  ___ _| |_ _  __| |_____    ____)  ) ____ _ _____ ____   __| |
|  ___  |/ ___) |/___|_   _) |/ _  | ___ |  |  __  ( / ___) (____ |  _ \ / _  |
| |   | | |   | |___ | | |_| ( (_| | ____|  | |__)  ) |   | / ___ | | | ( (_| |
|_|   |_|_|   |_(___/   \__)_|\____|_____)  |______/|_|   |_\_____|_| |_|\____|
    
Auteur: danie(danie.pro@gmail.com) 
ayuda.py(Ɔ) 2023
Description : Saisissez la description puis « Tab »
Créé le :  samedi 14 octobre 2023 à 15:46:58 
Dernière modification : samedi 14 octobre 2023 à 15:47:15
"""
import os
import shutil

# Ruta de la carpeta dist
dist_folder = 'dist'

# Verifica si la carpeta existe antes de intentar eliminarla
if os.path.exists(dist_folder):
    try:
        # Elimina la carpeta dist y su contenido
        shutil.rmtree(dist_folder)
        print(f'La carpeta {dist_folder} ha sido eliminada.')
    except Exception as e:
        print(f'Error al eliminar la carpeta {dist_folder}: {e}')
else:
    print(f'La carpeta {dist_folder} no existe.')
