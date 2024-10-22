# Correction TP1
taches = []


def ajout_tache(tache):
    taches.append(tache)
    print("Tache ajoutée :", tache)


def voir_tache():
    print("Liste des taches")
    for indice, tache in enumerate(taches):
        print(f"{indice + 1}.{tache}")


def supprimer_tache(indice):
    if 0 <= indice < len(taches):
        supprimer_tache = taches.pop(indice)
        print(f"tache supprimée : {supprimer_tache}")
    else:
        print("Indice invalide")


def run():
    while True:
        action = input(
            "Choisissez une action (ajouter, voir, supprimer, quitter) : ").strip().lower()
        if action == "ajouter":
            tache = input("Entrez la tache : ")
            ajout_tache(tache)
        elif action == "voir":
            voir_tache()
        elif action == "supprimer":
            indice = int(
                input("Entrez le numéro de la tache à supprimer : ")) - 1
            supprimer_tache(indice)
        elif action == "quitter":
            break
        else:
            print("Action non reconnue.")


if __name__ == "__main__":
    run()
