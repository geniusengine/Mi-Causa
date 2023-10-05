"""
 _______       _            _     _          ______        _                 _ 
(_______)     (_)       _  (_)   | |        (____  \      (_)               | |
 _______  ____ _  ___ _| |_ _  __| |_____    ____)  ) ____ _ _____ ____   __| |
|  ___  |/ ___) |/___|_   _) |/ _  | ___ |  |  __  ( / ___) (____ |  _ \ / _  |
| |   | | |   | |___ | | |_| ( (_| | ____|  | |__)  ) |   | / ___ | | | ( (_| |
|_|   |_|_|   |_(___/   \__)_|\____|_____)  |______/|_|   |_\_____|_| |_|\____|
    
Auteur: danie(danie.pro@gmail.com) 
database.py(Ɔ) 2023
Description : Saisissez la description puis « Tab »
Créé le :  mercredi 4 octobre 2023 à 22:58:02 
Dernière modification : mercredi 4 octobre 2023 à 22:59:13
"""
import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication


# Función para crear y abrir la conexión a la base de datos MySQL
def create_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="mi_usuario",
            password="mi_contraseña",
            database="mi_basededatos"
        )

        if connection.is_connected():
            print("Conexión a MySQL exitosa.")
            return connection

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

def main():
    app = QApplication(sys.argv)
    
    # Crear y abrir la conexión a la base de datos MySQL
    db_connection = create_db_connection()
    
    # Puedes pasar la conexión a la ventana principal o cualquier widget que la necesite
    main_menu = MainMenu(db_connection)
    main_menu.show()
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

