import requests
from pystyle import Colorate, Colors
from colorama import Fore
import os

def start_search():
    folder_path = "databases"  # dossier contenant les fichiers
    query = input(Colorate.Horizontal(Colors.green_to_cyan, "\n[-] Entrez un pseudo ou MDP à rechercher : ")).strip()
    print("\n")

    found = False

    # On parcourt tous les fichiers du dossier databases
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath) and filename.endswith(".txt"):
            with open(filepath, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for num, line in enumerate(lines, start=1):
                    if query.lower() in line.lower():
                        try:
                            email, mdp = line.strip().split(":", 1)
                        except ValueError:
                            email, mdp = line.strip(), "N/A"
                        file_without_ext = os.path.splitext(filename)[0]
                        print(Colorate.Horizontal(Colors.green_to_cyan,
                            f"[+] Trouvé dans la database {Fore.YELLOW}{file_without_ext}{Fore.RESET} à la ligne {Fore.MAGENTA}{num}{Fore.RESET} : "
                            f"Email = {email}, Mot de passe = {mdp}"))
                        found = True

    if not found:
        print(Colorate.Horizontal(Colors.red_to_purple, "[!] Aucun résultat trouvé."))

def close():
    input(Colorate.Horizontal(Colors.cyan_to_blue, "\n[-] Appuyez sur Entrée pour quitter..."))

text = """

██████╗░░█████╗░████████╗░█████╗░██████╗░░█████╗░░██████╗███████╗  ░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝  ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║
██║░░██║███████║░░░██║░░░███████║██████╦╝███████║╚█████╗░█████╗░░  ╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║
██║░░██║██╔══██║░░░██║░░░██╔══██║██╔══██╗██╔══██║░╚═══██╗██╔══╝░░  ░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║
██████╔╝██║░░██║░░░██║░░░██║░░██║██████╦╝██║░░██║██████╔╝███████╗  ██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝


"""

menu_text = Colorate.Vertical(Colors.blue_to_green, text) + "\n" + Colorate.Horizontal(
    Colors.cyan_to_blue,
    """
[-] 1 - Lancer le scan des bases de données
[-] 2 - Quitter
"""
)

def menu():
    while True:
        print(menu_text)
        choice = input(Colorate.Horizontal(Colors.green_to_cyan, "[-] Entrez votre choix : "))

        if choice == "1":
            start_search()
            print(Colorate.Horizontal(Colors.blue_to_green, "\n[-] Scan terminé."))
            close()
            break
        elif choice == "2":
            print(Colorate.Horizontal(Colors.red_to_purple, "\n[!] Au revoir !"))
            break
        else:
            print(Colorate.Horizontal(Colors.red_to_purple, "[!] Choix invalide, veuillez réessayer."))

if __name__ == "__main__":
    menu()
